import torch

def predictive_entropy(mean_probs):
    return -torch.sum(mean_probs * torch.log(mean_probs + 1e-8), dim=1)

def expected_entropy(all_probs):
    entropies = -torch.sum(all_probs * torch.log(all_probs + 1e-8), dim=2)
    return torch.mean(entropies, dim=0)

def mutual_information(all_probs):
    mean_probs = torch.mean(all_probs, dim=0)
    return predictive_entropy(mean_probs) - expected_entropy(all_probs)