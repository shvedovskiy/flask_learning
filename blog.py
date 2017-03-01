import os
from flask import Flask, render_template, redirect, request, make_response, url_for
from data import get_entries, add_entry, init_with_file

app = Flask(__name__)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def home():
    return render_template(
        'index.html',
        entries=get_entries(),
        login=request.cookies.get('login', None))


@app.route("/post/<int:post_id>")
def post(post_id):
    entry = get_entries()[post_id - 1]
    return render_template(
        'post.html',
        entry=entry,
        login=request.cookies.get('login', None))


@app.route("/new_post", methods=["POST"])  # по умолчанию обработчики принимают GET
def new_post():
    """ request -- глобальный объект, хранящий информацию о текущем обрабатываемом запросе. """
    title = request.form['title']
    abstract = request.form['abstract']
    content = request.form['content']
    add_entry({
        'title': title,
        'abstract': abstract,
        'content': content
    })
    return redirect(url_for('home'))


@app.route("/signup", methods=["POST"])
def signup():
    response = make_response(redirect(url_for('home')))  # создать объект ответа
    response.set_cookie('login', request.form['login'])
    return response


if __name__ == "__main__":
    init_with_file(os.path.join(SCRIPT_DIR, 'data.txt'))
    app.run(debug=True, host='0.0.0.0', port=5000)
