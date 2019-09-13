import random
from montecarlo import MontercarloSimulation


class Craps:
    def __init__(self):
        pass
    def roll_dices(self):
        first = random.choice([x + 1 for x in range(6)])
        second = random.choice([x + 1 for x in range(6)])
        return (first, second)
    """simulates a game, returns true if the player wins, 0 otherwise."""
    def play(self):
        numbers = self.roll_dices()
        sum = numbers[0] + numbers[1]
        if sum == 7 or sum == 11:
            return 1
        elif sum == 2 or sum == 3 or sum == 12:
            return 0
        else:
            return self.find_sum(sum)
    
    def find_sum(self, number):
        while True:
            numbers = self.roll_dices()
            sum = numbers[0] + numbers[1]
            if sum == number:
                return 1
            elif sum == 7:
                return 0
            else:
                return self.find_sum(number)

if __name__ == "__main__":
       c = Craps()
       m = MontercarloSimulation(10, 1000, c)
       res = m.simulate()
       print(res)
