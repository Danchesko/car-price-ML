import json
from flask import Flask, request, render_template, send_from_directory
from index import get_prediction

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/js/<path:path>')
def serve_js(path):
    return send_from_directory('static', path)


tester = None


@app.route('/api/prediction', methods=['POST'])
def prediction():
    if request.method == 'POST':
        data_for_prediction = json.loads(request.data)
        response = str(get_prediction(data_for_prediction))
        return response


if __name__ == '__main__':
    app.run(host="0.0.0.0")
