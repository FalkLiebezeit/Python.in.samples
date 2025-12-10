from flask import Flask, jsonify, request

app = Flask(__name__)

# Beispiel-Daten (normalerweise kämen die aus einer Datenbank)
todos = [
    {"id": 1, "task": "Einkaufen", "done": False},
    {"id": 2, "task": "Python lernen", "done": True}
]

# GET: Home-Seite mit API-Dokumentation
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Todo REST API",
        "endpoints": {
            "GET /todos": "Alle Todos abrufen",
            "GET /todos/<id>": "Einzelnes Todo abrufen",
            "POST /todos": "Neues Todo hinzufügen (JSON: {\"task\": \"...\", \"done\": false})",
            "PUT /todos/<id>": "Todo aktualisieren",
            "DELETE /todos/<id>": "Todo löschen"
        }
    })

# GET: Alle Todos abrufen
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

# GET: Einzelnes Todo abrufen
@app.route("/todos/<int:todo_id>", methods=["GET"])

def get_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    return jsonify(todo) if todo else ("Not Found", 404)

# POST: Neues Todo hinzufügen
@app.route("/todos", methods=["POST"])
def add_todo():
    new_todo = request.json
    new_todo["id"] = len(todos) + 1
    todos.append(new_todo)
    return jsonify(new_todo), 201

# PUT: Todo aktualisieren
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if not todo:
        return ("Not Found", 404)
    data = request.json
    todo.update(data)
    return jsonify(todo)

# DELETE: Todo löschen
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return ("Deleted", 204)

if __name__ == "__main__":
    app.run(debug=True)