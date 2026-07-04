import streamlit as st
from search import search_arxiv
from summarize import summarize_paper
from analyze import analyze_literature

st.set_page_config(page_title="LitScout AI", page_icon="🔍", layout="wide")

st.title("🔍 LitScout AI")
st.subheader("Agentic Literature Review & Research Gap Discovery System")

st.markdown("""
LitScout helps you navigate rapidly evolving scientific fields. Enter a research topic to automatically search arXiv, summarize key papers, compare methodologies, and discover emerging research gaps and project ideas.
""")

# Sidebar for configuration
with st.sidebar:
    st.header("Settings")
    ollama_model = st.text_input("Ollama Model", value="llama3.1")
    max_papers = st.slider("Number of papers to fetch", min_value=1, max_value=10, value=5)

# Main input
query = st.text_input("Enter a Research Topic (e.g., 'Agentic RAG for code generation')", "")

if st.button("Scout Literature"):
    if not query:
        st.warning("Please enter a research topic.")
    elif not ollama_model:
        st.warning("Please specify an Ollama model to use.")
    else:
        # Step 1: Search
        st.write("### 📚 1. Searching arXiv...")
        with st.spinner(f"Fetching top {max_papers} papers for '{query}'..."):
            try:
                papers = search_arxiv(query, max_results=max_papers)
                if not papers:
                    st.error("No papers found for this query.")
                    st.stop()
                st.success(f"Found {len(papers)} papers!")
            except Exception as e:
                st.error(f"Error searching arXiv: {e}")
                st.stop()
                
        # Step 2: Summarize
        st.write("### 📝 2. Summarizing Papers...")
        progress_bar = st.progress(0)
        
        for idx, paper in enumerate(papers):
            with st.spinner(f"Summarizing: {paper['title']}"):
                try:
                    ai_summary = summarize_paper(paper, model=ollama_model)
                    paper['ai_summary'] = ai_summary
                except Exception as e:
                    st.error(f"Error summarizing paper: {e}")
                    paper['ai_summary'] = "Summary generation failed."
            progress_bar.progress((idx + 1) / len(papers))
            
        st.success("Summaries generated!")
        
        # Display Papers and Summaries
        with st.expander("View Top Papers & Summaries", expanded=False):
            for paper in papers:
                st.markdown(f"**[{paper['title']}]({paper['url']})**")
                st.markdown(f"*Authors: {', '.join(paper['authors'])} | Published: {paper['published']}*")
                st.markdown(f"> {paper['ai_summary']}")
                st.divider()
                
        # Step 3: Analyze
        st.write("### 🧠 3. Analyzing Literature for Gaps & Ideas...")
        with st.spinner("Synthesizing common themes, research gaps, and project ideas..."):
            try:
                analysis_result = analyze_literature(papers, model=ollama_model)
                st.success("Analysis complete!")
                
                # Display Results
                st.markdown("---")
                st.markdown(analysis_result)
                
            except Exception as e:
                st.error(f"Error analyzing literature: {e}")
