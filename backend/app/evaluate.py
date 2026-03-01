import torch
import numpy as np
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from app.model import CNN
from app.mc_dropout import mc_dropout_predict
from app.calibration import compute_brier_score, compute_ece
import os

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

def evaluate_calibration(n_samples=30, batch_size=256):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])

    test_dataset = datasets.FashionMNIST(
        root="./data",
        train=False,
        download=True,
        transform=transform
    )
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    # Load model
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
    model_path = os.path.join(BASE_DIR, "saved_models", "model.pt")

    model = CNN().to(DEVICE)
    model.load_state_dict(torch.load(model_path, map_location=DEVICE))
    model.eval()

    all_probs = []
    all_labels = []

    print("Running MC Dropout inference on test set...")
    for images, labels in test_loader:
        images = images.to(DEVICE)

        # mc_dropout_predict returns (n_samples, batch_size, n_classes)
        probs = mc_dropout_predict(model, images, n_samples)
        mean_probs = torch.mean(probs, dim=0)  # (batch_size, n_classes)

        all_probs.append(mean_probs.cpu().numpy())
        all_labels.extend(labels.numpy())

    all_probs = np.concatenate(all_probs, axis=0)   # (N, n_classes)
    all_labels = np.array(all_labels)                # (N,)

    brier = compute_brier_score(all_labels, all_probs)
    ece = compute_ece(all_labels, all_probs)

    print(f"\n Calibration Results on Fashion-MNIST Test Set")
    print(f"   Brier Score : {brier:.4f}  (lower is better, 0 = perfect)")
    print(f"   ECE         : {ece:.4f}  (lower is better, 0 = perfect)")

    return {"brier_score": brier, "ece": ece}


if __name__ == "__main__":
    evaluate_calibration()