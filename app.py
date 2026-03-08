from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("car_price_model.pkl","rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    Present_Price = float(request.form['Present_Price'])
    Kms_Driven = int(request.form['Kms_Driven'])
    Owner = int(request.form['Owner'])
    Year = int(request.form['Year'])
    Car_Age = 2024 - Year

    Fuel_Type = request.form['Fuel_Type']
    Seller_Type = request.form['Seller_Type']
    Transmission = request.form['Transmission']

    Fuel_Type_Diesel = 1 if Fuel_Type=="Diesel" else 0
    Fuel_Type_Petrol = 1 if Fuel_Type=="Petrol" else 0

    Seller_Type_Individual = 1 if Seller_Type=="Individual" else 0
    Transmission_Manual = 1 if Transmission=="Manual" else 0

    input_data = [[Present_Price,Kms_Driven,Owner,Car_Age,
                   Fuel_Type_Diesel,Fuel_Type_Petrol,
                   Seller_Type_Individual,Transmission_Manual]]

    prediction = model.predict(input_data)

    return render_template('index.html',
            prediction_text="Estimated Selling Price: ₹ {:.2f} Lakh".format(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True)