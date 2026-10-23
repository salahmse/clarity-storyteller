# Clarity Storyteller - Meta Global AI Developer Hackathon 2026

**Track:** Indie Dev | **Theme:** Build for Your World
**Author:** Salah Eddine Moursli - Casablanca, Morocco

An AI-powered illustrated storytelling platform that transforms a simple prompt into a structured 3000-word story with 2-3 auto-generated figures.

Built for low-connectivity regions with local-first fallback.

## Demo Story: Sam et Orion
5-chapter fantasy story created entirely with Meta AI, included in `story.md` and `Sam_et_Orion_Version_Perfectionnee.docx` with 3 figures in `/figures`.

## Tech Stack - Use of Meta AI Tooling (25% of judging)
- **Muse Spark**: story structure & coherence checking via Meta Model API
- **Meta Image**: figure generation for illustrations
- **SAM 3.1**: scene segmentation for figure placement
- **Muse**: agentic coding for pipeline
- **Local Fallback**: Ollama `llama3.1:8b`, `mistral`, `nomic-embed-text` for offline mode (key for Morocco)

## Architecture
```
prompt -> Llama Spark (outline) -> chapter generation -> coherence check -> Meta Image (figures) -> SAM 3.1 (crop) -> DOCX export
```

## Installation
```bash
pip install -r requirements.txt
ollama pull llama3.1:8b
ollama pull nomic-embed-text
```

## Usage
```bash
python inference.py --prompt "boy and black cat guardian" --output report.docx
```

## Judging Criteria Fit
- **Impact 30%**: Education & creativity tool for students, works offline
- **Use of Meta Tooling 25%**: 4 models from hackathon stack
- **Demo 25%**: Full story + figures ready
- **Technical Depth 20%**: RAG, local embeddings, DOCX pipeline

## Links
- Demo Repo: https://github.com/salahmse/clarity-storyteller
- Hackathon: https://cerebralvalley.ai/e/meta-ai-developer-hackathon

## License
MIT - Built for Meta Global AI Developer Hackathon 2026
