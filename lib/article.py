class Article:
    all = []

    def _init_(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title

        # Validation for title
        if not isinstance(self._title, str):
            raise TypeError("Title must be a string")
        if not 5 <= len(self._title) <= 50:
            raise ValueError("Title must be between 5 and 50 characters, inclusive")

        Article.all.append(self)

    @property
    def title(self):
        return self._title
