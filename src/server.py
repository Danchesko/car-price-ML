import json
from flask import Flask, request,render_template
from index import get_prediction

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/api/prediction',methods = ['POST'])
def prediction():
    if request.method == 'POST':
        data_for_prediction = json.loads(request.data)
        return str(get_prediction(data_for_prediction))
    
if __name__ == '__main__':
    app.run(debug=True)
