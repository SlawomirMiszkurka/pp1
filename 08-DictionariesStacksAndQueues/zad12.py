import json
book={
    'author':'Andrzej Pilipuk',
    'title':'Oko Jelenia',
    'genre':'Fiction',
    'price': 39.90,
    'number of pages':341}
with open('favourite.json','w') as file:
    json.dump(book,file,indent=4)