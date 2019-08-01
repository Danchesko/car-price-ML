import json
from io import StringIO
from datetime import datetime

from flask import Flask, request, render_template, send_from_directory, make_response

from src.data_model.data_cleaning.data_cleaner import get_clean_data
from src.data_model.model.model_predictor import Predictor
from src.data_model.utils import dataset_manager
from src.server.app.config import Config
from src.server.app.data_service import DataService

data = dataset_manager.get_cleaned_outliers_dataset()
data_service = DataService(data)

from src.server.app import prediction_form


app = Flask(__name__)
app.config.from_object(Config)
predictor = Predictor()


@app.route('/')
def index():
	form = prediction_form.PredictionForm()
	return render_template('index.html', form=form)
	
	
@app.route('/js/<path:path>')
def serve_js(path):
    return send_from_directory('static', path)


@app.route('/api/v1/prediction', methods=['POST', 'GET'])
def prediction():
	if request.method == 'POST':
		data_for_prediction = json.loads(request.data)
		data_for_prediction['publication'] = datetime.now().strftime('%d-%m-%Y')
		response = str(predictor.predict(data_for_prediction).pop())
		return response


@app.route('/api/v1/cars')
def get_cars():
	byte_data = StringIO()
	data.to_csv(byte_data)
	response = make_response(byte_data.getvalue())
	response.headers['Content-Disposition'] = "attachment; filename=cars.csv"
	response.headers['Content-type'] = 'text/csv'
	return response


@app.route('/api/v1/models', methods=['GET'])
def get_models():
    brand = request.args.get('brand')
    return json.dumps(data_service.get_models(brand))