


class Animal:
    def __init__(self,sound,color):
        self.sound = sound
        self.color = color

    def dog(self):
        self.sound = "Woof"
        return self
    
    def cat(self):
        self.color = "Yellow"
        return self

d = Animal("", "Black").dog()
c = Animal("Meow", "").cat()


print(d.sound, d.color)
print(c.sound, c.color)

    