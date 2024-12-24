import requests

class WikiAPIClient:

    def __init__(self, wiki_api="https://ru.wikipedia.org/w/api.php"):
        self.wiki_api = wiki_api

    def search_for_articles(self, query):

        encoded_query = requests.utils.quote(query)
        url = f"{self.wiki_api}?action=query&list=search&utf8=&format=json&srsearch={encoded_query}"
        response = requests.get(url)
        response_data = response.json()
        return response_data.get('query', {}).get('search', [])