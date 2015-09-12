from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recipe/<uuid>')
def recipe(uuid):
    return render_template('recipe.html', recipe_id=uuid)


@app.route('/recipes/')
def recipes():
    return 'This is the recipes page'


if __name__ == '__main__':
    app.run(debug=True)
