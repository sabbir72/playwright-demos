import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test_open_playwright_page():
 with sync_playwright() as p:
    playwright = p
    browser = p.chromium.launch(headless=False, timeout=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://stagev15.inctl.net/#login")

    # Login part
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("Administrator")

    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin")

    page.get_by_role("button", name="Login").click()


#    # Pre Costing part
    page.get_by_role("combobox", name="Search or type a command (").click()
    page.get_by_role("combobox", name="Search or type a command (").fill("pre costing")
    page.get_by_role("listitem").filter(has_text="Pre Costing List").click()

    page.get_by_role("button", name="Add Pre Costing").click()
    page.locator("form").filter(has_text="Finished Goods Type Begin").get_by_role("combobox").first.click()
    page.get_by_title("RMG", exact=True).click()
    
    page.locator("//div[@data-fieldname='style']//input[@role='combobox']").click()
    page.get_by_text("HUPM0060").click()

    page.locator("form").filter(has_text="Finished Goods Type").get_by_role("textbox").nth(1).click()
    page.get_by_text("19").click()
    page.locator(".ml-2 > .es-icon").first.click()
    page.locator(".ml-2 > .es-icon").first.click()


    page.locator("form").filter(has_text="fabric_items Fabric Items No").get_by_role("button").click()
    page.locator(".rows > .grid-row > .data-row > .row-index").click()
    page.locator(".form-page > div > .section-body > div > form > div:nth-child(2) > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").first.click()
    page.locator(".form-page > div > .section-body > div > form > div:nth-child(2) > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").first.fill("100")
    page.get_by_text("% BCI Cotton S/J 100% BCI Cotton S/J").click()
    page.locator("div:nth-child(14) > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").click()
    page.get_by_title("Local").click()
    page.locator(".form-page > div > .section-body > div:nth-child(2) > form > div > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").first.click()
    page.get_by_title("Black", exact=True).click()
    page.locator(".form-page > div > .section-body > div:nth-child(2) > form > div:nth-child(2) > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").click()
    page.get_by_text("GSM-130-").click()
    page.locator(".form-page > div > .section-body > div:nth-child(2) > form > div:nth-child(3) > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").click()
    page.get_by_text("DIA-00001100.0").click()
    page.locator("div:nth-child(14) > .frappe-control > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").click()
    page.get_by_text("Back", exact=True).click()
    page.get_by_text("Front", exact=True).click()
    page.locator(".form-column.col-sm-3 > form > div > .form-group > .control-input-wrapper > .control-input > .input-with-feedback").first.click()
    page.locator(".form-column.col-sm-3 > form > div > .form-group > .control-input-wrapper > .control-input > .input-with-feedback").first.fill("0.50")
    page.locator("div:nth-child(6) > .section-body > div:nth-child(2) > form > .frappe-control > .form-group > .control-input-wrapper > .control-input > .input-with-feedback").click()
    page.locator("div:nth-child(6) > .section-body > div:nth-child(2) > form > .frappe-control > .form-group > .control-input-wrapper > .control-input > .input-with-feedback").click()
    page.locator("div:nth-child(6) > .section-body > div:nth-child(2) > form > .frappe-control > .form-group > .control-input-wrapper > .control-input > .input-with-feedback").fill("5")
    page.get_by_text("ESC", exact=True).click()

    # 2nd fabric item
    page.locator("form").filter(has_text="fabric_items Fabric Items No").get_by_role("button").click()
    page.get_by_label("Production Item").get_by_text("2", exact=True).click()
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-body > .form-area > .form-layout > .form-page > div > .section-body > div > form > div:nth-child(2) > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").first.fill("1*1")
    page.get_by_role("option", name="100% cotton 1*1 rib 100%").get_by_role("paragraph").click()
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-body > .form-area > .form-layout > .form-page > div > .section-body > div > form > div:nth-child(14) > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").click()
    page.get_by_role("option", name="Local").click()
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-body > .form-area > .form-layout > .form-page > div:nth-child(5) > .section-body > div > form > div > .form-group > .control-input-wrapper > .control-input > .input-with-feedback").first.click()
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-body > .form-area > .form-layout > .form-page > div:nth-child(5) > .section-body > div > form > div > .form-group > .control-input-wrapper > .control-input > .input-with-feedback").first.fill("0.60")
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-body > .form-area > .form-layout > .form-page > div:nth-child(6) > .section-body > div:nth-child(2) > form > .frappe-control > .form-group > .control-input-wrapper > .control-input > .input-with-feedback").click()
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-body > .form-area > .form-layout > .form-page > div:nth-child(6) > .section-body > div:nth-child(2) > form > .frappe-control > .form-group > .control-input-wrapper > .control-input > .input-with-feedback").fill("6")
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-body > .form-area > .form-layout > .form-page > div > .section-body > div:nth-child(3) > form > div:nth-child(14) > .frappe-control > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").click()
    page.get_by_role("option", name="Sleeve").get_by_role("strong").click()
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-body > .form-area > .form-layout > .form-page > div > .section-body > div:nth-child(2)").first.click()
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-heading > .toolbar > .row-actions > .btn.btn-secondary.btn-sm.pull-right.grid-collapse-row").click()

    # ACCESSORIES ITEM
    page.locator("form").filter(has_text="accessories_items Accessories").get_by_role("button").click()
    page.locator("span").filter(has_text=re.compile(r"^1$")).nth(2).click()
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-body > .form-area > .form-layout > .form-page > div > .section-body > div > form > div:nth-child(2) > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").first.fill("butt")
    page.get_by_text("Accessories-0023").click()
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-body > .form-area > .form-layout > .form-page > div > .section-body > div > form > div:nth-child(14) > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").click()
    page.get_by_role("option", name="Local").get_by_role("paragraph").click()
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-body > .form-area > .form-layout > .form-page > div:nth-child(5) > .section-body > div > form > div > .form-group > .control-input-wrapper > .control-input > .input-with-feedback").first.click()
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-body > .form-area > .form-layout > .form-page > div:nth-child(5) > .section-body > div > form > div > .form-group > .control-input-wrapper > .control-input > .input-with-feedback").first.fill("1")
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-body > .form-area > .form-layout > .form-page > div:nth-child(6) > .section-body > div:nth-child(2) > form > .frappe-control > .form-group > .control-input-wrapper > .control-input > .input-with-feedback").click()
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-body > .form-area > .form-layout > .form-page > div:nth-child(6) > .section-body > div:nth-child(2) > form > .frappe-control > .form-group > .control-input-wrapper > .control-input > .input-with-feedback").fill("2")
    page.get_by_text("ESC", exact=True).nth(2).click()

    # Selecting Operations
    page.get_by_role("tab", name="Operations").click()
    page.get_by_role("tabpanel", name="Operations").get_by_role("combobox").click()
    page.get_by_title("KOHLS-OPB", exact=True).click()

    # Pre Costing Data
    page.get_by_role("tab", name="Pre Costing Data").click()
    page.locator("//input[@data-fieldname='min_ord_qty']").click()
    page.get_by_role("textbox").first.fill("50")


    page.locator("//input[@data-fieldname='payment_term']").click()
    page.get_by_text("120 Days").click()

    page.locator("//input[@data-fieldname='shipping_mode']").click()
    page.get_by_title("Sea", exact=True).click()
    page.locator("//input[@data-fieldname='delivery_terms']").click()
    page.get_by_title("FOB").click()
    page.locator("//input[@data-fieldname='sales_price']").fill("15")

    page.locator("button[data-label='Save']").click()

    page.locator('button:has-text("Production Item")').click()
    page.locator('label:has-text("Expense Detail")').scroll_into_view_if_needed()

    
    page.locator("//div[@class='data-row row editable-row']//span[contains(text(),'8')]").click()
    page.locator("//input[@data-fieldname='rate']").click()
    page.get_by_role("textbox", name="Amount").fill("300")


    page.get_by_role("button", name="Save").click()

    # ---------------------
   


