import os
import asyncio
from playwright.async_api import async_playwright
from config import INPUT_FOLDER, USER_AGENTS
from database import load_database, save_database
from image_utils import load_image
from playwright_utils import process_page_for_image

async def process_image(image_path, browser, json_data, save_annotated, show_debug):
    ref_img = load_image(image_path)
    context = await browser.new_context()
    page = await context.new_page()
    try:
        await process_page_for_image(page, ref_img, os.path.basename(image_path), json_data, save_annotated, show_debug)
    finally:
        await page.close()
        await context.close()

async def main():
    save_annotated = input("Save annotated images? (y/n): ").strip().lower() == "y"
    show_debug = input("Show debug? (y/n): ").strip().lower() == "y"

    image_files = [os.path.join(INPUT_FOLDER, f) for f in os.listdir(INPUT_FOLDER)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not image_files:
        print("No images found.")
        return

    json_data = load_database()

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        semaphore = asyncio.Semaphore(3)

        async def sem_process(image_path):
            async with semaphore:
                await process_image(image_path, browser, json_data, save_annotated, show_debug)

        await asyncio.gather(*(sem_process(img_path) for img_path in image_files))
        await browser.close()

    save_database(json_data)

if __name__ == "__main__":
    asyncio.run(main())
