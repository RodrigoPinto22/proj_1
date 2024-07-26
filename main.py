from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
tasks = []
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form.get('task')
        print(task)
        tasks.append(task)
    return render_template("index.html")

@app.route("/task_list")
def task_list():
    print(tasks)
    return render_template("tasks.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)