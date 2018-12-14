import json
from io import StringIO

from flask import Flask, request, render_template, send_from_directory, make_response

from src.car_price_prediction.model.model_predictor import Predictor
from src.car_price_prediction.utils import dataset_manager
from app.config import Config
from app.prediction_form import PredictionForm



app = Flask(__name__)
app.config.from_object(Config)
predictor = Predictor()

@app.route('/')
def index():
	form = PredictionForm()
	return render_template('index.html', form=form)


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
    app.run(host="0.0.0.0", debug = True)
