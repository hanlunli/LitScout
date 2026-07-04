# LitScout AI

LitScout AI is an agentic literature review and research discovery system designed to help students, researchers, and engineers navigate rapidly evolving scientific fields.

Given a research topic, LitScout automatically searches relevant papers from arXiv, identifies the most relevant publications, summarizes key contributions, compares methodologies, and highlights emerging research gaps. The system then generates potential project and research ideas based on trends and limitations found in the literature.

## Key Features

* Automated arXiv paper discovery
* Local LLM-powered paper summarization using Ollama
* Cross-paper methodology comparison
* Research gap identification
* Project and research idea generation
* Interactive literature review reports

## Technology Stack

* Python
* Streamlit
* Ollama (Local LLMs)
* arXiv API (`arxiv` package)

## Setup Instructions

1. **Install Ollama:**
   Download and install Ollama from [ollama.com](https://ollama.com/).

2. **Pull a Model:**
   Open your terminal and pull a model. By default, LitScout uses `llama3.1`.
   ```bash
   ollama run llama3.1
   ```
   *You can exit the prompt after it finishes downloading.*

3. **Clone the repository and navigate to the LitScout directory.**

4. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

5. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the Streamlit app, execute the following command:

```bash
streamlit run app.py
```

Open your browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

## Example Use Cases

* Exploring new AI research areas
* Conducting literature reviews
* Finding undergraduate research project ideas
* Tracking emerging trends in machine learning, robotics, and healthcare AI
* Accelerating research onboarding for students and interns
