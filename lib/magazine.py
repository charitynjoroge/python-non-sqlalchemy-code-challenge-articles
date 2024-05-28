class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
    name = property(get_name, set_name)

    def get_category(self):
        return self._category
    
    def set_category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        
    category = property(get_category, set_category)

    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        return self._articles
    
    def contributors(self):
        return list(set([article.author for article in self._articles]))

    def article_titles(self):
        titles = [article.title for article in self._articles]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self._articles]
        contributing_authors = [author for author in set(authors) if authors.count(author) > 2]
        return contributing_authors if contributing_authors else None
