from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/tasks", methods=["GET", "POST"])
def task_manager():
    if request.method == "POST":
        task = request.form["task"]
        tasks.append(task)

    return render_template("tasks.html", tasks=tasks)


if __name__ == "__main__":
    app.run(debug=True)