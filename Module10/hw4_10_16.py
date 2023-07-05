class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, color):
        self.color = color


first_animal=Animal('nickname', 10)
second_animal=Animal('nickname1', 10)
Animal.change_color(Animal,'red')
