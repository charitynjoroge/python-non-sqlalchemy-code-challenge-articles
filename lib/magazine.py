class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = []
        self._contributors = set()
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def add_article(self, author, title):
        article = article(author, self, title)
        self._articles.append(article)
        return article

    def articles(self):
        return self._articles 

    def contributors(self):
        return list(self._contributors) 

    def article_titles(self):
        return [article.title for article in self._articles] 
        

    def contributing_authors(self):
        authors=[article.author for article in self._articles]
        return [author for author in set(authors) if authors.counts() > 2]
        

    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines, key=lambda magazine: len(magazine.articles()))