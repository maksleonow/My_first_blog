from .base_page import BasePage
from .selectors import LoginAdminPageSelectors


class LoginAdminPage(BasePage):

    def should_be_login_form(self):
        assert self.is_element_present(*LoginAdminPageSelectors.LOGIN_FROM), "Shoul be login form, but there is no it"

    def fill_login_form(self, login, pwd):
        user_name = self.browser.find_element(*LoginAdminPageSelectors.USERNAME_FIELD)
        user_name.send_keys(login)
        password = self.browser.find_element(*LoginAdminPageSelectors.PASSWORD_FIELD)
        password.send_keys(pwd)
        submit_button = self.browser.find_element(*LoginAdminPageSelectors.SUBMIT_BUTTON)
        submit_button.click()