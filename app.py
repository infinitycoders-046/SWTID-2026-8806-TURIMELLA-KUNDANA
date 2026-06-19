from flask import Flask, render_template

app = Flask(__name__)

# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- ABOUT ----------------

@app.route("/about")
def about():
    return render_template("about.html")


# ---------------- DASHBOARD 1 ----------------

@app.route("/dashboard1")
def dashboard1():
    return render_template("dashboard01.html")


# ---------------- DASHBOARD 2 ----------------

@app.route("/dashboard2")
def dashboard2():
    return render_template("dashboard02.html")


# ---------------- STORY ----------------

@app.route("/story")
def story():
    return render_template("story.html")


# ---------------- RUN APP ----------------

if __name__ == "__main__":
    app.run(debug=True)