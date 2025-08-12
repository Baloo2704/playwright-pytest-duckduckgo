from .base_page import BasePage

class ResultsPage(BasePage):

    def result_search_box(self):
        return self.page.get_by_role("combobox", name="search")
