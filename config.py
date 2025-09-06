import os
import torch

# Paths
INPUT_FOLDER = "data/images"
JSON_FILE_PATH = "output/database/cardmarket_price/cardmarket_price_playwright.json"
ANNOTATED_FOLDER = "output/matches"
os.makedirs(ANNOTATED_FOLDER, exist_ok=True)

# Device
USE_CUDA = torch.cuda.is_available()
DEVICE = "cuda" if USE_CUDA else "cpu"

# User agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko)",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)",
]
