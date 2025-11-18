
from book import Book


class Library:
    
    def __init__(self, name):
        self.__name = name
        self.__collection = []
    
    
    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError('Invalid Book object')
        
        self.__collection.append(book)
        
        
    def remove_book(self, key, field='id'):
        pass


    def find_book(self, key, field='id'):
        pass

    
    def __get_max_len(self, column):
        field = column['field']
        title = column['title']
        max_len = len(title)
        for book in self.__collection:
            max_len = max(max_len, len(str(book[field])))
        return max_len
    
    
    def report_books(self):
        report_columns = (
            {
                'title': 'IDXX',
                'width': 0,
                'align': '>',
                'field': 'id'
            },
            {
                'title': 'TÍTULO',
                'width': 0,
                'align': '<',
                'field': 'title'
            },
                        {
                'title': 'AUTOR',
                'width': 0,
                'align': '<',
                'field': 'author'
            },
            {
                'title': 'ANO PUB',
                'width': 0,
                'align': '>',
                'field': 'year'
            },
        )
        
        for col in report_columns:
            title = col['title']
            width = col['width']
            if width == 0:
                width = self.__get_max_len(col)
                col['width'] = width
                
            print(f'{title:<{width + 1}}', end='')
        print()
        
        for col in report_columns:
            width = col['width']
            print('-' * width, end=' ')
        print()
        
        for book in self.__collection:
            for col in report_columns:
                align = col['align']
                width = col['width']
                field = col['field']
                value = book[field]
                
                print(f'{value:{align}{width}}', end=' ')
            print()
        