import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("http://127.0.0.1:8000/admin/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Log in | Django site admin"))

def test_admin_login(page: Page):
    page.goto("http://127.0.0.1:8000/admin")

    # login with valid admin creds
    page.get_by_role("textbox", name="username").fill("admin")
    page.get_by_role("textbox", name="password").fill("pass")
    page.get_by_text("Log in").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Site administration")).to_be_visible()