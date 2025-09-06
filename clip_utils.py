from PIL import Image
import torch
import clip
from config import DEVICE

model, preprocess = clip.load("ViT-B/32", device=DEVICE)
model.eval()

def preprocess_image_for_clip(image: Image.Image):
    """Preprocess PIL image for CLIP model"""
    return preprocess(image).unsqueeze(0).to(DEVICE)

def clip_image_similarity(img1: Image.Image, img2: Image.Image):
    """Return cosine similarity between two images using CLIP"""
    with torch.no_grad():
        emb1 = model.encode_image(preprocess_image_for_clip(img1))
        emb2 = model.encode_image(preprocess_image_for_clip(img2))
        emb1 /= emb1.norm(dim=-1, keepdim=True)
        emb2 /= emb2.norm(dim=-1, keepdim=True)
        return (emb1 @ emb2.T).item()
