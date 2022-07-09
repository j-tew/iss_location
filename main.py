from flask import Flask, render_template
from utils import *

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "position": get_iss_position(),
        "map": get_map(),
        "country": get_country(),
        "crew": get_crew(),
    }
    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run()
