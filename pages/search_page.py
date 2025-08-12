from .base_page import BasePage

class SearchPage(BasePage):
    
    def open(self):
        self.goto("https://duckduckgo.com/")

    def search(self, query):
         self.page.get_by_role("combobox", name="Search with DuckDuckGo").fill(query)
         self.page.get_by_role("button", name="Search", exact=True).click()
  
