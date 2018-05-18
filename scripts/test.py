# coding: utf8

import sys
import hl_db as m_db



def test():
    
    m = m_db.Paper_book(None,'data/homebook.db')
    m.Open_lib()

    m.cur.execute("SELECT * FROM full_cat")
    for row in m.cur:
        print ('-'*10)
        
        print ('Наименование:', row[0])
        print ('Автор:', row[1])
        print ('Библиотека:', row[2])
        print ('Жанр:', row[3])
        print ('ebook:', row[4])
        print ('Год изд.:', row[5])
        print ('серия:', row[6])
        print ('Издательство:', row[7])
        
        print ('-'*10)
    #con.close()
    #print (m.cur.fetchall())
    

    # m1 = m_db.Paper_book()
    # m1.create_lib()



    book = ['','Наименование новое', '2','4' ,'2' ,'0' ,'2012','1' ,'' ,'','' ,'' ,'','' , '','', '', '']
    m.Add_book(m.cur,book)


test()    