import numpy as np

def mean_squared_error(y_true, y_pred):
    """
    
    @brief Computes the mean squared error between true and predicted values.
    
    @param y_true numpy array of true values.
    @param y_pred numpy array of predicted values.
    @return Mean squared error as a float.
     
    """
    return np.mean((y_true - y_pred) ** 2)