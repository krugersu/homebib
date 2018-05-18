import sqlite3


class All_book(object):
    """Общий класс для книг"""
   
    def __init__(self,cur,path_db):
        """Constructor"""
        self.conn = sqlite3.connect(path_db) 
        self.cur = self.conn.cursor()
        # book = [(4,'Наименование', '','' ,'' ,'' ,'','' ,'' ,'','' ,'' ,'','' , '','', '', '')]
        # # book = [('','Наименование', 2, 4, 2, 0,'7/9/2002', 2, 0,'Обложка', 0, 3,100000, 256, 'Описание'
        # # ,'ISBN', 'Твердая', 1)]
        # # book = [('Наименование', 'Библиотека', 'Автор', 'Жанр', 'Ебук','ДатаПубликации', 'Серия', 'Поиск','Обложка', 'Номер в серии', 'Издательство','Тираж', 'Количество страниц', 'Описание'
        # # ,'ISBN', 'ТипОбложки', 'Художник'),
          
 
        # self.cur.executemany('INSERT INTO book VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', book)
        # conn.commit()
    def __create_lib(self):
        pass

    def Open_lib(self):
        """
        Open library 
        """
        print('all_book_Open_lib')
    
    def Close_lib(self):
        """
        Close library
        """
        pass
    def Create_lib(self):
        pass

    def Add_book(self,cursor,bookD):
        
        #self.cur.execute("SELECT MAX (id_book) from book")
        # id_book =  self.cur.fetchone()[0] + 1
        # bookD[0] = id_book
        # print(bookD[0])
        # #print(book[0])

        # book = [(5,'Наименование', '','' ,'' ,'' ,'','' ,'' ,'','' ,'' ,'','' , '','', '', '')]
        # book = [('','Наименование', 2, 4, 2, 0,'7/9/2002', 2, 0,'Обложка', 0, 3,100000, 256, 'Описание'
        # ,'ISBN', 'Твердая', 1)]
        # book = [('Наименование', 'Библиотека', 'Автор', 'Жанр', 'Ебук','ДатаПубликации', 'Серия', 'Поиск','Обложка', 'Номер в серии', 'Издательство','Тираж', 'Количество страниц', 'Описание'
        # ,'ISBN', 'ТипОбложки', 'Художник'),
          
 
        self.cur.executemany('INSERT INTO book VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', bookD)
        self.conn.commit()
        

class Paper_book(All_book):
    """Класс для бумажных книг"""
    
    # def __init__(self):
    #     """Constructor"""
    #     pass
    def create_lib(self):
        print('PAPER_BOOK_create_lib')

    
class E_book(All_book):
    """Класс для электронных книг"""
    
    # def __init__(self):
    #     """Constructor"""
    #     pass
    def create_lib(self):
        print('E_BOOK_create_lib')


if __name__ == "__main__":
    pass
    # car = Vehicle("blue", 5, 4, "car")
    # print(car.brake())
    # print(car.drive())
 
    # truck = Vehicle("red", 3, 6, "truck")
    # print(truck.drive())
    # print(truck.brake())