import ollama
from typing import List, Dict, Any

def analyze_literature(papers_with_summaries: List[Dict[str, Any]], model: str = "llama3.1") -> str:
    """
    Analyze the collected papers and their summaries to identify themes, gaps, and project ideas.
    """
    # Prepare the context
    context = ""
    for idx, paper in enumerate(papers_with_summaries, 1):
        context += f"Paper {idx}:\nTitle: {paper['title']}\nSummary: {paper['ai_summary']}\n\n"
        
    prompt = f"""
    Based on the following papers from recent literature:
    
    {context}
    
    Please provide an analysis in the following three sections:
    1. Common Themes: What are the recurring methodologies, topics, or trends across these papers?
    2. Research Gaps: What limitations exist? What hasn't been explored yet?
    3. Project Ideas: Suggest 2-3 concrete, actionable research or engineering project ideas based on these gaps and trends.
    
    Format the output clearly using Markdown headers for 'Common Themes', 'Research Gaps', and 'Project Ideas'.
    """
    
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": "You are a senior research scientist identifying trends and opportunities in scientific literature."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response['message']['content'].strip()
