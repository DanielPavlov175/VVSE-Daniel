class Vehicle:
    def __init__(self,mark,model,price):
        self.mark=mark
        self.model=model
        self.price=price

class Car(Vehicle):
    def __init__(self, mark, model, price):
        super().__init__(mark, model, price)

class Bus(Vehicle):
    def __init__(self, mark, model, price):
        super().__init__(mark, model, price)

class Van(Vehicle):
    def __init__(self, mark, model, price):
        super().__init__(mark, model, price)

c1=Car("Audi","A6",10000)
c2=Car("Mercedes","C220",15000)
c3=Car("Opel","Astra",4000)

b1=Bus("Bus1","A",20000)
b2=Bus("Bus2","B",25000)
b3=Bus("Bus3","C",30000)

v1=Van("Van1","A",15000)
v2=Van("Van2","B",20000)
v3=Van("Van3","C",25000)

print("Vehicle:")
s=str(input())
if s=="car":
    print(c1.mark,c1.model,c1.price,"$")
    print(c2.mark,c2.model,c2.price,"$")
    print(c3.mark,c3.model,c3.price,"$")
if s=="bus":
    print(b1.mark,b1.model,b1.price,"$")
    print(b2.mark,b2.model,b2.price,"$")
    print(b3.mark,b3.model,b3.price,"$")
if s=="van":
    print(v1.mark,v1.model,v1.price,"$")
    print(v2.mark,v2.model,v2.price,"$")
    print(v3.mark,v3.model,v3.price,"$")