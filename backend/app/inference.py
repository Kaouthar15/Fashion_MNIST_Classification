import torch
from app.model import CNN
from app.mc_dropout import mc_dropout_predict
from app.uncertainty import predictive_entropy, expected_entropy, mutual_information
from app.ood import is_ood
import os
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

model = CNN().to(DEVICE)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "saved_models", "model.pt")

model.load_state_dict(torch.load(model_path, map_location=DEVICE))
model.eval()

def run_inference(image, n_samples=30):
    image = image.to(DEVICE)

    all_probs = mc_dropout_predict(model, image, n_samples)
    mean_probs = torch.mean(all_probs, dim=0)

    prediction = torch.argmax(mean_probs, dim=1).item()
    confidence = torch.max(mean_probs).item()

    pe = predictive_entropy(mean_probs)
    ee = expected_entropy(all_probs)
    mi = mutual_information(all_probs)

    ood_flag = is_ood(mi)

    return {
        "prediction": prediction,
        "confidence": confidence,
        "predictive_entropy": pe.item(),
        "expected_entropy": ee.item(),
        "mutual_information": mi.item(),
        "is_ood": ood_flag
    }