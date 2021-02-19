import random
from exceptions import *


class Enemy(object):

    def __init__(self, level, lives):
        self.level = level
        self.lives = lives

    @staticmethod
    def select_attack():
        return random.randrange(1, 4, 1)

    def decrease_lives(self):
        if self.lives > 1:
            self.lives = self.lives - 1
            return self.lives
        elif self.lives == 1:
            raise EnemyDown


class Player:
    score = 0

    allowed_attacks = int

    def __init__(self, name, lives):
        self.name = name
        self.lives = lives

    def decrease_lives(self):
        if self.lives > 1:
            self.lives = self.lives - 1
            return self.lives
        elif self.lives == 1:
            print("You reach: {}".format(self.score))
            scores = open('scores.txt', 'a+')
            if self.score < 10:
                self.score = '0' + str(self.score)
            scores.write("{}: {} \n".format(self.name, self.score))
            scores.close()
            self.top_ten_scores()
            raise GameOver("Your lives ended")

    def attack(self, enemy_obj):

        self.allowed_attacks = int(input("Please select attack type "))
        result = self.fight(self.allowed_attacks, enemy_obj.select_attack())

        if result == 0:
            return "It's draw!"
        elif result == 1:

            self.score = self.score + 1

            return "You attacked successfully"
        else:
            return "You missed"

    def defence(self, enemy_obj):
        self.allowed_attacks = int(input("Please select defense type: "))

        result = self.fight(enemy_obj.select_attack(), self.allowed_attacks)

        if result == 0:
            return "It's draw!"
        elif result == 1:
            self.decrease_lives()
            return "Your defense failed"
        else:
            return "You defensed successfully"

    @staticmethod
    def top_ten_scores():
        top_scores = {}
        with open('scores.txt') as file:
            for line in file:
                key, value = line.split()
                top_scores[key] = value
        list_of_scores = list(top_scores.items())
        list_of_scores.sort(key=lambda i: i[1])
        if len(list_of_scores) == 11 and list_of_scores[0][1] > list_of_scores[10][1]:
            del list_of_scores[10]
        elif len(list_of_scores) == 11 and list_of_scores[0][1] < list_of_scores[10][1]:
            del list_of_scores[0]
        file = open('scores.txt', 'w')
        for score in list_of_scores:
            file.write(' '.join(str(s) for s in score) + '\n')

    @staticmethod
    def fight(attack, defense):
        if attack == defense:
            return 0
        elif attack == 1 and defense == 3 \
                or attack == 2 and defense == 1 \
                or attack == 3 and defense == 2:
            return 1
        else:
            return -1




