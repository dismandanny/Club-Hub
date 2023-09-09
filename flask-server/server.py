from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# Members API Route
@app.route("/")
def members():
    # return {"members": ["Member1", "Member2", "Member3"]}
    return render_template("basic.html")

if __name__ == "__main__":
    app.run(debug=True)