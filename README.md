# Cerebra — Multi-Agent Research Assistant

> AI agents that think, critique and synthesize — so you don't have to.

Built with LangGraph, Groq (LLaMA 3.3 70B) and Tavily Search.

---

## What is Cerebra?

Cerebra is a multi-agent AI research system where three autonomous agents collaborate to deliver comprehensive, cited, and fact-checked research reports on any topic.

## How it works

| Agent | Role |
|---|---|
| Researcher | Searches the web using Tavily and collects relevant sources |
| Critic | Analyses sources, detects gaps and triggers re-search if needed |
| Synthesizer | Merges all findings into a structured report with citations |

The agents communicate through a shared state graph built with LangGraph. If the Critic detects gaps, it automatically sends the Researcher back to search again — up to 2 iterations.

## Tech Stack

- LangGraph — agent orchestration and state graph
- Groq (LLaMA 3.3 70B) — LLM powering all three agents
- Tavily — real-time web search
- Flask — backend API
- HTML/CSS/JS — frontend UI

## Project Structure

```
cerebra-multi-agent-research/
├── agents/
│   ├── researcher.py
│   ├── critic.py
│   └── synthesizer.py
├── graph/
│   └── research_graph.py
├── tools/
│   └── search.py
├── templates/
│   └── index.html
├── app.py
├── .env
└── requirements.txt
```

## Setup

1. Clone the repo
2. Create a virtual environment
3. Install dependencies
4. Add your API keys to `.env`
5. Run the app

```bash
git clone https://github.com/yourusername/cerebra-multi-agent-research.git
cd cerebra-multi-agent-research
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:

```
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
```

Run:

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Sample Output

- Query: *What is the impact of AI in healthcare?*
- Iterations: 2 (Critic triggered one re-search)
- Sources collected: 10
- Report: Structured with headings, bullet points and citations

---

Built by Preethikgha M 