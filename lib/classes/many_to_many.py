class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        #since theres no setter. validate in order to set the tit
        #*this works the too: type(title) == str
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
        #? ignore attempts to change the title, only solution that works
        pass
    
    def get_title(self):
        print(self._title)



class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass