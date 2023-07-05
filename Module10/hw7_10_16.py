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

    def info(self, name, age, address):
        owner = dict.fromkeys(['name', 'age', 'address'][name, age, address])
        return owner.info()


class Dog(Animal, Owner):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner.info(self, 'name', 'age', 'address')
        super(Owner).__init__(self, name, age, address)
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return owner.info('name', 'age', 'address')


owner = Owner("bob", 24, "London, 221B Baker Street")
dog = Dog("Simon", 10, "british", owner)
