#class with _init_
class mobile:
  def __init__(self, name, price):
    self.name = name
    self.price = price

m1 = mobile("samsung", 36000)

print(m1.name)
print(m1.price) 

#class without  _init_
class mobile:
  def func(self,name,price):
    print("moble name is %s and price is %d"%(name,price))

m1 = mobile()
m1.func("samsung", 36000)

del m1
m1.func("samsung", 36000)
