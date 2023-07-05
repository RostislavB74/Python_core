class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        owner = dict.fromkeys(['name', 'age', 'address'])
        return owner


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
       # owner.info = dog.owner
        return owner.info()


owner = Owner("bob", 24, "London, 221B Baker Street")
# print(owner.name)
dog = Dog("Simon", 10, "british", owner)
dog.owner = Owner("Travolta", 33, 'ffrr')
# print(dict.keys)
print(dog.who_is_owner())
