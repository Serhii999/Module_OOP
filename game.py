from models import *

from settings import *

if __name__ == '__main__':

    def play():
        player = Player(name=str(input("Please Enter your name: ")),
                        lives=int(input("if you want to play hard mode pick 1 live \n"
                                        "if you want to play middle mode pick 3 lives \n"
                                        "and if you want to play easy mode pick 5 lives, \n"
                                        "Please, choose how many lives do you want: ")))
        print(rules())
        try:
            player_live(player.lives)
        except IncorrectLivesInput:
            print("Please, choise correct mode")
            player = Player(name=str(input("Please Enter your name: ")),
                            lives=int(input("if you want to play hard mod pick 1 live \n"
                                            "if you want to play middle mod pick 3 lives \n"
                                            "and if you want to play easy mod pick 5 lives, \n"
                                            "Please, choose how many lives do you want: ")))
            player_live(player.lives)

        enemy_obj = Enemy(1, 1)

        start = str(input("Enter start to play the game "))

        if start == 'start':
            while True:
                try:
                    print("\nYour turn to attack")
                    attack = player.attack(enemy_obj)
                    print(attack)
                    if attack == "You attacked successfully":
                        enemy_obj.decrease_lives()
                    print("\nYour turn to defense")
                    print(player.defence(enemy_obj))
                except EnemyDown:
                    player.score = player.score + 5
                    print("Your score: {} ".format(player.score))
                    print("Level Up")
                    enemy_obj.level = enemy_obj.level + 1
                    enemy_obj.lives = enemy_obj.level
                    print("Enemy level: {}".format(enemy_obj.level))
                    print("Enemy lives: {}".format(enemy_obj.lives))


    try:
        play()
    except GameOver:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        print("Good Bye!")

    input()