class Animal:
    def __init__(self,type,talk):
        self.type=type
        self.talk=talk
cat=Animal("cat","meow")
dog=Animal("dog","barf")
mouse=Animal("mouse","tsur")
wolf=Animal("wolf","oooouuuuuu")
cow=Animal("cow","moooo")

while 1:
    print("Animal:")
    s=str(input())
    if s==cat.type:
        print(cat.talk)
    if s==dog.type:
        print(dog.talk)
    if s==mouse.type:
        print(mouse.talk)
    if s==wolf.type:
        print(wolf.talk)
    if s==cow.type:
        print(cow.talk)
    if s=="end":
        break