import random as random
import numpy as np
from scipy import stats
class MontercarloSimulation:
    """Returns the following tuple, (mean,confidence_interval(a,b),confidence) """
    def __init__(self, experiments, times, game):
        self.times = times
        self.game = game
        self.experiments = experiments

    def experiment(self):
        results = {
            0 : 0,
            1 : 0
        }
        
        for x in range(self.times):
            r = self.game.play()
            results[r] = results[r] +1 
        per_win = results[1] / self.times
        return per_win

    def simulate(self):
        acc = []
        for x in range(self.experiments):
            p = self.experiment()
            acc.append(p)
        res = np.array(acc)
        mean = np.mean(res)
        std = np.std(res)
        conf_interval = [ mean - ((2 * std) ), (2 * std) + mean]
        return (mean,conf_interval,0.95)
