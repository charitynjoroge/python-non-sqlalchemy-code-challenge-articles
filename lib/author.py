class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._articles = []

    def articles(self):
        return self._articles 
    @property
    def name(self):
        return self._name

    def magazines(self):
        return list(set(article.magazine for article in self._articles)) 
    

    def create_article(self, magazine, title):
        article = article(self, magazine, title)
        self._articles.append(article)
        return article

    def articles(self):
        return self._articles

    def add_article(self, magazine, title):
        article = article(self, magazine, title)
        self._articles.append(article) 
        article = article(self, magazine, title)  
        self._articles.append(article)  
        return article

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

    def contributing_authors(self):
        if not self._articles:
            return []
        author_count = {}
        for article in self._articles:
            if article.author in author_count:
                author_count[article.author] += 1
            else:
                author_count[article.author] = 1
        return [author for author, count in author_count.items() if count > 2]

