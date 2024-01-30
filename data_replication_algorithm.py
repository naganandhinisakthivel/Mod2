import heapq

class DataCenterNode:
    def __init__(self, name, capacity, replication_threshold):
        self.name = name
        self.capacity = capacity
        self.replication_threshold = replication_threshold
        self.replicas = []

    def add_replica(self, replica):
        self.replicas.append(replica)

    def remove_replica(self, replica):
        self.replicas.remove(replica)

    def get_total_data_size(self):
        return sum(replica['size'] for replica in self.replicas)

    def exceeds_capacity(self, new_replica_size):
        return self.get_total_data_size() + new_replica_size > self.capacity

class DataChunk:
    def __init__(self, name, popularity, size):
        self.name = name
        self.popularity = popularity
        self.size = size

def initialize_data_centers():
    data_centers = [
        DataCenterNode(name='DC1', capacity=1000, replication_threshold=3),
        DataCenterNode(name='DC2', capacity=800, replication_threshold=2),
        DataCenterNode(name='DC3', capacity=1200, replication_threshold=4),
    ]
    return data_centers

def initialize_data_chunks():
    data_chunks = [
        DataChunk(name='Chunk1', popularity=0.9, size=200),
        DataChunk(name='Chunk2', popularity=0.8, size=150),
        DataChunk(name='Chunk3', popularity=0.7, size=180),
    ]
    return data_chunks

def calculate_replication_score(chunk, data_center):
    # Placeholder for the replication score calculation based on factors like popularity, access patterns, and size.
    return chunk.popularity * 0.5 + (1 - chunk.size / 300) * 0.3 + data_center.replication_threshold * 0.2

def replicate_data(data_centers, data_chunks):
    for chunk in data_chunks:
        replication_scores = [(calculate_replication_score(chunk, data_center), data_center) for data_center in data_centers if not data_center.exceeds_capacity(chunk.size)]
        top_replication_nodes = heapq.nlargest(chunk.replication_threshold, replication_scores, key=lambda x: x[0])

        for score, data_center in top_replication_nodes:
            replica = {'chunk': chunk, 'data_center': data_center, 'size': chunk.size}
            data_center.add_replica(replica)

def calculate_deletion_score(replica):
    # Placeholder for deletion score calculation based on factors like access recency, importance, or value of data.
    return replica['chunk'].popularity * 0.4 + (1 - replica['chunk'].size / 300) * 0.3

def manage_data_center_capacity(data_centers):
    for data_center in data_centers:
        if data_center.exceeds_capacity(0):  # Check if the capacity is exceeded due to new replicas
            replicas_to_remove = sorted(data_center.replicas, key=calculate_deletion_score, reverse=True)

            total_data_size = data_center.get_total_data_size()
            while total_data_size > data_center.capacity:
                replica_to_remove = replicas_to_remove.pop(0)
                data_center.remove_replica(replica_to_remove)
                total_data_size -= replica_to_remove['size']

def serve_data_request(requested_chunk, data_centers):
    for data_center in data_centers:
        local_replicas = [replica for replica in data_center.replicas if replica['chunk'].name == requested_chunk.name]
        if local_replicas:
            print(f"Serve request locally from {data_center.name}")
            return

    # If not available locally, identify the closest data center node with the required data chunk
    closest_data_center = min(data_centers, key=lambda dc: min(latency_map[dc.name][dc2.name] for dc2 in data_centers))
    closest_replica = next(replica for replica in closest_data_center.replicas if replica['chunk'].name == requested_chunk.name)

    print(f"Serve request from closest replica in {closest_data_center.name}")

latency_map = {
    'DC1': {'DC1': 0, 'DC2': 10, 'DC3': 15},
    'DC2': {'DC1': 10, 'DC2': 0, 'DC3': 12},
    'DC3': {'DC1': 15, 'DC2': 12, 'DC3': 0},
}

data_centers = initialize_data_centers()
data_chunks = initialize_data_chunks()

replicate_data(data_centers, data_chunks)
manage_data_center_capacity(data_centers)

# Simulate data request
requested_chunk = data_chunks[0]
serve_data_request(requested_chunk, data_centers)
