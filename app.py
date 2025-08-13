from flask import Flask, render_template, redirect, url_for
from forms import LoginForm, RegisterForm, ForgotPasswordForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'  # Change this in production

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Here you would check credentials
        return redirect(url_for("home"))
    return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Save user to database
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        # Send password reset email
        return redirect(url_for("login"))
    return render_template("forgot_password.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
