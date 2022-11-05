import time
from population import Populations
import math
import random


def print_state(state):
    print("--------------------------")
    print(((state.block.node1.x, state.block.node1.y),
          (state.block.node2.x, state.block.node2.y)))
    print("--------------------------")


def print_block(state):
    print(state.block.string_block())


def print_population(population):
    pr = ""
    for state in population:
        pr += state.block.string_block() + "|"
    print(pr)
    return pr


def print_populations(populations):
    # print("Watch populations")
    # print("count", populations.count)
    pr = ""
    for populations in populations.populations:
        if pr != print_population(populations.population):
            pr = print_population(populations.population)
            # print("fitness_score", populations.fitness_score)
        # print("probability", populations.probability)
        # print("xxxxxxxxxxxxxx")


def dfs(init_state):
    stack = []
    stack.append(init_state)
    visited = set()
    ind = 0
    time_start = time.time()
    print("start a new state")
    while stack:
        curr_state = stack.pop()
        if curr_state.finish() is True:
            print("time: ", time.time() - time_start)
            return curr_state
        if curr_state.block.string_block() not in visited:
            visited.add(curr_state.block.string_block())
            for next_state in curr_state.move():
                stack.append(next_state)
        #     print(len(curr_state.move()))
        # ind += 1
        # if ind == 1:
        #     return curr_state
        # time.sleep(1)


def generate_new_population(init_state, population_size):
    population = []
    population.append(init_state)
    while len(population) < population_size:
        population.append(population[len(population)-1].random_move())
    return Populations.Population(population, fitness_function(population))


def generate_populations(init_state, population_size):
    populations = Populations([], population_size)

    while len(populations.populations) < population_size:
        population = generate_new_population(init_state, population_size)
        populations.populations.append(population)
    calculate_probability(populations.populations)

    return populations


def fitness_function(population):
    bad_fitness = math.sqrt((population[0].block.node1.x - population[0].goal.x)**2 +
                            (population[0].block.node1.y - population[0].goal.y)**2) * len(population)
    fitness_score = 0
    for state in population:
        center = (math.floor((state.block.node1.x + state.block.node2.x) / 2),
                  math.floor((state.block.node1.y + state.block.node2.y) / 2))
        fitness_score += math.sqrt((center[0] - state.goal.x)**2 +
                                   (center[1] - state.goal.y)**2)
    return bad_fitness-fitness_score


def calculate_probability(populations):
    total_fitness = 0
    for population in populations:
        total_fitness += population.fitness_score
    for population in populations:
        population.probability = population.fitness_score / total_fitness


def select(populations, r, p):
    selection_count = math.ceil((1-r)*p)
    selection_array = []
    while len(selection_array) < selection_count:
        for population in populations:
            selection_percent = random.random() * p
            if population.probability > selection_percent:
                selection_array.append(population)

    return selection_array


def crossover(populations, r, p):

    pair_count = math.floor((r/2)*p)  # số cặp
    crossover_array = []
    while len(crossover_array) < pair_count:
        # random 2 cá thể trong quần thể
        random_pair = random.sample(populations, 2)
        random_index = random.randint(0, p-1)
        population_child1 = random_pair[0].population[:random_index] + \
            random_pair[1].population[random_index:]
        population_child2 = random_pair[1].population[:random_index] + \
            random_pair[0].population[random_index:]

        new_population1 = Populations.Population(
            population_child1, fitness_function(population_child1))
        new_population2 = Populations.Population(
            population_child2, fitness_function(population_child2))

        crossover_array.append(new_population1)
        crossover_array.append(new_population2)
    return crossover_array


def mutation_state(state):
    parent_state = state.parent
    if parent_state is None:
        return state
    else:
        return parent_state.random_move()


def mutation(populations, mutation_percent, p):
    mutation_count = math.floor(mutation_percent*p)
    while mutation_count > 0:
        random_population_index = random.randint(0, len(populations)-1)
        population = populations[random_population_index].population
        random_state_index = random.randint(0, len(population)-1)
        population[random_state_index] = mutation_state(
            population[random_state_index])
        populations[random_population_index].population = population
        mutation_count -= 1
    return populations


def get_max_fitness(populations):

    max_fitness = 0
    for population in populations:
        if population.fitness_score > max_fitness:
            max_fitness = population.fitness_score
    return max_fitness


def genetic_algorithm(init_state, population_size):
    populations = generate_populations(init_state, population_size)

    # while True:
    new_population_list = []
    r = random.random()
    print("max fitness: ", get_max_fitness(populations.populations))
    print_populations(populations)
    selected_population = select(
        populations.populations, r, population_size)
    crossover_population = crossover(
        populations.populations, r, population_size)
    new_population_list.extend(selected_population)

    new_population_list.extend(crossover_population)

    new_population_list = mutation(
        new_population_list, 0.05, population_size)
    new_populations = Populations(new_population_list, population_size)
    calculate_probability(new_populations.populations)
    populations = new_populations
    print("max fitness: ", get_max_fitness(populations.populations))
    print_populations(populations)

    # print_population(new_populations)

    # while True:
    #     populations.populations.sort(
    #         key=lambda x: x.fitness_score, reverse=True)
    #     total_fitness = 0
    #     for population in populations.populations:
    #         total_fitness += population.fitness_score
    #     crossover_array = []
    #     for population in populations.populations:
    #         population.probability = population.fitness_score / total_fitness
    #     new_populations = []
    #     for i in range(100):
    #         parent1 = populations.select_parent()
    #         parent2 = populations.select_parent()
    #         child = parent1.crossover(parent2)
    #         child.mutation()
    #         new_populations.append(child)
    #     populations.populations = new_populations
    #     if populations.populations[0].fitness_score == 0:
    #         return populations.populations[0].state
