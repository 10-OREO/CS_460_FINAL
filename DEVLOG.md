# Development Log – The Torchbearer

**Student Name:** Chris Lepe Tenorio
**Student ID:** 827762800

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – May 14, 2026 3:30 AM: Initial Plan
 
I made sure to read all the instructions. Afterwards, I felt that in order to find the solution, we would need to follow 2 paths. Those are, shortest-path precomputation and search over relic orders. First i will use Djikstras. Next I will store the instances in a dictionary. I feel as though this will be helpful for a fast lookup. I feel that the most difficult part, and the part that I will most likely struggle with is the recursive search as well as the pruning logic. This is mainly because it must avoid skipping the optimal solution.
---

## Entry 2 – May 14, 2026 6:48 AM: Parts 2 - 5

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.
I implemented source selection. I used the entrance as well as every relic chambers as Dijkstra sources. Then I made sure to use a priority queue. This priority queue had `heapq`. Basically what it did was initialized unreachable nodes to infinity. I stored all results in `dist_table`. `dist_table[u][v]` gives the cheapest known cost from u to v. 

---

## Entry 3 – May 14, 2026 9:33 AM: Parts 5 - 6

For my search design, my main priority was choosing the next relic. I made sure tht the base case also added the cost from the last relic to the exit. This was due to the fact that a route might appear to be cheaper that what it really is, if the final exit cost were not included. In order to remedy this, I made sure tht `dist_table[current_loc][exit_node]` was checked when there were no remaining relics. Unreachable paths returned infinity rather than being seen or considcered to be valid moves.
---

## Entry 4 – May 14, 2026 12:15 PM: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

After I finished up with the implementation and made sure that it was complete. The I tested the provided examples in order to see if my work was right. I then confirmed that the expected costs were in fact returned properly and as expected. If I gave my self a bit more time, i feel that I would be able to make some improvements. Those being improving the lower bound. This way, it would account for more of the remaining route. I feel as though that would prune more branches. Pruning more branches would the lead to making algorithm faster for a larger k value. 


---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | .5 |
| Part 2: Precomputation Design | .5 |
| Part 3: Algorithm Correctness | .5 |
| Part 4: Search Design |1|
| Part 5: State and Search Space | 1 |
| Part 6: Pruning | 2 |
| Part 7: Implementation | 2 |
| README and DEVLOG writing | 1 |
| **Total** | 8.5 |