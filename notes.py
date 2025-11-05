from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    note = ""
    if request.method == "POST":
        note = request.form["note"]
        with open("note.txt", "w") as f:
            f.write(note)
    try:
        with open("note.txt", "r") as f:
            note = f.read()
    except FileNotFoundError:
        pass
    return render_template("index.html", note=note)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
