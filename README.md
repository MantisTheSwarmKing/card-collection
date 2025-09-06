Project Structure
project/
│
├─ main.py                 # Entry point
├─ config.py               # Paths, device, user-agent configuration
├─ clip_utils.py           # CLIP model loading and image similarity functions
├─ playwright_utils.py     # Playwright scraping and image processing
├─ database.py             # JSON database read/write utilities
├─ image_utils.py          # Image helpers and preprocessing
├─ data/images/            # Input images
├─ output/                 # Annotated images and database
└─ requirements.txt        # Python dependencies

Installation
git clone https://github.com/yourusername/card-image-scraper.git
cd card-image-scraper
Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Install dependencies
pip install -r requirements.txt
Install Playwright browsers
playwright install
Place your card images in data/images/.
Run the main script:
python main.py
During runtime, you will be prompted to
Save annotated images (y/n)

Show debug logs (y/n)

Extracted card details are stored in output/database/cardmarket_price/cardmarket_price_playwright.json.

Annotated images are saved in output/matches/ (if enabled).

Configuration
config.py to adjust:

Input/output paths

Device selection (GPU/CPU)

User agents for Playwright
USE_CUDA = torch.cuda.is_available()
DEVICE = "cuda" if USE_CUDA else "cpu"
INPUT_FOLDER = "data/images"
ANNOTATED_FOLDER = "output/matches"
JSON_FILE_PATH = "output/database/cardmarket_price/cardmarket_price_playwright.json"

Dependencies

Python 3.9+

PyTorch

CLIP

Playwright

Pillow (PIL)

NumPy

