import numpy as np

def sensitivity_analysis(data_centers, data_chunks, latency_matrix, storage_costs, replication_thresholds, capacity_constraints):
    # Vary storage costs for sensitivity analysis
    storage_cost_variations = np.linspace(0.8, 1.2, 5)  # Vary storage costs by +/- 20%

    results = []

    for cost_variation in storage_cost_variations:
        # Adjust storage costs
        adjusted_storage_costs = [cost * cost_variation for cost in storage_costs]

        # Run optimization with adjusted storage costs
        optimized_placement, optimized_replication = optimize_data_placement(data_centers, data_chunks, latency_matrix, adjusted_storage_costs, replication_thresholds, capacity_constraints)

        # Evaluate system performance metrics with adjusted storage costs
        data_availability = calculate_data_availability(data_centers, data_chunks, optimized_replication)
        total_cost = calculate_total_cost(data_centers, data_chunks, latency_matrix, adjusted_storage_costs, optimized_replication)

        # Save results for each variation
        results.append({
            'Storage Cost Variation': cost_variation,
            'Data Availability': data_availability,
            'Total Cost': total_cost
        })

    # Display sensitivity analysis results
    print("\nSensitivity Analysis Results:")
    print("{:<25} {:<20} {:<15}".format("Storage Cost Variation", "Data Availability (%)", "Total Cost"))
    for result in results:
        print("{:<25} {:<20.2f} {:<15.2f}".format(result['Storage Cost Variation'], result['Data Availability'], result['Total Cost']))

if __name__ == "__main__":
    # Assuming previous code is loaded or imported here

    # Set parameters for sensitivity analysis
    sensitivity_analysis(data_centers, data_chunks, latency_matrix, storage_costs, replication_thresholds, capacity_constraints)
