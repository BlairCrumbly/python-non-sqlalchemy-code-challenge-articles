class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        #!title must be a string between 5 and 50 characters and validation
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise TypeError("Title must be a string between 5 and 50 characters")
        type(self).all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_value):
        pass


class Author:
    all = []
    
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self._name = name
        self.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        pass
    
    def articles(self):
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        magazines_list = [article.magazine for article in self.articles()]
        unique_magazines = []
        for magazine in magazines_list:
            if magazine not in unique_magazines:
                unique_magazines.append(magazine)
        return unique_magazines
    
    def add_article(self, magazine, title):
        
        new_article = Article(self, magazine, title)
        return new_article
    
    def topic_areas(self):
        #!set for uniqueness
        areas = list(set([magazine.category for magazine in self.magazines()]))
        
        return None if not areas else areas


class Magazine:
    all = []
    
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = name
        
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = category
        
        self.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
    
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
    
    def contributors(self):
        #!return unique authors
        authors_list = [article.author for article in self.articles()]
        #! remove duplicates while preserving order
        unique_authors = []
        for author in authors_list:
            if author not in unique_authors:
                unique_authors.append(author)
        return unique_authors
    
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        
        return None if not titles else titles
    
    def contributing_authors(self):
        #authors who have written more than 2 articles for this magazine
        author_count = {}
        for article in self.articles():
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1
        
        authors = [author for author, count in author_count.items() if count > 2]
        return None if not authors else authors