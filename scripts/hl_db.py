import sqlite3


class All_book(object):
    """Общий класс для книг"""
   
    def __init__(self,cur,path_db):
        """Constructor"""
        conn = sqlite3.connect(path_db) 
        self.cur = conn.cursor()
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