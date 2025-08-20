from playwright.sync_api import sync_playwright
import time

def verify_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:9090/login")
        time.sleep(5)
        print(page.content())
        page.fill("input[name='matricule']", "admin")
        page.fill("input[name='password']", "oncf123")
        page.click("button[type='submit']")
        page.wait_for_url("http://localhost:9090/dashboard")
        page.screenshot(path="jules-scratch/verification/dashboard.png")
        browser.close()

if __name__ == "__main__":
    verify_login()
