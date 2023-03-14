from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/training/<prof>')
def index(prof):
    return render_template('base.html', title='Заготовка', prof=prof)


if __name__ == '__main__':
    app.run(port=8067, host='127.0.0.1')