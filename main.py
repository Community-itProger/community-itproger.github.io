from flask import Flask, render_template, url_for

app = Flask(import_name=__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template(template_name_or_list="index.html")


@app.route("/about")
def about():
    return render_template(template_name_or_list="about.html")


@app.route("/user/id/<int:user_id>")
def user(user_id):
    return str(user_id)


@app.route("/admin")
def admin():
    return render_template(template_name_or_list="admin_panel.html")


if __name__ == "__main__":
    app.run(debug=True)
