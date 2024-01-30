import random

def simulate_dynamic_scenario(data_centers, data_chunks, latency_matrix, replication_strategy, simulation_duration):
    for _ in range(simulation_duration):
        # Simulate dynamic changes in data access patterns (randomly update access frequencies)
        for chunk in data_chunks:
            chunk.access_frequency = random.uniform(0.1, 1.0)

        # Print updated access frequencies
        print("\nSimulating dynamic changes in data access patterns:")
        for chunk in data_chunks:
            print(f"Data Chunk {chunk.name}: Access Frequency - {chunk.access_frequency}")

        # Simulate dynamic updates in replication strategy based on access patterns
        updated_replication_strategy = {}
        for chunk in data_chunks:
            if chunk.access_frequency > replication_strategy[chunk.name]:
                updated_replication_strategy[chunk.name] = min(replication_strategy[chunk.name] + 1, len(data_centers))
            else:
                updated_replication_strategy[chunk.name] = max(replication_strategy[chunk.name] - 1, 1)

        # Print updated replication strategy
        print("\nUpdating replication strategy based on access patterns:")
        for chunk_name, replicas in updated_replication_strategy.items():
            print(f"Data Chunk {chunk_name}: Replicas - {replicas}")

if __name__ == "__main__":
    # Assuming previous code is loaded or imported here

    # Initialize replication strategy (number of replicas for each data chunk)
    initial_replication_strategy = {f'DataChunk{i}': 2 for i in range(1, 4)}

    # Set simulation duration
    simulation_duration = 5

    # Run dynamic scenario simulation
    simulate_dynamic_scenario(data_centers, data_chunks, latency_matrix, initial_replication_strategy, simulation_duration)
