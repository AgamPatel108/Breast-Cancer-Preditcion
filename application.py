from flask import Flask, request, app,render_template
from flask import Response
import pickle
import numpy as np
import pandas as pd


application = Flask(__name__)
app=application

#scaler=pickle.load(open("Model/standardScalar.pkl", "rb"))
model = pickle.load(open("Model/breastcancerlogisticregmodel.pkl", "rb"))

## Route for homepage

@app.route('/')
def index():
    return render_template('index.html')

## Route for Single data point prediction
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    result=""

    if request.method=='POST':

        Radius= float(request.form.get("mean_radius"))
        Texture = float(request.form.get("mean_texture"))
        Perimeter = float(request.form.get('mean_perimeter'))
        Area = float(request.form.get('mean_area'))
        Smoothness = float(request.form.get('mean_smoothnes'))
        

        new_data=[[Radius,Texture,Perimeter,Area,Smoothness]]
        predict=model.predict(new_data)
       
        if predict[0] ==1 :
            result = 'Cancer'
        else:
            result ='No Cancer'
            
        return render_template('single_prediction.html',result=result)

    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")