


class All_book(object):
    """Общий класс для книг"""
    
    def __init__(self):
        """Constructor"""
        pass
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
    

class Paper_book(All_book):
    """Общий класс для книг"""
    
    def __init__(self):
        """Constructor"""
        pass
    def create_lib(self):
        print('PAPER_BOOK_create_lib')

    


if __name__ == "__main__":
    pass
    # car = Vehicle("blue", 5, 4, "car")
    # print(car.brake())
    # print(car.drive())
 
    # truck = Vehicle("red", 3, 6, "truck")
    # print(truck.drive())
    # print(truck.brake())