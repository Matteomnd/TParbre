class Node :
    def __init__(self,val,right=None,left=None):
        self.__val = val
        self.__right = right
        self.__left = left

    def get_right(self):
        return self.__right

    def get_left(self):
        return self.__left

    def get_value(self):
        return self.__val

    def set_right(self,right):
        self.__right = right

    def set_left(self,left):
        self.__left = left






