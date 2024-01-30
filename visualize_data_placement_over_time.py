import seaborn as sns
import matplotlib.pyplot as plt

def visualize_data_placement_over_time(data_centers, data_chunks, replication_strategies, iterations):
    # Prepare data for heatmap
    data_matrix = []

    for iteration in range(iterations):
        replication_strategy = replication_strategies[iteration]
        row = [replication_strategy[f'DataChunk{i+1}'] for i in range(len(data_chunks))]
        data_matrix.append(row)

    # Create a heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(data_matrix, cmap="viridis", annot=True, fmt='d', xticklabels=[f'DataChunk{i+1}' for i in range(len(data_chunks))],
                yticklabels=[f'Iteration {i+1}' for i in range(iterations)])
    plt.title('Data Placement and Replication Strategies Over Time')
    plt.xlabel('Data Chunks')
    plt.ylabel('Iterations')
    plt.show()


if __name__ == "__main__":
    num_iterations = 5
    replication_strategies_over_time = []

    # Simulate data replication over multiple iterations
    for iteration in range(num_iterations):
        # Run optimization or replication logic for each iteration
        optimized_placement, optimized_replication = optimize_data_placement(data_centers, data_chunks, latency_matrix, storage_costs, replication_thresholds, capacity_constraints)
        replication_strategies_over_time.append(optimized_replication.copy())

    # Visualize data placement and replication over time
    visualize_data_placement_over_time(data_centers, data_chunks, replication_strategies_over_time, num_iterations)
