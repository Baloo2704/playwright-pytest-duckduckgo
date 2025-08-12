import allure
from playwright.sync_api import expect
from pages.search_page import SearchPage
from pages.results_page import ResultsPage


@allure.feature("DuckDuckGo Search")

class TestDuckDuckGo:

    @allure.story("Search returns results")
    def test_search_returns_results(self, page):
        search_page = SearchPage(page)
        results_page = ResultsPage(page)

        search_page.open()
        search_page.search("Playwright Python")

        expect(results_page.result_search_box()).to_have_value("Playwright Python")






# @allure.feature("DuckDuckGo Search")
# @pytest.mark.asyncio
# class TestDuckDuckGo:

#     # @allure.story("Search returns results")
#     async def test_search_returns_results(self, page):
#         search_page = SearchPage(page)
#         results_page = ResultsPage(page)

#         await search_page.open()
#         await search_page.search("Playwright Python")

#         assert await results_page.result_count() > 0

    # @allure.story("First result contains query")
    # async def test_first_result_contains_query(self, page):
    #     search_page = SearchPage(page)
    #     results_page = ResultsPage(page)

    #     await search_page.open()
    #     await search_page.search("OpenAI GPT-5")

    #     first_title = (await results_page.first_result_title()).lower()
    #     assert "openai" in first_title or "gpt" in first_title

    # @allure.story("Multiple results returned")
    # async def test_multiple_results(self, page):
    #     search_page = SearchPage(page)
    #     results_page = ResultsPage(page)

    #     await search_page.open()
    #     await search_page.search("Selenium vs Playwright")

    #     assert await results_page.result_count() >= 5

    # @allure.story("Result titles are not empty")
    # async def test_result_titles_not_empty(self, page):
    #     search_page = SearchPage(page)
    #     results_page = ResultsPage(page)

    #     await search_page.open()
    #     await search_page.search("Python pytest tutorial")

    #     titles = await results_page.get_result_titles()
    #     assert all(title.strip() for title in titles)

    # @allure.story("Search with special characters")
    # async def test_search_special_characters(self, page):
    #     search_page = SearchPage(page)
    #     results_page = ResultsPage(page)

    #     await search_page.open()
    #     await search_page.search("@#$%^& DuckDuckGo test")

    #     assert await results_page.result_count() > 0
