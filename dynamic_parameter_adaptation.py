import time
import random

def dynamic_parameter_adaptation(data_chunks, replication_thresholds, adaptation_duration):
    # Simulate dynamic changes in data popularity
    start_time = time.time()

    while time.time() - start_time < adaptation_duration:
        # Simulate data popularity changes
        for chunk in data_chunks:
            popularity_change = random.uniform(-0.2, 0.2)  # Vary popularity by +/- 20%
            chunk.access_frequency *= (1 + popularity_change)

        # Adjust replication thresholds based on updated popularity
        for chunk in data_chunks:
            adjusted_threshold = int(chunk.access_frequency * 3)  # Adjust according to your specific scaling factor
            replication_thresholds[chunk.name] = max(1, adjusted_threshold)  # Ensure the minimum threshold is 1

        # Run optimization with the adapted replication thresholds
        optimized_placement, optimized_replication = optimize_data_placement(data_centers, data_chunks, latency_matrix, storage_costs, replication_thresholds, capacity_constraints)

        # Display dynamic adaptation results
        print("\nDynamic Parameter Adaptation:")
        print(f"Replication Thresholds After Adaptation: {replication_thresholds}")

        analyze_optimization_results(data_centers, data_chunks, optimized_replication)

if __name__ == "__main__":
    # Assuming previous code is loaded or imported here

    # Set parameters for dynamic adaptation
    adaptation_duration = 60  # Adaptation duration in seconds

    # Run dynamic adaptation
    dynamic_parameter_adaptation(data_chunks, replication_thresholds, adaptation_duration)
