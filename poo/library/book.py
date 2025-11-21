
class Book:
    
    def __init__(self, id, title, author, year):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__year = year
        
    
    def __repr__(self):
        return str(self)
    
    
    def __str__(self):
        return f'Book({self.__id},{self.__title},{self.__year})'
    
       
    def __getitem__(self, field):
        match field:
            case 'id':
                return self.__id
            case 'title':
                return self.__title
            case 'author':
                return self.__author
            case 'year':
                return self.__year
        raise IndexError(f'Invalid Book field: {field}')
    
    
    def id(self):
        return self.__id
    
    
    def title(self):
        return self.__title
    
    
    def author(self):
        return self.__author
    
    
    def year(self):
        return self.__year