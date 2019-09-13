from montecarlo import MontercarloSimulation
import random
class Birthday:    
    def __init__(self, n):
            self.n = n
    def play(self):
      birthdays = {}
      for i in range(self.n):
        day = random.randint(1, 365)
        p = birthdays.get(day, 0)
        if p == 1:
            return 1
        birthdays[day] = p + 1
      return 0
          


if __name__ == "__main__":
       c = Birthday(50)
       m = MontercarloSimulation(10, 1000, c)
       res = m.simulate()
       print(res)
