from torchvision import datasets, transforms
import matplotlib.pyplot as plt
from torchvision.utils import save_image
transform = transforms.ToTensor()

test_dataset = datasets.FashionMNIST(
    root="./data",
    train=False,
    download=True,
    transform=transform
)

# Find a T-shirt (class 0)
for img, label in test_dataset:
    if label == 0:
        plt.imshow(img.squeeze(), cmap="gray")
        plt.title("Class 0 - T-shirt")
        plt.axis("off")
        break

for img, label in test_dataset:
    if label == 0:
        save_image(img, "tshirt_official.png")
        break
