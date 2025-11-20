from playwright.sync_api import sync_playwright
from spellchecker import SpellChecker  # স্পেলচেক লাইব্রেরি

def test_spelling():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demoqa.com")  # আপনার URL
        
        site_text = page.inner_text("body")  # body-এর সব টেক্সট
        
        spell = SpellChecker(language='en')  # বাংলার জন্য আলাদা আলগোরিদম প্রয়োজন
        words = site_text.split()
        wrong = spell.unknown(words)
        
        assert len(wrong) == 0, f"ভুল বানান আছে: {wrong}"
        
        context.close()
        browser.close()
