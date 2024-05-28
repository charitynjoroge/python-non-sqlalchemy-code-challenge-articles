class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    name = property(get_name, set_name)

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)  # Assuming Article class is defined elsewhere
        self._articles.append(new_article)
        return new_article

    def topic_areas(self):
        topics = list(set(article.magazine.category for article in self._articles if article.magazine.category))
        return topics if topics else None
