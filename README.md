Second-Hand Car Price Prediction

This project is a machine learning web application that predicts the selling price of a used car based on vehicle details such as registration year, present price, kilometers driven, fuel type, seller type, transmission type, and number of previous owners.

The prediction model is built using Random Forest regression from scikit-learn. The trained model learns patterns from historical car sales data and estimates the expected resale value of a car.

📊 Dataset

The dataset contains 301 car records with the following features:

Car_Name – model name of the car

Year – registration year

Selling_Price – current second-hand price (target variable)

Present_Price – original showroom price of the car

Kms_Driven – total kilometers driven

Fuel_Type – Petrol / Diesel / CNG

Seller_Type – Dealer or Individual

Transmission – Manual or Automatic

Owner – number of previous owners

During preprocessing, the car age feature is created from the registration year, and categorical variables are converted into numerical form using encoding techniques.

⚙️ Machine Learning Workflow

Load and explore the dataset

Clean and preprocess data

Feature engineering (calculate car age)

Convert categorical features using encoding

Split dataset into training and testing sets

Train a Random Forest regression model

Evaluate model performance using the R² score

The model typically achieves an R² score around 0.90–0.95, indicating good prediction accuracy.

🌐 Web Application

A simple Flask-based web interface allows users to enter car details such as:

Registration year

Present car price

Kilometers driven

Fuel type

Seller type

Transmission type

Number of owners

The application processes this input and predicts the estimated second-hand selling price of the car.

🛠️ Technologies Used

Python

Flask

Pandas

NumPy

Scikit-learn

HTML / CSS

This project demonstrates how machine learning can be applied to estimate vehicle resale prices based on real-world car attributes.

read me file

Here is a clean README.md file (under ~350 words) you can directly place in your GitHub repository.

🚗 Second-Hand Car Price Prediction

This project is a machine learning web application that predicts the selling price of a used car based on various vehicle features. The system analyzes historical car data and estimates the expected resale value of a vehicle.

The prediction model is built using Random Forest regression from scikit-learn, and the model is integrated into a simple Flask web interface for user interaction.

📊 Dataset

The dataset contains 301 car records with the following features:

Car_Name – Model name of the car

Year – Registration year

Selling_Price – Current second-hand price (target variable)

Present_Price – Original showroom price

Kms_Driven – Total kilometers driven

Fuel_Type – Petrol / Diesel / CNG

Seller_Type – Dealer or Individual

Transmission – Manual or Automatic

Owner – Number of previous owners

During preprocessing, car age is calculated from the registration year, and categorical variables are converted to numerical values using encoding.

⚙️ Machine Learning Workflow

Load and explore the dataset

Data preprocessing and cleaning

Feature engineering (calculate car age)

Encode categorical variables

Split data into training and testing sets

Train the Random Forest regression model

Evaluate model performance

The model achieves an R² score of approximately 0.90–0.95, indicating strong prediction accuracy.

🌐 Web Application

A Flask-based web interface allows users to enter car details such as:

Registration year

Present price of the car

Kilometers driven

Fuel type

Seller type

Transmission

Number of owners

The system then predicts the estimated second-hand selling price of the car.

🛠 Technologies Used

Python

Flask

Pandas

NumPy

Scikit-learn

HTML / CSS

🚀 How to Run
pip install flask pandas scikit-learn numpy
python app.py

Open in browser:

http://127.0.0.1:5000
