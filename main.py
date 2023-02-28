from flask import Flask, render_template

app = Flask(__name__)

menu = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]


@app.route('/')
def index():
    return render_template('index.html', menu=menu)


@app.route('/about/<title>')
def about(title):
    return render_template('about.html', title=title, menu=menu)


if __name__ == '__main__':
    app.run(debug=True, port=7500)
