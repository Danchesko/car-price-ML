import json
from flask import Flask, request,render_template
import index 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/api/prediction',methods = ['POST'])
def prediction():
    if request.method == 'POST':
        
        data_for_prediction = json.loads(request.data)
        data_for_prediction = {
        "year": 2010,
        "transmission":'автомат',
        "brand":'toyota',
        "urgency":'срочно',
        "capacity":4.0,
        "drive":'передний',
        "mileage":125000,
        "wheel":'левый',
        "carcass":'седан',
        "fuel":'бензин',
        "color":'белый'}
        print('hello',data_for_prediction)
        return index.get_prediction(data_for_prediction)
    
if __name__ == '__main__':
    app.run(debug=True)
