import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("sample.csv")  # Replace with your file name

print("Dataset Preview:")
print(df.head())

X = df[['sqft_living', 'bedrooms', 'bathrooms']]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nModel Performance:")
print("MSE:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

sqft = float(input("\nEnter Square Footage: "))
bedrooms = int(input("Enter Bedrooms: "))
bathrooms = float(input("Enter Bathrooms: "))

new_house = [[sqft, bedrooms, bathrooms]]
predicted_price = model.predict(new_house)

print(f"\nPredicted House Price: ${predicted_price[0]:,.2f}")