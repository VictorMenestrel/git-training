import numpy as np

def accuracy_score(y_true, y_pred):
    """
    @brief Computes the accuracy score.
    
    @param y_true Array-like of shape (n_samples,). Ground truth (correct) labels.
    @param y_pred Array-like of shape (n_samples,). Predicted labels, as returned by a classifier.
    
    @return float Accuracy score, the fraction of correct predictions.
    """
    return np.mean(y_true == y_pred)