# House Price Prediction using Linear Regression

## Overview

This project implements a Linear Regression model to predict house prices based on key housing features such as living area, number of bedrooms, and number of bathrooms. The model is built using Python and Scikit-learn as part of the Prodigy InfoTech Machine Learning Internship.

## Objective

To develop a machine learning model that can estimate house prices using historical housing data and multiple input features.

## Dataset Features

* sqft_living – Living area in square feet
* bedrooms – Number of bedrooms
* bathrooms – Number of bathrooms
* price – House price (target variable)

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn

## Project Workflow

1. Load the housing dataset.
2. Perform data preprocessing and feature selection.
3. Split the dataset into training and testing sets.
4. Train a Linear Regression model.
5. Evaluate the model using:

   * Mean Squared Error (MSE)
   * R² Score
6. Predict house prices for new user inputs.

## Model Evaluation

The model's performance is assessed using:

* Mean Squared Error (MSE)
* R² Score

These metrics help determine how accurately the model predicts house prices.

## How to Run

### Clone the Repository

```bash
git clone https://github.com/Dorjit-Nameirakpam/PRODIGY_ML_01.git
cd PRODIGY_ML_01
```

### Install Dependencies

```bash
pip install pandas numpy scikit-learn
```

### Run the Program

```bash
python PRODIGY_ML_01.py
```

## Sample Input

* Square Footage: 2000
* Bedrooms: 3
* Bathrooms: 2

## Expected Output

Predicted House Price based on the trained Linear Regression model.

## Learning Outcomes

* Understanding Linear Regression
* Data preprocessing using Pandas
* Model training and evaluation with Scikit-learn
* Feature selection and prediction
* Working with real-world datasets

## Internship Task

Task 01 – Implement a Linear Regression Model for House Price Prediction

## Author

Dorjit Nameirakpam

Machine Learning Intern – Prodigy InfoTech
