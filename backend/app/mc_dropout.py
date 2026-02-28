import torch

def mc_dropout_predict(model, x, n_samples=30):
    model.train()  # keep dropout active

    predictions = []

    for _ in range(n_samples):
        output = torch.softmax(model(x), dim=1)
        predictions.append(output.unsqueeze(0))

    return torch.cat(predictions, dim=0)