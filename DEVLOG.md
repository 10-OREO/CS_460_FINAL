# Development Log – The Torchbearer

**Student Name:** Chris Lepe Tenorio
**Student ID:** 827762800

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – May 13, 2026 1:30 AM: Initial Plan
 
I made sure to read all the instructions. Afterwards, I felt that in order to find the solution, we would need to follow 2 paths. Those are, shortest-path precomputation and search over relic orders. First i will use Djikstras. Next I will store the instances in a dictionary. I feel as though this will be helpful for a fast lookup. I feel that the most difficult part, and the part that I will most likely struggle with is the recursive search as well as the pruning logic. This is mainly because it must avoid skipping the optimal solution.
---

## Entry 2 – May 13, 2026 6:48 AM: Parts 2 - 5

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.
I implemented source selection. I used the entrance as well as every relic chambers as Dijkstra sources. Then I made sure to use a priority queue. This priority queue had `heapq`. Basically what it did was initialized unreachable nodes to infinity. I stored all results in `dist_table`. `dist_table[u][v]` gives the cheapest known cost from u to v. 

---

## Entry 3 – [Date]: [Short description]

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis |.5|
| Part 2: Precomputation Design |.5|
| Part 3: Algorithm Correctness |.5|
| Part 4: Search Design |1|
| Part 5: State and Search Space |1|
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |