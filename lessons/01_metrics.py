"""Demonstrate F1 (classification) and RMSE (regression)."""
import numpy as np
from sklearn.metrics import f1_score, mean_squared_error, mean_absolute_error, r2_score

# Classification example
y_true_class = [0, 1, 1, 0, 1, 0]
y_pred_class = [0, 1, 0, 0, 1, 1]
print("F1 score:", f1_score(y_true_class, y_pred_class))

# Regression example
y_true_reg = np.array([3.0, 5.0, 2.5, 7.0])
y_pred_reg = np.array([2.8, 5.2, 2.7, 6.5])
rmse = np.sqrt(mean_squared_error(y_true_reg, y_pred_reg))
print("RMSE:", rmse)
print("MAE:", mean_absolute_error(y_true_reg, y_pred_reg))
print("R2:", r2_score(y_true_reg, y_pred_reg))
