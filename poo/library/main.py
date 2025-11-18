
from book import Book
from library import Library
from fake_books import fake_books


def main():
    my_lib = Library('UESPI Parnaíba')

    for fb in fake_books:       
        book = Book(
            fb['id'], 
            fb['title'], 
            fb['author'], 
            fb['year']
        )
        
        my_lib.add_book(book)
        
    my_lib.report_books()
    

if __name__ == '__main__':
    main()
