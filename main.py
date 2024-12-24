from Wiki_APIClient import WikiAPIClient
from Search_ResultView import SearchResultView
from ArticlePage_Opener import ArticlePageOpener

class WikiApp:

    def __init__(self):
        self.api_client = WikiAPIClient()
        self.result_view = SearchResultView()
        self.page_opener = ArticlePageOpener()

    def start(self):
        query = input("Введите запрос для поиска статей: ")
        search_results = self.api_client.search_for_articles(query)
        if not search_results:
            print("По вашему запросу ничего не найдено. Программа завершена.")
            return
        self.result_view.show_results(search_results)

        self._process_user_selection(search_results)

    def _process_user_selection(self, search_results):
        try:
            selection = int(input("Введите номер статьи для открытия (или 0 для выхода): "))
            if selection == 0:
                print("Выход из программы.")
                return
            elif 1 <= selection <= len(search_results):
                selected_article = search_results[selection - 1]
                self.page_opener.open_article(selected_article['pageid'])
            else:
                print("Некорректный номер. Пожалуйста, выберите правильный номер статьи.")
        except ValueError:
            print("Ошибка ввода. Введите число.")

def main():
    app = WikiApp()
    app.start()

if __name__ == "__main__":
    main()
