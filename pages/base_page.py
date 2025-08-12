class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def click(self, selector):
        self.page.click(selector)

    def fill(self, selector, value):
        self.page.fill(selector, value)

    def text_content(self, selector):
        return self.page.text_content(selector)

    def all_text_contents(self, selector):
        return self.page.locator(selector).all_text_contents()
