
print("class inheritance")
class mobile:
  def __init__(self, name, price):
    self.name = name
    self.price = price
  def details(self):
      print("moble name is %s and price is %d"%(self.name,self.price))
m1 = mobile("samsung", 36000)
m1.details()

print("child class")
##child class

#method-1
'''
class generation(mobile):
    def __init__(self, name, price):
      mobile.__init__(self, name, price)
g1 = generation("samsung 5g", 75000)
g1.details()
'''
#method-2
'''
class generation(mobile):
    def __init__(self, name, price):
      super().__init__(name, price) #no self key
g1 = generation("samsung 5g", 75000)
g1.details()
'''
#Add new Properties
print("after adding new Properties")

#method-1
'''
class generation(mobile):
    def __init__(self, name, price,year):
      super().__init__(name, price) #no self key
      self.releaseyear = year        #new property
    def details(self):                #ovewrite the method
      print("moble name is %s and price is %d relased in %d year"%(self.name,self.price,self.releaseyear))
g1 = generation("samsung 5g", 75000,2019)
g1.details()
'''
#method-2
class generation(mobile):
    def __init__(self, name, price,year):
      mobile.__init__(self,name, price)
      self.releaseyear = year        #new property
    def details(self):                #ovewrite the method
      print("moble name is %s and price is %d relased in %d year"%(self.name,self.price,self.releaseyear))
g1 = generation("samsung 5g", 75000,2019)
g1.details()
