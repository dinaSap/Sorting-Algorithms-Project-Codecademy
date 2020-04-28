import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
#for item in bookshelf:
  #print(item['title'])
  
def by_title_ascending(book_a, book_b):
  if book_a['title_lower'] > book_b['title_lower']:
    return True
  else:
    return False
  
def by_author_ascending(book_a, book_b):
  if book_a['author_lower'] > book_b['author_lower']:
    return True
  else:
    return False

def by_total_length(book_a, book_b):
  return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])
  
bookshelf_v1 = bookshelf.copy()
sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)  

sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)


bookshelf_v2 = bookshelf.copy()
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

long_bookshelf = utils.load_books('books_large.csv')
#sorts.bubble_sort(long_bookshelf, by_total_length) 
sorts.quicksort(long_bookshelf, by_total_length)









  
