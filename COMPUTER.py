class computer:
    def __init__(self):
        self.max__price=90000
    
    def selling_price(self):
        print(f"sellling price:{self.max__price}")
    
    def max__price(self,price):
        self.__max__price=price

c=computer()

c.selling_price()

c.__max__price=9687

c.sell_max_price(87520)

c.selling_price()