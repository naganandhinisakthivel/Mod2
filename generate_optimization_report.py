import matplotlib.pyplot as plt

def generate_optimization_report(data_centers, data_chunks, latency_matrix, storage_costs, initial_replication_strategy, optimized_replication_strategy):
    # Calculate data availability before and after optimization
    initial_availability = calculate_data_availability(data_centers, data_chunks, initial_replication_strategy)
    optimized_availability = calculate_data_availability(data_centers, data_chunks, optimized_replication_strategy)

    # Calculate cost savings before and after optimization
    initial_cost = calculate_total_cost(data_centers, data_chunks, latency_matrix, storage_costs, initial_replication_strategy)
    optimized_cost = calculate_total_cost(data_centers, data_chunks, latency_matrix, storage_costs, optimized_replication_strategy)
    cost_savings_percentage = ((initial_cost - optimized_cost) / initial_cost) * 100

    # Calculate network latency reduction before and after optimization
    initial_latency = calculate_total_network_latency(data_centers, data_chunks, latency_matrix, initial_replication_strategy)
    optimized_latency = calculate_total_network_latency(data_centers, data_chunks, latency_matrix, optimized_replication_strategy)
    latency_reduction_percentage = ((initial_latency - optimized_latency) / initial_latency) * 100

    # Display key metrics
    print("Optimization Report:")
    print(f"Initial Data Availability: {initial_availability}%")
    print(f"Optimized Data Availability: {optimized_availability}%")
    print(f"Cost Savings: {cost_savings_percentage:.2f}%")
    print(f"Network Latency Reduction: {latency_reduction_percentage:.2f}%")

    # Visualize data availability changes
    visualize_data_availability(data_chunks, initial_replication_strategy, optimized_replication_strategy)

    # Visualize network latency changes
    visualize_network_latency(data_chunks, latency_matrix, initial_replication_strategy, optimized_replication_strategy)

def calculate_data_availability(data_centers, data_chunks, replication_strategy):
    total_replicas = sum(replication_strategy.values())
    total_possible_replicas = len(data_centers) * len(data_chunks)
    data_availability = (total_replicas / total_possible_replicas) * 100
    return data_availability

def calculate_total_cost(data_centers, data_chunks, latency_matrix, storage_costs, replication_strategy):
    total_cost = sum(storage_costs[i] * replication_strategy[f'DataChunk{i+1}'] for i in range(len(data_chunks)))
    for i in range(len(data_chunks)):
        total_cost += replication_strategy[f'DataChunk{i+1}'] * sum(latency_matrix[i][j] for j in range(len(data_centers)))
    return total_cost

def calculate_total_network_latency(data_centers, data_chunks, latency_matrix, replication_strategy):
    total_latency = sum(replication_strategy[f'DataChunk{i+1}'] * sum(latency_matrix[i][j] for j in range(len(data_centers))) for i in range(len(data_chunks)))
    return total_latency

def visualize_data_availability(data_chunks, initial_replication_strategy, optimized_replication_strategy):
    chunk_names = [f'DataChunk{i+1}' for i in range(len(data_chunks))]
    initial_replicas = [initial_replication_strategy[chunk] for chunk in chunk_names]
    optimized_replicas = [optimized_replication_strategy[chunk] for chunk in chunk_names]

    plt.bar(chunk_names, initial_replicas, color='blue', label='Initial Replicas')
    plt.bar(chunk_names, optimized_replicas, color='green', label='Optimized Replicas', alpha=0.7)
    plt.xlabel('Data Chunks')
    plt.ylabel('Number of Replicas')
    plt.title('Data Availability Comparison Before and After Optimization')
    plt.legend()
    plt.show()

def visualize_network_latency(data_chunks, latency_matrix, initial_replication_strategy, optimized_replication_strategy):
    chunk_names = [f'DataChunk{i+1}' for i in range(len(data_chunks))]
    initial_latencies = [sum(latency_matrix[i][j] for j in range(len(data_centers))) * initial_replication_strategy[chunk] for i, chunk in enumerate(chunk_names)]
    optimized_latencies = [sum(latency_matrix[i][j] for j in range(len(data_centers))) * optimized_replication_strategy[chunk] for i, chunk in enumerate(chunk_names)]

    plt.bar(chunk_names, initial_latencies, color='blue', label='Initial Network Latency')
    plt.bar(chunk_names, optimized_latencies, color='green', label='Optimized Network Latency', alpha=0.7)
    plt.xlabel('Data Chunks')
    plt.ylabel('Total Network Latency')
    plt.title('Network Latency Comparison Before and After Optimization')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Assuming previous code is loaded or imported here

    # Set initial replication strategy
    initial_replication_strategy = {f'DataChunk{i+1}': 2 for i in range(len
