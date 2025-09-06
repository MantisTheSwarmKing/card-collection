import asyncio
import re
from io import BytesIO
from PIL import Image
from clip_utils import clip_image_similarity
from image_utils import save_annotated_image
from database import find_entry_by_name, is_image_in_database

async def extract_op_code(page, show_debug=False):
    try:
        await page.wait_for_selector("xpath=//div[@id='text_container']/textarea", timeout=30000)
    except:
        if show_debug:
            print("[DEBUG] OP code textarea not found.")
        return None
    content = await page.eval_on_selector("xpath=//div[@id='text_container']/textarea", "el => el.value")
    match = re.search(r'OP.{6}', content)
    return match.group(0) if match else None

async def extract_card_details(page, show_debug=False):
    try:
        await page.wait_for_selector("dd.col-6.col-xl-7", timeout=15000)
        elements = await page.query_selector_all(".flex-grow-1")
        card_name_text = " ".join([await el.inner_text() for el in elements])
        dd_elements = await page.query_selector_all("dd.col-6.col-xl-7")
        info = [await el.inner_text() for el in dd_elements]
        img_element = await page.query_selector("img")
        img_url = await img_element.get_attribute("src") if img_element else ""
        return {
            "card_code": "ExtractedCodePlaceholder",
            "card_image": img_url,
            "card_name": card_name_text,
            "printed_in": info[2] if len(info) > 2 else "",
            "available_items": info[4] if len(info) > 4 else "",
            "from": info[5] if len(info) > 5 else "",
            "price_trend": info[6] if len(info) > 6 else "",
            "30_days_average_price": info[7] if len(info) > 7 else "",
            "7_days_average_price": info[8] if len(info) > 8 else "",
            "1_day_average_price": info[9] if len(info) > 9 else "",
            "card_url": page.url
        }
    except Exception as e:
        if show_debug:
            print(f"[DEBUG] extract_card_details failed: {e}")
        return {}

async def process_page_for_image(page, ref_img, image_name, json_data, save_annotated=False, show_debug=False):
    if is_image_in_database(json_data, image_name):
        if show_debug:
            print(f"[DEBUG] {image_name} already in database.")
        return

    # --- Place here your Playwright steps: navigation, uploading, extracting thumbnails ---
    # Use clip_image_similarity(ref_img, img) to compare images
    # Save annotated images via save_annotated_image()
    # Update json_data with new card info

    # For brevity, the detailed Playwright code can be refactored similarly.
    pass
