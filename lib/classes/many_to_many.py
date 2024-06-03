from collections import Counter

class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
        

class Author:
    def __init__(self, name):
        self.name = name
        self.articles_list = []

    def articles(self):
        return self.articles_list

    def magazines(self):
        return self.magazines_list
        
    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        magazine.add_article(article)  # Associate the article with the magazine
        self.articles_list.append(article)
        return article
    
    def add_magazine(self, magazine):
        self.magazines_list.append(magazine) 

    def topic_areas(self):
        return list(set(article.magazine.category for article in self.articles()))

class Magazine:
    def __init__(self, name , category):
        self.name = name
        self.category = category
        self.articles_list = []
        self.contributors_list = []

    def articles(self):
        return self.articles_list
    
    def add_contributor(self, author):
        self.contributors_list.append(author)

    def contributing_authors(self):
        authors = []
        for author in self.contributors_list:
            if len([article for article in author.articles() if article.magazine == self]) > 2:
                authors.append(author)
        return authors

    def add_article(self, article):
        self.articles_list.append(article)

    def article_titles(self):
        return [article.title for article in self.articles_list if article.title]
