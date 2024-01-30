def adaptive_replication_thresholds(data_chunks, replication_thresholds):
    for chunk in data_chunks:
        # Simulate dynamic changes in popularity or access frequency
        dynamic_factor = random.uniform(0.8, 1.2)  # Vary by +/- 20%
        chunk.access_frequency *= dynamic_factor
        # Adjust replication threshold based on access frequency
        adjusted_threshold = int(chunk.access_frequency * 3)  # Adjust according to your specific scaling factor
        replication_thresholds[chunk.name] = max(1, adjusted_threshold)  # Ensure the minimum threshold is 1

    # Display the adjusted replication thresholds
    print("\nAdaptive Replication Thresholds:")
    for chunk_name, threshold in replication_thresholds.items():
        print(f"Data Chunk {chunk_name}: Replication Threshold - {threshold}")
if __name__ == "__main__":
    # Set initial replication thresholds
    initial_replication_thresholds = {f'DataChunk{i+1}': 2 for i in range(len(data_chunks))}

    # Run adaptive replication threshold adjustment
    adaptive_replication_thresholds(data_chunks, initial_replication_thresholds)
