import sys
 
 
sys.path.append('D:/home/Project/homebib/scripts/') 
import hl_db as m_db


def test():

    m = m_db.All_book()
    m.Open_lib()

    m1 = m_db.Paper_book()
    m1.create_lib()


test()    