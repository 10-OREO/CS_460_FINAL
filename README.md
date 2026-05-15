# The Torchbearer

**Student Name:** Chris Lepe Tenorio
**Student ID:** 827762800
**Course:** CS 460 – Algorithms | Spring 2026
---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
  A single shortest path run from S is not sufficient since it only gives us the cost of the entrance of each node. It is unable to decide in what order to visit the relics while still reaching T.

- **What decision remains after all inter-location costs are known:**
  The order that relics must be visited in is the structural desicion that remains

- **Why this requires a search over orders (one sentence):**
  The reason why this is a search over orders is due to the fact that we are able to produce different fuel cost due to differing orders and sequences of relics to visit

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
|---|---|
| Entrance node S | This is where the route begins. This means that distances from S to any other relic are needed |
| Relic Chamber | The planenr must know the cheapest possible cost to every remaining relic as well as the exit |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | dist_tabl |
| What the keys represent | the inner key represents an destination node, while the outer key represents a source node |
| What the values represent | the values represent hte cheapest cost  |
| Lookup time complexity | O(1)|
| Why O(1) lookup is possible | hash table lookup is used |

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** k + 1
- **Cost per run:** O(m log n)
- **Total complexity:** O((k + 1)m log n)
- **Justification (one line):** from S, dijkstra is ran once. it is then ran once again for every k relic

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  Finalized nodes have their shortest path from the source

- **For nodes not yet finalized (not in S):**
  Nonfinalized nodes store the best and shortest known path using finalized nodes

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  The invariant holds before the first iteration since the source begins at 0 and the other nodes at infinity

- **Maintenance : why finalizing the min-dist node is always correct:**
  finalizing the min-dist node is always correct since nonnegative edge weights make sure that the minimum unfinalized node are unable to improve later on.

- **Termination : what the invariant guarantees when the algorithm ends:**
  The invariant guarantees that all reachable nodes having the correct shortest path distance

### Part 3c: Why This Matters for the Route Planner

This matters for the Route Planner since the planner relies on the correct distances in order to compare the complete relic routes in an accurate fashion.

---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** the reason why greedy fails is because picking the cheapest immediate relic can result in being more expensive later on
- **Counter-example setup:** S -> B = 1, S -> C = 2, B -> D = 3, C -> D = 1, D -> T = 2
- **What greedy picks:** Greddy will choose B since it happens to be the closest
- **What optimal picks:** S -> C -> D -> T. this has a cost of 5.
- **Why greedy loses:** Greedy loses since it will need to explore other relic order in order to be able to find a route that happens to be optimal

### What the Algorithm Must Explore

- it must explore other orders. this is because it will not always choose the best route if it chooses the nest local choice

---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | current_loc | node | this is just the current location for where our recursive search happens to be|
| Relics already collected | relics_visited_order | list[node] |  this is just the list of relics in order|
| Fuel cost so far | cost_so_far | float | this is the cost of fuel by the current route |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: O(1)|
| Operation: mark a relic as collected | Time complexity: O(1) |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) |
| Why this structure fits | this structure fits since fast remove and add checks are supported while we do recursive backtracking|

### Part 5c: Worst-Case Search Space

- **Worst-case number of orders considered:** k!
- **Why:** this is the worst case since the algorithm could face having to consider all alterations of k relics

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

- **What is tracked:** what is being tracked is the relic order that happend to produce the best complete route 
- **When it is used:** it is used after a full route to the exit was completed as well as prior to a branch expanding.
- **What it allows the algorithm to skip:** the algorithm skips due to routes that happend to be unable to be the current best solution

### Part 6b: Lower Bound Estimation

- **What information is available at the current state:** it knows thew current location, as well as the remainig relics, exit node, shortest path distances, and the cost so far
- **What the lower bound accounts for:** it accounts for adding the cheapest posible next move and the current cost
- **Why it never overestimates:** since it is optimistic, it is unable to be larger than the remainder of the rout cost

### Part 6c: Pruning Correctness

- It is safe since a branch will be  abandoned only when the optimistic lower bound happens to be at least as large as the best complete route that was found so far


---

## References

- Lectures, and Lecture Notes