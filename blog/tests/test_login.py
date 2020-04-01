import time
from selenium.webdriver.support.ui import Select
from .pages.base_page import BasePage
from .pages.login_admin_page import LoginAdminPage

link = "http://127.0.0.1:8000/admin/login"
login = "admin"
password_text = "password"

def test_login_page(browser):
    login_page = LoginAdminPage(browser, link)
    login_page.open()
    login_page.should_be_login_form()
    login_page.fill_login_form(login, password_text)

    admin_title = browser.find_element_by_link_text("Администрирование Django")
    assert admin_title.text == "Администрирование Django"

def test_add_post(browser):
    page = BasePage(browser, link)
    page.open()
    username = browser.find_element_by_name("username")
    username.send_keys(login)
    password = browser.find_element_by_name("password")
    password.send_keys(password_text)
    submit_button = browser.find_element_by_css_selector(".submit-row > input")
    submit_button.click()
    admin_title = browser.find_element_by_link_text("Администрирование Django")
    assert admin_title.text == "Администрирование Django"

    time.sleep(1)
    add_new_post = browser.find_element_by_link_text("Добавить")
    add_new_post.click()

    title_add_new_post = browser.find_element_by_css_selector(".colM > h1")
    assert title_add_new_post.text == "Добавить post"

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value("1")
    post_title = browser.find_element_by_name("title")

    title_of_new_post = "Test Selenium title"

    post_title.send_keys(title_of_new_post)
    post_text = browser.find_element_by_name("text")
    post_text.send_keys("This text type by script")
    post_to_day = browser.find_element_by_name("published_date_0")
    post_to_day.send_keys("31.03.2020")
    post_rightnow = browser.find_element_by_name("published_date_1")
    post_rightnow.send_keys("17:18:54")
    save_button = browser.find_element_by_name("_save")
    save_button.click()
    success_message = browser.find_element_by_css_selector(".success > a")
    assert title_of_new_post == success_message.text

    time.sleep(1)
