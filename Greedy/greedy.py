# Greedy Algorithm

# List of states we want to cover
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# Keys are station names and values are the states they cover
stations = {
    "kone": set(["id", "nv", "ut"]),
    "ktwo": set(["wa", "id", "mt"]),
    "kthree": set(["or", "nv", "ca"]),
    "kfour": set(["nv", "ut"]),
    "kfive": set(["ca", "az"])
}

# Final set of stations
final_stations = set()

# Loop until states_needed is empty
while states_needed:
    best_station = None
    states_covered = set()
    
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    # Remove the covered states and add the best station
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
