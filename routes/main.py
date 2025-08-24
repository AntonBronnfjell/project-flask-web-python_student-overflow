from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def feed():
    # TODO: paginar preguntas y pasar al template
    return render_template("feed.html")