from playwright.sync_api import sync_playwright
import os


def render_pdf():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{os.path.abspath("report.html")}")
        page.emulate_media(media="screen")
        page.pdf(path="report-py.pdf")
        browser.close()


print(f"module name: {__name__}")
