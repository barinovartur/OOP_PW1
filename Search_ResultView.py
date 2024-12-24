class SearchResultView:

    def show_results(self, results):
        if not results:
            print("По вашему запросу ничего не найдено.")
            return

        print("Найдено следующих статей:")
        for idx, article in enumerate(results, start=1):
            print(f"{idx}. {article['title']}")
