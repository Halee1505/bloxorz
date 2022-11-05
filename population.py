class Populations:
    def __init__(self, populations, count):
        self.populations = populations  # list of population
        self.count = count

    class Population:
        def __init__(self, population, fitness_score, probability=0):
            self.population = population  # list of state
            self.fitness_score = fitness_score
            self.probability = probability
