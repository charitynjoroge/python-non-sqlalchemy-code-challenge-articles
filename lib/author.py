
class Author:
    def __init__(self, name):
        self.name = name
        self.articles_written = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if hasattr(self, "_name"):
            raise AttributeError("Name cannot be changed")
        else:
            if isinstance(new_name, str):
                if len(new_name) > 0:
                    self._name = new_name
                else:
                    raise ValueError("Name must be longer than 0 characters")
            else:
                raise TypeError("Name must be a string")

    def articles(self):
        return self.articles_written
    
    def magazines(self):
        return [article.magazine for article in self.articles_written]

    def add_article(self, magazine, title):
        article = article(self, magazine, title)
        self.articles_written.append(article)
        return article

    def topic_areas(self):
        return list(set(magazine.category for magazine in self.magazines()))
