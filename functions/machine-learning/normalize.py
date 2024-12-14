import numpy as np

def normalize(data):
    """
    @brief Normalizes the input data to a range between 0 and 1.
    
    @param data The input data to be normalized. It should be a numpy array or a similar iterable.
    
    @return The normalized data, with values scaled to the range [0, 1].
    """
    return (data - np.min(data)) / (np.max(data) - np.min(data))