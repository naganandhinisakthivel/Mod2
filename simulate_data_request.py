def simulate_data_request(data_centers, latency_map, requested_chunk):
    closest_data_center = identify_closest_data_center(requested_chunk, data_centers, latency_map)
    
    if closest_data_center != -1:
        print(f"Simulating data request for {requested_chunk.name}:")
        print(f"Serve request from the closest replica in {data_centers[closest_data_center].name}")
    else:
        print(f"No suitable data center with the required data chunk ({requested_chunk.name}) is available.")

if __name__ == "__main__":
    # Assuming previous code is loaded or imported here
    
    # Simulate data request for a specific chunk
    requested_chunk = data_chunks[2]  # Change the index as needed
    simulate_data_request(data_centers, latency_map, requested_chunk)
