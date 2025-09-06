from PIL import Image
import os
from config import ANNOTATED_FOLDER

def load_image(path: str):
    return Image.open(path).convert("RGB")

def save_annotated_image(img, image_name, idx, sim):
    filename = f"{image_name.replace('.', '_')}_thumb_{idx}_sim_{sim:.3f}.png"
    path = os.path.join(ANNOTATED_FOLDER, filename)
    img.save(path)
