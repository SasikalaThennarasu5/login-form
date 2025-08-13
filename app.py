from flask import Flask, render_template, flash, redirect, url_for
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Dummy credentials
DUMMY_EMAIL = "test@example.com"
DUMMY_PASSWORD = "password123"

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if email == DUMMY_EMAIL and password == DUMMY_PASSWORD:
            flash("Login successful", "success")
            return redirect(url_for('login'))
        else:
            flash("Invalid credentials", "danger")
    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
