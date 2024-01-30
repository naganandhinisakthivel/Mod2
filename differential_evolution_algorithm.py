import numpy as np

def initialize_population(population_size, num_data_centers):
    return np.random.randint(2, size=(population_size, num_data_centers))

def fitness_function(individual, availability, latency, storage_cost):
    return np.sum(availability * individual - latency * individual - storage_cost * individual)

def generate_mutant(a, b, c, mutation_scale_factor):
    return a + mutation_scale_factor * (b - c)

def perform_crossover(i, mutant, crossover_rate, random_index):
    trial = np.copy(i)
    for j in range(len(i)):
        if np.random.rand() < crossover_rate or j == random_index:
            trial[j] = mutant[j]
    return trial

def optimize_data_placement(population_size, num_generations, crossover_rate, mutation_scale_factor,
                             data_centers, data_chunk_attributes, chunk_size):
   
    num_data_centers = len(data_centers)
    num_data_chunks = len(data_chunk_attributes['availability'])
    
    # Input parameters
    availability = data_chunk_attributes['availability']
    latency = data_chunk_attributes['latency']
    storage_cost = data_chunk_attributes['storage_cost']
    
    # Initialize population
    population = initialize_population(population_size, num_data_centers)
    
    # Differential Evolution Loop
    for generation in range(num_generations):
        for i in range(population_size):
            # Select three distinct individuals a, b, and c
            a, b, c = np.random.choice(population, size=3, replace=False)
            
            # Generate mutant individual
            mutant = generate_mutant(a, b, c, mutation_scale_factor)
            
            # Perform crossover
            random_index = np.random.randint(num_data_centers)
            trial = perform_crossover(population[i], mutant, crossover_rate, random_index)
            
            # Evaluate fitness of the trial individual
            fitness_i = fitness_function(population[i], availability, latency, storage_cost)
            fitness_trial = fitness_function(trial, availability, latency, storage_cost)
            
            # Update population if the trial is better
            if fitness_trial > fitness_i:
                population[i] = trial
                
    # Find the best individual in the population (optimal data placement configuration)
    best_individual = max(population, key=lambda ind: fitness_function(ind, availability, latency, storage_cost))
    
    # Output the best data placement configuration
    best_data_placement = {
        'data_centers': data_centers,
        'data_placement_configuration': best_individual,
    }
    
    return best_data_placement

data_centers = ['DC1', 'DC2', 'DC3']
data_chunk_attributes = {
    'availability': np.array([[0.8, 0.9, 0.7], [0.6, 0.7, 0.5], [0.9, 0.8, 0.6]]),
    'latency': np.array([[10, 20, 15], [15, 25, 20], [12, 18, 22]]),
    'storage_cost': np.array([10, 15, 12]),
}
chunk_size = 1000

result = optimize_data_placement(population_size=50, num_generations=100, crossover_rate=0.8, 
                                  mutation_scale_factor=0.5, data_centers=data_centers, 
                                  data_chunk_attributes=data_chunk_attributes, chunk_size=chunk_size)

print("Best Data Placement Configuration:", result['data_placement_configuration'])
