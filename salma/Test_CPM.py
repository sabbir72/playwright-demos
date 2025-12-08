import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    # Navigate to the login page
    page.goto("https://stage-salma.altersense.net/")

    # Fill in login credentials
    page.get_by_role("textbox", name="Email").fill("Administrator")
    page.get_by_role("textbox", name="Password").fill("admin")
    page.get_by_role("button", name="Login").click()

    # Wait for the search combobox to be visible
    page.get_by_role("combobox", name="Search or type a command (").click()
    page.get_by_role("combobox", name="Search or type a command (").fill("Operation wise")
    page.get_by_role("link", name="Operation Wise CPM Setup List").click()
    page.goto("https://stage-salma.altersense.net/app/operation-wise-cpm-setup")
    page.get_by_role("button", name="Add Operation Wise CPM Setup").click()
    
    
    Company= page.locator(".input-with-feedback.form-control.bold[maxlength='140'][data-fieldtype='Link'][data-fieldname='company']")
    Company.click()
    Company.clear()
    Company.fill("Dabiruddin Spinning Mills Ltd.")

    Month = page.locator('.input-with-feedback.form-control.ellipsis')
    Month.click()
    Month_select = page.select_option('select[data-fieldname="month"]', "March")
    


    date_field = page.locator('input[data-fieldname="from_date"]')
    date_field.click()
    page.get_by_text("December,").first.click()
    page.get_by_text("Jan", exact=True).click()
    page.get_by_text("1", exact=True).first.click()

    
    date_field = page.locator('input[data-fieldname="to_date"]')
    date_field.click()
    page.get_by_text("December,").first.click()
    page.get_by_text("Dec").nth(2).click()
    page.get_by_text("31").nth(2).click()
    
    # Operation Name = machine type same hole machine count no fatch hobe.
    Op_name =page.locator("//div[@data-fieldname='operation']//input[@role='combobox']")
    Op_name.click()
    Op_name.fill("Carding")

    holyday = page.locator("//div[@data-fieldname='default_holiday_list']//input[@role='combobox']")
    holyday.click()
    holyday.type("Holiday List 2025 Friday")

    #  machine theke fatch hobe
    OverHeadCost = page.locator("//input[@data-fieldname='total_overhead_cost']")
    OverHeadCost.click()
    OverHeadCost.fill("15")

    
    WorkHours = page.locator("//input[@data-fieldname='working_hours_day']")
    WorkHours.click()
    WorkHours.fill("8")

     
    Total_monthCost = page.locator("//input[@data-fieldname='total_monthly_cost']")
    Total_monthCost.click()
    Total_monthCost.fill("15000")
    
    page.wait_for_timeout(2000)
    FirstSave=page.get_by_role("button", name="Save")
    FirstSave.click()
    # avg_efficiency = wORKSTATION THEKE FATCH HOBE
    print("Saved Successfully")
   
     

    