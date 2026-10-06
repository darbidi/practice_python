import random
class Game():
    def __init__(self):
        self.secret_num = random.randint(1, 1000)

    def play(self):  # هم‌تراز با init
        while True:  # یک Tab فاصله از چپ (داخل متد)

            number = int(input("enter yor gess: "))  # دو Tab فاصله (داخل حلقه)

            if number > self.secret_num:  # دو Tab فاصله
                print("you guessed too high")
            elif number < self.secret_num:  # دو Tab فاصله
                print("you guessed too low")
            else:  # دو Tab فاصله
                print("you guessed correctly")
                break  # سه Tab فاصله! (فقط وقتی برنده شد ترمز کشیده می‌شه)




my_game = Game()

my_game.play()