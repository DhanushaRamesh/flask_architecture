import imp
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/') 
@app.route('/home') 
def home():
    print("---- Inside my Home page ------")
    return render_template('index.html')

@app.route('/next')
def nextpage():
    print("---- Next page ----")
    return render_template('next.html')

if __name__ == '__main__' :
    app.run(debug=True)
