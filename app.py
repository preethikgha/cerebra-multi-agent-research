from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from graph.research_graph import create_graph

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/research", methods=["POST"])
def research():
    data = request.json
    query = data.get("query", "")

    graph = create_graph()
    initial_state = {
        "query": query,
        "search_results": [],
        "critique": "",
        "gaps": [],
        "needs_reresearch": False,
        "final_report": "",
        "iteration": 0
    }
    result = graph.invoke(initial_state)

    return jsonify({
        "report": result["final_report"],
        "critique": result["critique"],
        "sources": result["search_results"],
        "iterations": result["iteration"]
    })

if __name__ == "__main__":
    app.run(debug=True)