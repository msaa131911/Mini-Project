#Built ML pipeline using feature selection (OMP) and Kernel Ridge Regression for regression task
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import OrthogonalMatchingPursuit
from sklearn.kernel_ridge import KernelRidge
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv(r"C:\Users\MS AA\Downloads\train (1).csv")

#  only numeric
df = df.select_dtypes(include=['int64', 'float64'])
df = df.dropna()



X = df.drop("SalePrice", axis=1)
y = df["SalePrice"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


omp = OrthogonalMatchingPursuit(n_nonzero_coefs=10)
omp.fit(X_train_scaled, y_train)

coef = pd.Series(omp.coef_, index=X.columns)
selected_features = coef[coef != 0].index

#print("\nSelected Features:\n", selected_features)

# index mapping
feature_idx = [X.columns.get_loc(col) for col in selected_features]

# reduce dataset
X_train_sel = X_train_scaled[:, feature_idx]
X_test_sel = X_test_scaled[:, feature_idx]


model = KernelRidge(alpha=1.0, kernel='rbf', gamma=0.1)
model.fit(X_train_sel, y_train)


y_pred = model.predict(X_test_sel)


rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)


print("RMSE:", rmse)
print("R2 Score:", r2)
