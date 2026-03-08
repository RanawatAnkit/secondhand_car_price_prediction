# 🚗 Second-Hand Car Price Prediction

This project is a **Machine Learning web application** that predicts the **selling price of a used car** based on various vehicle attributes such as registration year, present price, kilometers driven, fuel type, seller type, transmission, and number of previous owners.

The model is trained using **Random Forest Regression** from the Scikit-learn library and deployed using a simple **Flask web application** where users can input car details and receive an estimated resale price.

---

## 📊 Dataset

The dataset contains **301 car records** with the following features:

- Car_Name – Model name of the car  
- Year – Registration year  
- Selling_Price – Current second-hand price *(target variable)*  
- Present_Price – Original showroom price of the car  
- Kms_Driven – Total kilometers driven  
- Fuel_Type – Petrol / Diesel / CNG  
- Seller_Type – Dealer or Individual  
- Transmission – Manual or Automatic  
- Owner – Number of previous owners  

During preprocessing, the **car age** is calculated from the registration year, and categorical features are converted into numerical values using encoding.

link : https://www.kaggle.com/datasets/bhavikjikadara/car-price-prediction-dataset
---

## ⚙️ Machine Learning Workflow

1. Load and explore the dataset  
2. Data preprocessing and cleaning  
3. Feature engineering (calculate car age)  
4. Encode categorical variables  
5. Split data into training and testing sets  
6. Train the Random Forest regression model  
7. Evaluate model performance

The model achieves an **R² score of approximately 0.90–0.95**, indicating good prediction accuracy.

---

## 🌐 Web Application

A simple Flask-based web interface allows users to input:

- Registration year
- Present price of the car
- Kilometers driven
- Fuel type
- Seller type
- Transmission
- Number of owners

The system then predicts the **estimated second-hand selling price**.

---

## 🛠 Technologies Used

- Python  
- Flask  
- Pandas  
- NumPy  
- Scikit-learn  
- HTML / CSS  

##How to Run the Project
1) git clone 
2) cd car-price-prediction
3) pip install flask pandas numpy scikit-learn
4) python app.py
