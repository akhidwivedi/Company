import requests
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template,request
import json
from datetime import datetime



app =Flask(__name__)
app.config['DEBUG']=True


@app.route('/',methods=['GET','POST'])
def index():
    # url = 'https://assignment-machstatz.herokuapp.com/excel?date=2020-05-22T01:00:00Z'
    url = 'https://assignment-machstatz.herokuapp.com/excel'
    r = requests.get(url)
    print("**********")
    # print(r.json())
   

    print("##############")
    # data = json.loads(url)
    # print(data)
    # data ={
    #     "totalWeight": ,
    #     "totalLength": ,
    #     "totalQuantity": ,
    # }
    return render_template('data.html', data = r.json())