import numpy as np
import torch

def compute_brier_score(y_true, y_prob):
    """
    y_true: list/array of integer labels (N,)
    y_prob: array of predicted probabilities (N, n_classes)
    """
    n_classes = y_prob.shape[1]
    y_true_onehot = np.zeros_like(y_prob)
    for i, label in enumerate(y_true):
        y_true_onehot[i, label] = 1.0

    brier = np.mean(np.sum((y_prob - y_true_onehot) ** 2, axis=1))
    return float(brier)


def compute_ece(y_true, y_prob, n_bins=10):
    """
    y_true: array of integer labels (N,)
    y_prob: array of predicted probabilities (N, n_classes)
    """
    confidences = np.max(y_prob, axis=1)
    predictions = np.argmax(y_prob, axis=1)
    accuracies = (predictions == np.array(y_true))

    ece = 0.0
    bin_edges = np.linspace(0, 1, n_bins + 1)

    for i in range(n_bins):
        low, high = bin_edges[i], bin_edges[i + 1]
        mask = (confidences > low) & (confidences <= high)
        if mask.sum() > 0:
            bin_acc = accuracies[mask].mean()
            bin_conf = confidences[mask].mean()
            bin_weight = mask.sum() / len(y_true)
            ece += bin_weight * abs(bin_acc - bin_conf)

    return float(ece)