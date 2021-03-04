from flask import Flask, request
import pandas as pd
import joblib
import json
import pipeline
from pipeline import *

app = Flask(__name__)
pipe = joblib.load("train_pipe.joblib")

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        dat = pd.read_json(request.form["input"])
        return json.dumps(pipe.predict(dat).tolist())
    else:
        print("Remember to use the POST method for this server")

if __name__ == "__main__":
    app.run()
