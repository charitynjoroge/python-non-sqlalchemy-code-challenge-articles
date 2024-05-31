class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self, "_title"):
            raise AttributeError("Title cannot be changed")
        if not isinstance(new_title, str):
            raise TypeError("Title must be a string")
        if not 5 <= len(new_title) <= 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = new_title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author):
            self._author = new_author
        else:
            raise TypeError("Author must be an instance of Author")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine):
            self._magazine = new_magazine
        else:
            raise TypeError("Magazine must be an instance of Magazine")

