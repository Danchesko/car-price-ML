import json
from io import StringIO

from flask import Flask, request, render_template, send_from_directory, make_response

from src.car_price_prediction.model.model_predictor import Predictor
from src.car_price_prediction.utils import dataset_manager



app = Flask(__name__)
predictor = Predictor()

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
        response = str(predictor.predict(data_for_prediction).pop())
        return response


@app.route('/api/v1/cars')
def get_cars():
        df = dataset_manager.get_cleaned_outliers_dataset()
        byte_data = StringIO()
        df.to_csv(byte_data)
        response = make_response(byte_data.getvalue())
        response.headers['Content-Disposition'] = "attachment; filename=cars.csv"
        response.headers['Content-type'] = 'text/csv'
        return response


if __name__ == '__main__':
    app.run(host="0.0.0.0")
