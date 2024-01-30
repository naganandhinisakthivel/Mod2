def analyze_optimization_results(data_centers, data_chunks, replication_strategy):
    # Calculate average number of replicas per data center
    replicas_per_data_center = {dc: 0 for dc in data_centers}
    for chunk, dc in replication_strategy.items():
        replicas_per_data_center[dc] += 1

    total_replicas = sum(replicas_per_data_center.values())
    average_replicas_per_data_center = total_replicas / len(data_centers)

    # Calculate the percentage of data chunks meeting their replication thresholds
    chunks_meeting_threshold = sum(1 for chunk, dc in replication_strategy.items() if replicas_per_data_center[dc] >= replication_thresholds[chunk])
    percentage_chunks_meeting_threshold = (chunks_meeting_threshold / len(data_chunks)) * 100

    # Calculate the overall system efficiency
    total_capacity = sum(data_center.capacity for data_center in data_centers)
    system_efficiency = total_replicas / total_capacity * 100

    # Display analysis results
    print("\nOptimization Results Analysis:")
    print(f"Average Replicas per Data Center: {average_replicas_per_data_center:.2f}")
    print(f"Percentage of Data Chunks Meeting Replication Thresholds: {percentage_chunks_meeting_threshold:.2f}%")
    print(f"Overall System Efficiency: {system_efficiency:.2f}%")

# Example Usage
if __name__ == "__main__":
    # Assuming previous code is loaded or imported here

    # Set parameters for analysis
    replication_strategy = optimized_replication  # Replace with the actual optimized replication strategy

    # Run analysis on optimization results
    analyze_optimization_results(data_centers, data_chunks, replication_strategy)
