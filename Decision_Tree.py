import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from IngestionTransformation import create_overall_data_dictionary, check_for_nan_in_ready_data

data = create_overall_data_dictionary()
print("All Finished")

# Convert to DataFrame
columns = ['number', 'CustomerID', 'Age', 'Gender', 'LoyaltyMember', 'ProductType', 'Rating', 'PaymentMethod',
           'TotalPrice', 'Quantity', 'AddOnTotal']
df = pd.DataFrame(data, columns=columns)

# If 'color_code' is a categorical variable encoded as integers, one-hot encode it
categorical_columns = ['ProductType']
df = pd.get_dummies(df, columns=categorical_columns, prefix=categorical_columns)

# Convert boolean dummies to integers
for col in df.columns:
    if col.startswith('ProductType_'):
        df[col] = df[col].astype(int)
print("Stop Point To View the Data")

# Specify target and features manually
# You can change these to select different target and feature columns
target_column = 'TotalPrice' #משתנה המטרה
feature_columns = ['AddOnTotal', 'Gender', 'LoyaltyMember', 'Quantity', 'Rating', 'ProductType_1', 'ProductType_2', 'ProductType_3', 'ProductType_4', 'ProductType_5']

# Split dataset
X = df[feature_columns]
y = df[target_column]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Hyperparameter grid
# criterion: The function to measure the quality of a split. 'squared_error' is the default for regression.
# max_depth: The maximum depth of the tree. None means nodes are expanded until all leaves are pure.
# min_samples_split: The minimum number of samples required to split an internal node.
# min_samples_leaf: The minimum number of samples required to be at a leaf node.
param_grid = {
    'criterion': ['squared_error'],
    'max_depth': [4, 8, 14, 20],
    'min_samples_split': [10, 20],
    'min_samples_leaf': [5]
}

# Model and Grid Search
regressor = DecisionTreeRegressor(random_state=42)
grid_search = GridSearchCV(estimator=regressor, param_grid=param_grid, cv=2, scoring='r2')
grid_search.fit(X_train, y_train)

# Best model
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Output
print("Best Parameters:", grid_search.best_params_)
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)

# Regular plot of the decision tree
plt.figure(figsize=(15, 10), dpi=150)
tree.plot_tree(best_model, filled=True, feature_names=X.columns, fontsize=6)
plt.title("Decision Tree Regressor", fontsize=12)
plt.tight_layout()
plt.show()