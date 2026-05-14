"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: ___________________________
Student ID:   ___________________________

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return """
    - A single shortest path run from S is not sufficient since it only gives us the cost of the entrance of each node. It is unable to decide in what order to visit the relics while still reaching T. 
    - The order that relics must be visited in is the structural desicion that remains
    - The reason why this is a search over orders is due to the fact that we are able to produce different fuel cost due to differing orders and sequences of relics to visit 
    """



# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    # i started at the spawn as the first source
    sources = [spawn]
    # i then made sure that all the relics are included
    for relic in relics:
        if relic not in sources:
            sources.append(relic)
    return sources


def run_dijkstra(graph, source):
    # i initialied all nodes to infinity
    dist = {}

    for node in graph:
        dist[node] = float('inf')

    # this means that hte distance from the source to itself is 0
    dist[source] = 0

    # the priority q will store the current distane and current node
    priority_q = [(0, source)]

    while priority_q:
        # this just gets the node with the smallest know distance
        current_distance, node = heapq.heappop(priority_q)

        # this skips all the q entries that happen to be outdated
        if current_distance > dist[node]:
            continue
        
        # this is used to explore neighbors :)
        for neighbor, cost in graph[node]:
            # this is basically the cost to reachthe neighbor using  
            new_cost = current_distance + cost

            if new_cost < dist[neighbor]:
                # this makes sure to update the shortest know distance
                dist[neighbor] = new_cost
                # the updated distance is then pushed into heap
                heapq.heappush(priority_q, (new_cost, neighbor))

    return dist

def precompute_distances(graph, spawn, relics, exit_node):

    dist_table = {}

    # this makes sure to select all hte nodes that we should run dijkstra from
    sources = select_sources(spawn, relics, exit_node)
    
    # dijkstra is ran from every source
    for source in sources:
        dist_table[source] = run_dijkstra(graph, source)

    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return """
    3a. 
        - Finalized nodes have their shortest path from the source
        - Nonfinalized nodes store the best and shortest known path using finalized nodes
    3b. 
        - The invariant holds before the first iteration since the source begins at 0 and the other nodes at infinity
        - finalizing the min-dist node is always correct since nonnegative edge weights make sure that the minimum unfinalized node are unable to improve later on.
        - The invariant guarantees that all reachable nodes having the correct shortest path distance
    3c. This matters for the Route Planner since the planner relies on the correct distances in order to compare the complete relic routes in an accurate fashion.
    """


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return """
    - The failure mode: The reason why greedy fails is because picking the cheapest immediate relic can result in being more expensive later on
    - Counter-example setup: S -> B = 1, S -> C = 2, B -> D = 3, C -> D = 1, D -> T = 2 
    - What greedy picks: Greddy will choose B since it happens to be the closest
    - What optimal picks: S -> C -> D -> T. this has a cost of 5.
    - Why greedy loses: Greedy loses since it will need to explore other relic order in order to be able to find a route that happens to be optimal
    """


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    # stores the best solution
    # best[0] means best cost and best[1] means best relic order
    best = [float('inf'), []]
    relics_remaining = set(relics)

    # this is just a recursive search
    _explore(dist_table, spawn, relics_remaining,[], 0, exit_node, best)

    return best[0], best[1]


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    
    # this check to see if all relics were collected
    if not relics_remaining:
        # this is just the cost it takes to go from the current location to the exit
        exit_cost = dist_table[current_loc].get(exit_node, float('inf'))

        # this checks that if it is unable to reach the exit, then to abandon that path or branch
        if exit_cost == float('inf'):
            return
        
        # this basically just calculates the cost of the entire route
        total_cost = cost_so_far + exit_cost

        # this makes sure that when a better solution is found to make sure to update it
        if total_cost < best[0]:
            best[0] = total_cost
            best[1] = relics_visited_order.copy()

        return
    
    # this finds rthe next possible cheapest move
    min_next = float('inf')

    for relic in relics_remaining:
        travel_cost = dist_table[current_loc].get(relic, float('inf'))

        min_next = min(min_next, travel_cost)
    
    lower_bound = cost_so_far + min_next

    """
    it is safe since lower_bound happens to assume the cheapest possible continuation.
    Due to this, it will not overestimate its cost for the remainder of the route
    no completetion of this branch would be able to be optimal if the optimistic value is unable to be beaten
    """
    if lower_bound >= best[0]:
        return

    # this is here to continue to try the remaining relics
    for relic in list(relics_remaining):
        # this is to store the cost to reach this relic
        travel_cost = dist_table[current_loc].get(relic,float('inf'))

        # this is basically just here to skip the relics that are unreachable
        if travel_cost == float('inf'):
            continue

        # relics are being marked as collected
        relics_remaining.remove(relic)

        # this is used for ading relics to the routes
        relics_visited_order.append(relic)

        _explore(dist_table, relic, relics_remaining, relics_visited_order, cost_so_far + travel_cost, exit_node, best)

        # thi is used to remove relics from the route
        relics_visited_order.pop()

        # this is used for adding relics to the remaing sets
        relics_remaining.add(relic)


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):

    # this makes sure to build the shortes path lookup table
    dist_table = precompute_distances(graph, spawn, relics, exit_node)

    # this finds the optimal relic order
    return find_optimal_route(dist_table, spawn, relics, exit_node)



# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()