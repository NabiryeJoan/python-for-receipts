class Dog:
    def __init__(self,name, age):
        self.name = name
        self.age = age 
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
# d= Dog("tim",34)
# print(d.name,d.age)
# when u want to change the age
    def set_age(self,age):
        self.age = age
d=Dog("bill",34)
d.set_age(23) 
print(d.name) 
print(d.get_age())      
        
        