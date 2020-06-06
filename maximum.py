import random

def maximum():
    x = y = [0, 1, 2, 3, 4, 5, 6, 7]
    population = [(3, 6, -8), (6, 4, -15), (3, 5, -3), (7, 0, -32),
                    (3, 7, -15), (1, 6, -8), (1, 2, 0), (5, 4, -8),
                    (6, 1, -18), (4, 2, -3)]
    population = sorted(population, key=lambda tup: tup[2], reverse=True)
    qtt = 0
    while population[0][2] != 2:
        qtt += 1
        population = [population[0]] + [population[1]] + [population[2]] + [population[3]]

        # begin new population

        # first row after the cutoff point
        population = generate_population(population, 0, 4)

        # second row after the cutoff point
        population = generate_population(population, 1, 3)

        # third row after the cutoff point
        population = generate_population(population, 2, 2)

        # fourth row after the cutoff point
        population = generate_population(population, 3, 1)

        population = population[4:len(population)]

        # end new population

        # begin mutation

        population = mutation(population, [0, 1])
        population = mutation(population, [2, 3])
        population = mutation(population, [4, 5])
        population = mutation(population, [6, 7])
        population = mutation(population, [8, 9])

        # end mutation
        population = sorted(population, key=lambda tup: tup[2], reverse=True)
    print(qtt)
    print(population)

def generate_population(population, row, count):
    chromosome = binary_size_three(format(population[row][0], 'b')) + binary_size_three(format(population[row][1], 'b'))
        
    for i in range(count):
        item = random.choice(population[0:4])
        item_chromosome = binary_size_three(format(item[1], 'b'))
                
        crossover = chromosome[0:4] + item_chromosome

        x = int(crossover[0:3], 2)
        y = int(crossover[3:6], 2)
        result = 2-(x-2)**2-(y-3)**2
                
        new_item = (x, y, result) # f(x,y)=2–(x–2)^2–(y–3)^2
        population.append((x, y, result))
    return population

def mutation(population, row_array):
    idx_chromosome = [0, 1, 2, 3, 4, 5]
    change_chromosome = [0, 1]

    row = random.choice([0, 1])
    item = population[row]
    del population[row]

    x = item[0]
    y = item[1]
    result = item[2]

    idx = random.choice(idx_chromosome)
    change = random.choice(change_chromosome)

    old_chromosome = binary_size_three(format(x, 'b')) + binary_size_three(format(y, 'b'))
    new_chromosome = old_chromosome[0:idx] + str(change) + old_chromosome[idx+1:7]
        
    new_x = int(new_chromosome[0:3], 2)
    new_y = int(new_chromosome[3:6], 2)
    new_result = 2-(new_x-2)**2-(new_y-3)**2

    population.append((new_x, new_y, new_result))

    return population
    

def binary_size_three(n):
    while len(n) < 3:
        n = '0' + n
    return n

if __name__ == '__main__':
    maximum()
