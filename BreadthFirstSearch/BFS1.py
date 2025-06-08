# Breadth-First Search Algorithm: Workflow below
# 1. Keep a queue containing the people to check 2. Pop a person off the queue
# 3. Check if this person is a mango seller. 4a. No -> Add all their mangos to the queue
# 4b. Yes -> You're done. 5. Loop!

# Mapping a node to its out-neighbors, not everyone has an in-neighbor
# Directed graphs (bidirectional), Undirected Graphs (Unidirectional)
from collections import deque

# Mapping a node to its out-neighbors
graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

# Function to check if someone is a mango seller
def person_is_seller(name):
    return name[-1] == 'm'  # A person is a seller if their name ends with 'm'

# Breadth-First Search implementation
def search():
    search_queue = deque()  # Create queue
    search_queue += graph["you"]  # Start with your immediate connections
    checked = set()  # Track checked people to avoid infinite loops

    while search_queue:
        person = search_queue.popleft()  # Remove first person in queue

        if person not in checked:  # Check only if not visited
            if person_is_seller(person):  
                print(person + " is a mango seller!")
                return True  # Found the seller!

            search_queue += graph[person]  # Add their out-neighbors
            checked.add(person)  # Mark them as checked

    return False  # If queue is empty and no seller was found


 
