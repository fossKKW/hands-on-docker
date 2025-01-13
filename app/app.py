from flask import Flask, render_template, request, redirect, url_for
from storage.database import create_task, delete_task

app = Flask(__name__)

# Store tasks in memory (for simplicity)
tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    # if task:
    #     tasks.append(task)
    if task:
        new_task = create_task(task)
        tasks.append([new_task["id"], new_task["task"]])
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id:int):
    # if 0 <= task_id < len(tasks):
    #     tasks.pop(task_id)
    deleted_task = delete_task(task_id)
    print(deleted_task)
    tasks.pop(task_id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
