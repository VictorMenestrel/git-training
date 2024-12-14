import numpy as np

def sigmoid(x):
    """
    @brief Computes the sigmoid function.
    
    The sigmoid function is defined as 1 / (1 + exp(-x)).
    
    @param x Input value or array.
    @return The sigmoid of the input.
    """
    return 1 / (1 + np.exp(-x))