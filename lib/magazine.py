
class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.articles_published = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16:
                self._name = new_name
            else:
                raise ValueError("Name must be between 2 and 16 characters")
        else:
            raise TypeError("Name must be a string")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str):
            if len(new_category) > 0:
                self._category = new_category
            else:
                raise ValueError("Category must be longer than 0 characters")
        else:
            raise TypeError("Category must be a string")

    def articles(self):
        return self.articles_published

    def contributors(self):
        return [article.author for article in self.articles_published]

    def article_titles(self):
        return [article.title for article in self.articles_published]

    def contributing_authors(self):
        authors = {}
        for article in self.articles_published:
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1  
        
        return [author for author, count in authors.items() if count >= 2]