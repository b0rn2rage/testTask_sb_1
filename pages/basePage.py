class BasePage:

    def __init__(self, browser, base_url: str):
        self.browser = browser
        self.base_url = base_url
