from flask import Flask,render_template         #Import flask module and render_template 

app = Flask(__name__)                           #The variable __name__ is passed as first argument when creating an instance of the Flask object

@app.route('/')                                 # Home page contents - "/ --> represents index page"
@app.route('/home') 
def home():
    print("---- Inside my Home page ------")
    return render_template('index.html')

@app.route('/next')                            
def nextpage():
    print("---- Next page ----")
    return render_template('next.html')

#app.run(port=5000)                             #You can give any port number but it should be unique 

if __name__ == '__main__' :
    app.run(debug=True)                         #Flask starts the server listening on 127.0.0.1 and port 5000 by default
