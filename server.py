from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    """Static Homepage."""

    return render_template("index.html")


@app.route("/aboutme.json")
def get_profile():
    """Get about me profile."""

    return jsonify()


@app.route("/projects.json")
def get_projects():
    """Get project info."""

    return jsonify()


@app.route("/connect")
def get_contacts():
    """Get contact info."""

    return jsonify()


app.run(debug=True)
