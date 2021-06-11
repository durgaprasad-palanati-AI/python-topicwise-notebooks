#class with _init_
#method-1
print("class with _init_ ->method-1")
class mobile:
  def __init__(self, name, price):
    self.name = name
    self.price = price

m1 = mobile("samsung", 36000)

print(m1.name)
print(m1.price) 


#class with _init_
#method-2
print("class with _init_ ->method-2")
class mobile:
  def __init__(self, name, price):
    self.name = name
    self.price = price
  def details(self):
      print("moble name is %s and price is %d"%(self.name,self.price))
m1 = mobile("samsung", 36000)
m1.details()


#class without  _init_
print("class with out _init_")
class mobile:
  def func(self,name,price):
    print("moble name is %s and price is %d"%(name,price))

m1 = mobile()
m1.func("samsung", 36000)

del m1
m1.func("samsung", 36000)
