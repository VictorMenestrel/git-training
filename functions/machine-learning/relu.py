import numpy as np

def relu(x):
    """
    @brief Applies the Rectified Linear Unit (ReLU) activation function.

    The ReLU function returns the input value if it is greater than 0; otherwise, it returns 0.

    @param x Input value or array.

    @return The result of applying the ReLU function element-wise to the input.
    """
    return np.maximum(0, x)