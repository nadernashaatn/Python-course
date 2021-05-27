# you will able to add getters and setters "behind the scenes" without affecting the syntax that you used to access or modify the attribute when it was public.
#
#
class House:

    def __init__(self,price):
       self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price    

    @price.deleter
    def price(self):
        del self._price    

