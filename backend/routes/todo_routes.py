from flask import Blueprint, jsonify, request
from models.todo_model import TodoModel

todo_bp = Blueprint("todo", __name__)

@todo_bp.route("/todos", methods=["GET"])
def get_todos():
    todos = TodoModel.get_all()
    return jsonify(todos), 200

@todo_bp.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()

    title = data.get("title")
    priority = data.get("priority")
    due_date = data.get("due_date")

    if not title or not priority or not due_date:
        return jsonify({"message": "Field tidak boleh kosong"}), 400

    TodoModel.create(title, priority, due_date)
    return jsonify({"message": "Todo berhasil ditambahkan"}), 201

@todo_bp.route("/todos/<int:todo_id>/status", methods=["PATCH"])
def update_status(todo_id):
    data = request.get_json()
    is_completed = data.get("is_completed")

    if is_completed not in [0, 1]:
        return jsonify({"message": "Status tidak valid"}), 400

    TodoModel.update_status(todo_id, is_completed)
    return jsonify({"message": "Status todo berhasil diupdate"}), 200

@todo_bp.route("/todos/<int:todo_id>", methods=["PATCH"])
def update_todo(todo_id):
    data = request.get_json()

    title = data.get("title")
    priority = data.get("priority")
    due_date = data.get("due_date")

    if not title or not priority or not due_date:
        return jsonify({"message": "Data tidak lengkap"}), 400

    TodoModel.update(todo_id, title, priority, due_date)
    return jsonify({"message": "Todo berhasil diupdate"}), 200

@todo_bp.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    TodoModel.delete(todo_id)
    return jsonify({"message": "Todo berhasil dihapus"}), 200
