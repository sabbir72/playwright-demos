import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    # Navigate to the login page
    page.goto("https://salma-qc.altersense.net/")

    # Fill in login credentials
    page.get_by_role("textbox", name="Email").fill("Administrator")
    page.get_by_role("textbox", name="Password").fill("admin")
    page.get_by_role("button", name="Login").click()

    # Wait for the search combobox to be visible
    search_box = page.get_by_role("combobox", name=re.compile(r"Search or type a command", re.IGNORECASE))
    expect(search_box).to_be_visible(timeout=5000)
    search_box.click()
    search_box.fill("Requisition List")
    

    page.get_by_role("listitem").filter(has_text=re.compile(r"^Requisition List$")).click()
    page.get_by_role("button", name="Add Requisition").click()
    page.get_by_text("BSB Spinning Mills Ltd.").click()
    page.locator("form").filter(has_text="Department Begin typing for").get_by_role("combobox").click()
    page.get_by_text("Accounts - BSML").click()
    
    material_type = page.locator("input[data-fieldname='material_type'][data-doctype='Material Request']")
    material_type.click()
    material_type.fill("Electric Item")

    
    
    # page.get_by_role("combobox").filter(has_text=re.compile(r"^$")).nth(5).click()
    # page.get_by_label("Details").get_by_text("Purchase", exact=True).click()
    # page.locator(".ml-2 > .es-icon").first.click()
    # page.locator("div:nth-child(2) > div > form > div:nth-child(2) > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").first.click()
    # page.get_by_text("Cargil CottonCargill Cotton").click()
    # page.get_by_text("Currency and Exchange Rate").click()
    # page.get_by_text("Currency and Exchange Rate").click()
    # page.get_by_text("Warehouse and Location Details").click()
    # page.locator(".form-column.col-sm-20 > form > .frappe-control > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").first.click()
    # page.get_by_text("Stores - BSML").click()
    # page.get_by_role("button", name="Add Row").click()
    # page.locator(".col.grid-static-col.col-xs-5.error").click()
    # page.get_by_text("Electric Item-Electric-0002Laptop").click()
    # page.locator(".data-row.row.m-0.editable-row > .row-index").click()
    # page.locator("div:nth-child(5) > .form-group > .control-input-wrapper > .control-input > .input-with-feedback").click()
    # page.locator("div:nth-child(5) > .form-group > .control-input-wrapper > .control-input > .input-with-feedback").fill("17500")
    # page.locator(".btn.btn-secondary.btn-sm.pull-right").first.click()
    # page.get_by_role("button", name="Save").click()
