# Shortest Path

Shortest path algorithms are core graph theory algorithms. Dijkstra's single-source shortest path is a must-master—essentially an improved BFS algorithm. Save the template for quick use in exams.

## Dijkstra Algorithm Template

```python
import heapq
from typing import List

class State:
    # Current node ID
    def __init__(self, node: int, distFromStart: int):
        self.node = node
        # Minimum path weight from the start node s to the current node
        self.distFromStart = distFromStart

    # Define comparison for min-heap
    def __lt__(self, other: "State") -> bool:
        return self.distFromStart < other.distFromStart

# Input the weighted graph (without negative weight edges) graph and the starting node src
# Return the minimum path weight from the starting node src to other nodes
def dijkstra(graph: Graph, src: int) -> List[int]:
    # Record the minimum path weight from the starting node src to other nodes
    # distTo[i] represents the minimum path weight from the starting node src to node i
    distTo: List[int] = [float('inf')] * graph.size()

    # Priority queue, nodes with smaller distFromStart are in front
    pq: List[State] = []

    # Start BFS from the starting node src
    heapq.heappush(pq, State(src, 0))
    distTo[src] = 0

    while pq:
        state = heapq.heappop(pq)
        curNode = state.node
        curDistFromStart = state.distFromStart

        if distTo[curNode] < curDistFromStart: # [!code highlight:5]
            # In Dijkstra's algorithm, the queue may contain duplicate nodes state
            # So it is necessary to check when the element leaves the queue to remove the worse duplicate nodes
            continue

        for e in graph.neighbors(curNode):
            nextNode = e.to
            nextDistFromStart = curDistFromStart + e.weight

            if distTo[nextNode] <= nextDistFromStart:
                continue

            # [!code highlight:6]
            # Add nextNode node to the priority queue
            heapq.heappush(pq, State(nextNode, nextDistFromStart))
            # Record the minimum path weight from the starting node to the nextNode node
            distTo[nextNode] = nextDistFromStart

    return distTo
```

## Leetcode Exercise

- '743. Network Delay Time'
- '1631. Path With Minimum Effort'
- '1514. Path with Maximum Probability'
- '787. Cheapest Flights Within K Stops'
