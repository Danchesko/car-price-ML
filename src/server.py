import json
from flask import Flask, request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/api/prediction',methods = ['POST'])
def prediction():
    if request.method == 'POST':
        print('hello',json.loads(request.data)['year'])
        return '40'
    
if __name__ == '__main__':
    app.run(debug=True)
