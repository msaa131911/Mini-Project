import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import OrthogonalMatchingPursuit
from sklearn.kernel_ridge import KernelRidge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator, TransformerMixin

class OMPFeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, n_nonzero_coefs=5):
        self.n_nonzero_coefs = n_nonzero_coefs

    def fit(self, X, y):
        self.model = OrthogonalMatchingPursuit(n_nonzero_coefs=self.n_nonzero_coefs)
        self.model.fit(X, y)
        self.selected_idx = np.where(self.model.coef_ != 0)[0]
        return self

    def transform(self, X):
     X= X.to_numpy()
     return X[:, self.selected_idx]


df = pd.read_csv(r"C:\Users\MS AA\Downloads\train (1).csv")

df=df.select_dtypes(include=['int64', 'float64'])
df=df.dropna()

x=df.drop("SalePrice",axis=1)
y=df["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('feature_selection', OMPFeatureSelector(n_nonzero_coefs=10)),
    ('scaler', StandardScaler()),
    ('kernel_ridge', KernelRidge())
])

param_grid = {
    'feature_selection__n_nonzero_coefs': [5, 10, 15],
    'kernel_ridge__alpha': [0.1, 1, 10],
    'kernel_ridge__kernel': ['linear', 'rbf']
}

grid = GridSearchCV(pipeline, param_grid, cv=3)
grid.fit(X_train, y_train)

print("Best Params:", grid.best_params_)
print("R2 Score:", grid.score(X_test, y_test))

