import torch
from torchvision import datasets, transforms
from torchvision.utils import save_image
import os

# Create folder for outputs
os.makedirs("test_samples", exist_ok=True)

transform = transforms.ToTensor()

# Load datasets
fashion_test = datasets.FashionMNIST(
    root="./data",
    train=False,
    download=True,
    transform=transform
)

mnist_test = datasets.MNIST(
    root="./data",
    train=False,
    download=True,
    transform=transform
)

# -----------------------------
# 1️⃣ Get official T-shirt (class 0)
# -----------------------------
for img, label in fashion_test:
    if label == 0:
        tshirt = img
        save_image(tshirt, "test_samples/id_tshirt.png")
        print("Saved ID sample: id_tshirt.png")
        break

# -----------------------------
# 2️⃣ Create noisy T-shirt
# -----------------------------
noise = 0.1 * torch.randn_like(tshirt)
noisy_tshirt = (tshirt + noise).clamp(0, 1)

save_image(noisy_tshirt, "test_samples/noisy_tshirt.png")
print("Saved Noisy sample: noisy_tshirt.png")

# -----------------------------
# 3️⃣ Get MNIST digit 5 (OOD)
# -----------------------------
for img, label in mnist_test:
    if label == 5:
        digit5 = img
        save_image(digit5, "test_samples/ood_digit5.png")
        print("Saved OOD sample: ood_digit5.png")
        break

print("\nAll test images generated successfully.")