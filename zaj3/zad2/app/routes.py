from datetime import datetime

from flask import render_template, request, redirect, url_for, jsonify
from app import app, db
from app.models import Task


@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.json
    content = data.get('content')
    if content:
        new_task = Task(content=content)
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task added successfully'}), 200
    else:
        return jsonify({'error': 'Content is required'}), 400


@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully'}), 200
    else:
        return jsonify({'error': 'Task not found'}), 404