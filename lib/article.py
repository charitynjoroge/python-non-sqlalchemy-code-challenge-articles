class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        self.author._articles.append(self)
        self.magazine._articles.append(self)
        Article.all.append(self)
    
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if isinstance(title, str):
            self._title = title

    title = property(get_title, set_title)
