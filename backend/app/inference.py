import torch
import numpy as np
import os
from app.model import CNN
from app.mc_dropout import mc_dropout_predict
from app.uncertainty import predictive_entropy, expected_entropy, mutual_information
from app.ood import is_ood
from app.calibration import compute_brier_score

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

model = CNN().to(DEVICE)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "saved_models", "model.pt")

model.load_state_dict(torch.load(model_path, map_location=DEVICE))
model.eval()

def run_inference(image, n_samples=30, true_label=None):
    image = image.to(DEVICE)

    all_probs = mc_dropout_predict(model, image, n_samples)
    mean_probs = torch.mean(all_probs, dim=0)  # (1, n_classes)

    prediction = torch.argmax(mean_probs, dim=1).item()
    confidence = torch.max(mean_probs).item()

    pe = predictive_entropy(mean_probs)
    ee = expected_entropy(all_probs)
    mi = mutual_information(all_probs)

    ood_flag = is_ood(mi)

    probs_np = mean_probs.cpu().detach().numpy()  # (1, n_classes)

    # Brier Score: use true_label if provided, else use predicted label as proxy
    label_for_brier = true_label if true_label is not None else prediction
    brier = compute_brier_score([label_for_brier], probs_np)

    # Calibration Error (always computed):
    # Variance across MC samples for the predicted class — 
    # high variance = model is uncertain = poorly calibrated for this input
    all_probs_np = all_probs.cpu().detach().numpy()  # (n_samples, 1, n_classes)
    per_sample_confidence = all_probs_np[:, 0, prediction]  # (n_samples,)
    calibration_error = float(np.std(per_sample_confidence))

    # If true label is known, override with exact |confidence - correctness|
    if true_label is not None:
        correct = int(prediction == true_label)
        calibration_error = abs(confidence - correct)

    result = {
        "prediction": prediction,
        "confidence": round(confidence, 4),
        "predictive_entropy": round(pe.item(), 4),
        "expected_entropy": round(ee.item(), 4),
        "mutual_information": round(mi.item(), 4),
        "is_ood": ood_flag,
        "brier_score": round(brier, 4),
        "calibration_error": round(calibration_error, 4),
    }

    return result