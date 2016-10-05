from flask import Blueprint, request, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
  return render_template("home/index.html")
