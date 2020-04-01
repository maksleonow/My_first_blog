from selenium.webdriver.common.by import By
class LoginAdminPageSelectors:
    LOGIN_FROM = (By.CSS_SELECTOR, "#login-form")
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".submit-row > input")