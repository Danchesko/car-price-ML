import json
from flask import Flask, request, render_template, send_from_directory, make_response
from src.app import api_service

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/js/<path:path>')
def serve_js(path):
    return send_from_directory('static', path)


@app.route('/api/v1/prediction', methods=['POST'])
def prediction():
    if request.method == 'POST':
        data_for_prediction = json.loads(request.data)
        response = str(api_service.get_prediction(data_for_prediction))
        return response


@app.route('/api/v1/cars')
def get_cars():
        data = api_service.get_cars()
        response = make_response(data.getvalue())
        response.headers['Content-Disposition'] = "attachment; filename=cars.csv"
        response.headers['Content-type'] = 'text/csv'
        return response


if __name__ == '__main__':
    app.run(host="0.0.0.0")
