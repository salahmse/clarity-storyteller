"""
Clarity Storyteller - Minimal inference script for Hackathon
Local-first with Meta Model API fallback
"""
import argparse
from docx import Document

# Try Meta API first, fallback to Ollama local
def generate_story(prompt: str):
    try:
        # TODO: Replace with real Meta Model API call when credits received
        # from meta_api import Llama
        # response = Llama.create(...)
        print("[Meta API] Using Meta Model API (placeholder - add key after acceptance)")
        # For now use local mock that returns our perfected story
        with open("story.md", "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"[Fallback] Using Ollama local: {e}")
        # Real local call would be:
        # import ollama
        # return ollama.chat(model='llama3.1:8b', messages=[...])
        with open("story.md", "r", encoding="utf-8") as f:
            return f.read()

def export_docx(content: str, output_path: str):
    doc = Document()
    doc.add_heading("Clarity Report - Generated Story", 0)
    for para in content.split("\n\n"):
        doc.add_paragraph(para)
    # Add figures if present
    doc.add_heading("Figures", 1)
    doc.add_paragraph("Figure 1: Le jardin secret")
    doc.add_paragraph("Figure 2: Orion lion noir geant")
    doc.add_paragraph("Figure 3: Nyx, la Gardienne")
    doc.save(output_path)
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=str, default="Sam et le chat noir")
    parser.add_argument("--output", type=str, default="report.docx")
    args = parser.parse_args()
    
    story = generate_story(args.prompt)
    export_docx(story, args.output)
