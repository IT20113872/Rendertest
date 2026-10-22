from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    name = ""
    greeting = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            greeting = f"Hello, {name}! Welcome to Flask."

    return render_template("index.html", name=name, greeting=greeting)


if __name__ == "__main__":
    app.run(debug=True)