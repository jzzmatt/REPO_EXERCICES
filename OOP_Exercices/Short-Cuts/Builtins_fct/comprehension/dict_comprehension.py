'''
Comprehensions aren't restricted to lists

'''

from collections import namedtuple

Book = namedtuple("Book", "author title genre")

books = [
    Book("Pratchett", "Nightwatch", "fantasy"),
    Book("Pratchett", "Thief of time", "fantasy"),
    Book("Le Guin", "The Dispossessed", "scifi"),
    Book("Le Guin", "A Wizard of Earthsea", "fantasy"),
    Book("Turner", "The thief", "fantasy"),
    Book("Phillips", "Preston Diammond", "western"),
    Book("Phillips", "Twice Upon A Time", "scifi"),


]

#print(books)

fantasy_authors = {
    b.author for b in books if b.genre == 'fantasy'
}

print(fantasy_authors)

fantasy_titles = {
    b.title:  b for b in books if b.genre == 'fantasy'
}


print(fantasy_titles)

