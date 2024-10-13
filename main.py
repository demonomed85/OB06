class Hero:
    def __init__(self, name, health = 100, attack_power = 20):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.alive = True

    def attack(self, other):
        other.health -= self.attack_power
        if other.health <= 0:
            other.alive = False

    def is_alive(self):
        return self.alive

class game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start(self):
        while self.player1.is_alive() and self.player2.is_alive():
            self.player1.attack(self.player2)
            print(f"{self.player1.name} атаковал {self.player2.name} и у него осталось {self.player1.health}")
            if not self.player2.is_alive():
                print(f"{self.player1.name} выиграл!")
                break
            self.player2.attack(self.player1)
            print(f"{self.player2.name} атаковал {self.player1.name} и у него осталось {self.player2.health}")
            if not self.player1.is_alive():
                print(f"{self.player2.name} выиграл!")
                break

User = Hero(input("Введите имя героя: "))
Computer = Hero("Computer", 100, 20)
game = game(User, Computer)
game.start()