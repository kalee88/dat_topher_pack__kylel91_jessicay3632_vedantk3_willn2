from flask import Flask             
from flask import render_template  
from flask import request          

from flask import session

import os

app = Flask(__name__)    
app.secret_key = os.urandom(32)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__": 
    app.debug = True 
    app.run()