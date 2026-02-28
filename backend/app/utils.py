from PIL import Image
import torch
import torchvision.transforms as transforms

transform = transforms.Compose([
    transforms.Grayscale(),
    transforms.Resize((28, 28)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

def preprocess(image_file):
    image = Image.open(image_file).convert("L")
    image = transform(image)
    return image.unsqueeze(0)