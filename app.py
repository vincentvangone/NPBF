from flask import Flask,render_template
from flask_assets import Environment,Bundle, assets
from webassets import bundle

app = Flask(__name__)


bundle = {
    "bootstrap.css":Bundle('css/bootstrap.css',output = 'gen/bootstrap.css'),
    "theme.css":Bundle('css/theme.css',output = 'gen/theme.css'),
}

assets = Environment(app)
assets.register(bundle)

@app.route('/')
def index():
    return render_template('main.html')


@app.route('/add')
def add():
    fat7i = [
        {"id":"1","name":"fat7i"},
        {"id":"1","name":"fathh7i"},
        {"id":"1","name":"fatgrg7i"},
        {"id":"1","name":"fat7wedi"},
        {"id":"1","name":"fatwde7i"},
        {"id":"1","name":"fatwde7wdi"},
        {"id":"1","name":"fathk7i"},
        {"id":"1","name":"fat7jji"},
    ]
    # select id,name from "types"  
    # sql(l;kds;fks).dicts()
    return render_template('add.html',types = fat7i)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)