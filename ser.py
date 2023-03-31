import pandas as pd
from flask import Flask,render_template,request
import numpy as np
from sklearn.tree import DecisionTreeRegressor

bodyfat=pd.read_csv('bodyfat.csv')
model=DecisionTreeRegressor()
X=bodyfat.drop(columns=['BodyFat','Density'],axis=1)
y=bodyfat['BodyFat']
model.fit(X.values,y.values)


app=Flask(__name__)

@app.route('/')

def first():
    return render_template('index.html')

@app.route('/bodyfat',methods=['POST'])

def second():
    Age = float(request.form['Age'])
    Weight = float(request.form['Weight'])
    Height = float(request.form['Height'])
    Neckcir = float(request.form['Neckcir'])
    Chestcir = float(request.form['Chest'])
    Abdomencir = float(request.form['Abdomen'])
    Hipcir = float(request.form['Hip'])
    Thighcir = float(request.form['Thigh'])
    Kneecir = float(request.form['Knee'])
    Anklecir = float(request.form['Ankle'])
    Bicepscir = float(request.form['Biceps'])
    Forearmcir= float(request.form['Forearm'])
    Wristcir = float(request.form['Wrist'])
    Values = [[Age, Weight, Height, Neckcir, Chestcir, Abdomencir, Hipcir, Thighcir, Kneecir, Anklecir, Bicepscir, Forearmcir, Wristcir]]
    percentage=model.predict(Values)[0]
    return str(round(percentage, 2))

if __name__=="__main__":
    app.run(debug=True)










