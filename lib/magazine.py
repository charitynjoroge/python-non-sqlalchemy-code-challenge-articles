class Magazine:
    def _init_(self, name, category):
        self._name = name
        self._category = category

        # Validation for name and category
        if not isinstance(self._name, str):
            raise TypeError("Name must be a string")
        if not 2 <= len(self._name) <= 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        if not isinstance(self._category, str):
            raise TypeError("Category must be a string")
        if len(self._category) == 0:
            raise ValueError("Category must be longer than 0 characters")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 2 <= len(value) <= 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = {}
        for article in self.articles():
            if article.author not in authors:
                authors[article.author] = 0
            authors[article.author] += 1
        return [author for author, count in authors.items() if count > 2]



if _name_ == "_main_":
  
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")

  
    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")


    article1 = author1.add_article(magazine1, "AI in 2024")
    article2 = author1.add_article(magazine2, "Healthy Living Tips")
    article3 = author2.add_article(magazine1, "The Future of Quantum Computing")
    article4 = author2.add_article(magazine2, "Mental Health Awareness")
    article5 = author2.add_article(magazine1, "Blockchain and Cryptocurrency")

    print(f"Articles written by {author1.name}:")
    for article in author1.articles():
        print(f"- {article.title} in {article.magazine.name}")


    print(f"Magazines {author1.name} has contributed to:")
    for magazine in author1.magazines():
        print(f"- {magazine.name}")

  
    print(f"Topic areas {author1.name} has written about:")
    for topic in author1.topic_areas():
        print(f"- {topic}")


    print(f"Articles published in {magazine1.name}:")
    for article in magazine1.articles():
        print(f"- {article.title} by {article.author.name}")


    print(f"Contributors to {magazine1.name}:")
    for author in magazine1.contributors():
        print(f"- {author.name}")


    print(f"Article titles in {magazine1.name}:")
    for title in magazine1.article_titles():
        print(f"- {title}")

 
    print(f"Authors with more than 2 articles in {magazine1.name}:")
    for author in magazine1.contributing_authors():
        print(f"- {author.name}")