class Article:
    all = []
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if value is str and  50 >= len(value) >= 5 and self.title == None:
            self._title = value
        else: 
            raise TypeError("wrong type")
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        self._author = author
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, mag):
        self._magazine = mag
            
class Author:
    all = []
    def __init__(self, name):
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    #is checks types of two objects, so you don't have to do value(type)
    @name.setter
    def name(self, value):
        if value is str and self._name == None and len(value) > 0:
            self._name = value
        else:
            raise TypeError("wrong type")
    
    def articles(self):
        articles_list = []
        for each in Article.all:
            if each.author == self:
                articles_list.append(each)
        return articles_list

    def magazines(self):
        mag_list = []
        for each in Article.all:
            if each.author == self and each.magazine not in mag_list:
                mag_list.append(each.magazine)
        return mag_list


    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        list_of_topics = []
        for each in Article.all:
            if each.author == self and each.magazine.category not in list_of_topics:
                list_of_topics.append(each.magazine.category)
        if list_of_topics == []:
            list_of_topics = None
        return list_of_topics
    

class Magazine:
    all = []
    def __init__(self, name, category):
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    
    @name.setter
    def name(self,value):
        if type(value) is str and 16 >= len(value) >= 2:
            self._name = value
        else:
            raise TypeError("wrong type")
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if type(value) is str and len(value) > 0:
            self._category = value
        else:
            raise TypeError("wrong type")
            
    def articles(self):
        list_art = []
        for each in Article.all:
            if each.magazine == self:
                list_art.append(each)
        return list_art
    
    def contributors(self):
        unique_cont = []
        for each in Article.all:
            if each.magazine == self and each.author not in unique_cont:
                unique_cont.append(each.author)
        return unique_cont
    
    def article_titles(self):
        list_of_titles = []
        for each in Article.all:
            if each.magazine == self:
                list_of_titles.append(each.title)
        if list_of_titles == []: 
            list_of_titles = None
        return list_of_titles
    def contributing_authors(self):
        list_of_authors1 = []
        list_of_authors2 = []
        final_list_of_authors = []
        for each in Article.all:
            if each.magazine == self and each.author not in list_of_authors1:
                list_of_authors1.append(each.author)
            elif each.magazine == self and each.author not in list_of_authors2 and each.author in list_of_authors1:
                list_of_authors2.append(each.author)
            elif each.magazine == self and each.author in list_of_authors2 and each.author in list_of_authors1 and each.author not in final_list_of_authors:
                final_list_of_authors.append(each.author)
        if final_list_of_authors == []:
            final_list_of_authors = None
        return final_list_of_authors
    def top_publisher():
        unique_magazine_list = {}
        highest_mag = None
        highest_int = 0
        for each in Article.all:
            if each.magazine not in unique_magazine_list:
                unique_magazine_list[each.magazine] = 0
            else:
                unique_magazine_list[each.magazine] += 1
        for each in unique_magazine_list:
            if unique_magazine_list[each] > highest_int:
                highest_int = unique_magazine_list[each]
                highest_mag = each
        return highest_mag