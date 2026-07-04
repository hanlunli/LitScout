import ollama
from typing import Dict, Any

def summarize_paper(paper: Dict[str, Any], model: str = "llama3.1") -> str:
    """
    Generate a concise summary of the paper's key contributions using Ollama.
    """
    prompt = f"""
    Title: {paper['title']}
    Authors: {', '.join(paper['authors'])}
    Abstract: {paper['summary']}
    
    Please provide a concise summary of this paper's key contributions, methodology, and main findings. 
    Keep it under 150 words.
    """
    
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": "You are an expert AI research assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response['message']['content'].strip()
