from playwright.sync_api import sync_playwright

def test_open_playwright_page():
 with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    print(page.title())
    # browser.close()


# from playwright.sync_api import sync_playwright

# def test_open_playwright_page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)  # headless=False → ব্রাউজার দেখা যাবে
#         page = browser.new_page()
#         page.goto("https://playwright.dev/")
#         assert "Playwright" in page.title()  # title check
#         browser.close()

# test_example.py
def test_sum():
    assert 2 + 3 == 5
def test_sum1():
    assert 2 + 3 == 6