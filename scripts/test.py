# coding: utf8

import sys
import hl_db as m_db



def test():
    
    m = m_db.Paper_book(None,'data/homebook.db')
    m.Open_lib()
#     m.cur.execute('''SELECT book.name,
#        author.fullName,
#        library.name AS libName,
#        genre.name AS genreName,
#        book.ebook,
#        book.ypubl
#   FROM book,
#        author,
#        library,
#        genre
#  WHERE author.id = book.author AND 
#        library.id = book.library AND 
#        genre.id = book.genre''')
    m.cur.execute("Select * from full_cat ")
    for row in m.cur:
        print ('-'*10)
        
        print ('Наименование:', row[0])
        print ('Автор:', row[1])
        print ('Библиотека:', row[2])
        print ('Жанр:', row[3])
        print ('ebook:', row[4])
        print ('Год изд.:', row[5])
        
        
        print ('-'*10)
    #con.close()
    #print (m.cur.fetchall())
    

    # m1 = m_db.Paper_book()
    # m1.create_lib()

test()    