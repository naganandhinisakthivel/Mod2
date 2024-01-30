def remove_replica_with_highest_deletion_score(replicas, deletion_scores, capacity):
    # Calculate deletion score for each replica
    deletion_score_mapping = {i: deletion_scores[i] for i in range(len(replicas))}
    
    # Sort replicas based on their deletion scores in descending order
    sorted_replicas = sorted(deletion_score_mapping, key=deletion_score_mapping.get, reverse=True)
    
    # Initialize variables
    total_data_size = sum(replica['size'] for replica in replicas)
    current_replica_index = 0
    
    # Remove replicas to meet capacity constraint
    while total_data_size > capacity and current_replica_index < len(sorted_replicas):
        replica_to_remove_index = sorted_replicas[current_replica_index]
        
        # Remove the replica at replica_to_remove_index
        total_data_size -= replicas[replica_to_remove_index]['size']
        replicas.pop(replica_to_remove_index)
        
        # Increment current_replica_index to consider the next replica
        current_replica_index += 1
    
    return replicas

# Example Usage
if __name__ == "__main__":
    # Sample data
    replicas = [
        {'size': 100, 'deletion_score': 0.8},
        {'size': 120, 'deletion_score': 0.6},
        {'size': 80, 'deletion_score': 0.9},
        {'size': 150, 'deletion_score': 0.7},
    ]
    
    # Extract deletion scores
    deletion_scores = [replica['deletion_score'] for replica in replicas]
    
    # Set capacity constraint
    capacity = 300
    
    # Apply the algorithm
    updated_replicas = remove_replica_with_highest_deletion_score(replicas, deletion_scores, capacity)
    
    # Display the result
    print("Replicas after removal:", updated_replicas)
