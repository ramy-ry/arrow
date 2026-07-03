import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session,jsonify 
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")
db.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    hash TEXT
)
""")
#journey table
db.execute("""
CREATE TABLE IF NOT EXISTS journey(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    hours REAL,
    satisfaction INTEGER
)
""")

#define the apology function
def apology(message, code=400):
    return render_template("apology.html", message=message ),code


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index() :
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Register user"""
    if request.method == "POST":

        username = request.form.get("username")
        if not username:
            return apology("Must provide username !")

        password = request.form.get("password")

        if not password:
            return apology("Must provide password !")

        confirmation = request.form.get("confirmation")
        if password != confirmation:
            return apology("confirmation must match the password !")

        rows = db.execute("SELECT * FROM users WHERE username = ? ", username)

        if len(rows) != 0:
            return apology("Username already exist !")

        hash = generate_password_hash(password)

        db.execute("INSERT INTO users (username , hash) VALUES (? , ?)", username, hash)

        rows = db.execute(
                   "SELECT id FROM users WHERE username = ?",
                         username
                               )
         #vgj
        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:

        return render_template("signup.html")
    

@app.route("/jour")
def journey():
    if not session.get("user_id") :
        flash("You should log in or sign up first!")
        return redirect("/")
    tasks = db.execute(
        "SELECT * FROM tasks WHERE user_id = ?",
        session["user_id"]
    )
    return render_template("todo.html" ,tasks = tasks)


@app.route("/time")
def time():
    if not session.get("user_id") :
        flash("You should log in or sign up first!")
        return redirect("/")
    return render_template("time.html")



@app.route("/save-progress", methods=["POST"])
def save_progress():


    date = request.form.get("date")
    hours = request.form.get("hours")
    satisfaction = request.form.get("satisfaction")

    existing = db.execute(
    "SELECT * FROM journey WHERE user_id = ? AND date = ?",
    session["user_id"],
    date
    )


    if existing:

        db.execute(
            """
            UPDATE journey
            SET hours = ?, satisfaction = ?
            WHERE user_id = ? AND date = ?
            """,

            hours,
            satisfaction,
            session["user_id"],
            date
               )
        return redirect("/time")

    else:
        
        db.execute(
            """
            INSERT INTO journey
            (user_id, date, hours, satisfaction)

            VALUES (?, ?, ?, ?)
            """,

            session["user_id"],
            date,
            hours,
            satisfaction
        )

        return redirect("/time")

@app.route("/graph")
def graph():
    if not session.get("user_id") :
        flash("You should log in or sign up first!")
        return redirect("/")
    data = db.execute(
        """
        SELECT date, hours, satisfaction
        FROM journey
        WHERE user_id = ?
        ORDER BY date
        """,
        session["user_id"]
    )

    return render_template("graph.html", data=data )

@app.route("/add_task", methods=["POST"])
def add_task(): 
    if not session.get("user_id"):
        flash("You should log in or sign up first!")
        return redirect("/")


    task = request.form.get("task")

    if task:

        db.execute(
            "INSERT INTO tasks (user_id, task) VALUES (?, ?)",
            session["user_id"],
            task
        )

    return redirect("/todo")

@app.route("/delete_task/<int:id>")
def delete_task(id):
    if not session.get("user_id"):
        flash("You should log in or sign up first!")
        return redirect("/")
    db.execute("DELETE FROM tasks WHERE id = ? AND user_id = ?",
               id,
               session["user_id"]
               )
    return redirect("/todo")
@app.route("/todo")
def todo():
    if not session.get("user_id"):

        flash("You should log in or sign up first!")
        return redirect("/")
    tasks=db.execute(
        "SELECT * FROM tasks WHERE user_id = ?",
        session["user_id"]
   )
    
    return render_template(
        "todo.html",
          tasks=tasks 
    )

@app.route("/toggle_task/<int:id>")
def toggle_task(id):

    if not session.get("user_id"):
        flash("You should log in first!")
        return redirect("/")

    db.execute(
        """
        UPDATE tasks
        SET completed = NOT completed
        WHERE id = ? AND user_id = ?
        """,
        id,
        session["user_id"]
    )

    return redirect("/todo")