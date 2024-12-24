import webbrowser

class ArticlePageOpener:

    def open_article(self, article_id):
        w_url = f"https://ru.wikipedia.org/w/index.php?curid={article_id}"
        webbrowser.open(w_url)
