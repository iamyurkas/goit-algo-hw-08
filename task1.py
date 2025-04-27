import heapq

def min_cost_to_connect(cables):
    if not cables:
        return 0

    heapq.heapify(cables)  # make mini-heap
    total_cost = 0

    while len(cables) > 1:
        # start with smallest
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second

        total_cost += first + second

        # return the new cable to heap
        heapq.heappush(cables, cost)

    return total_cost

cables = [4, 3, 2, 6]
print("Minimal spendings:", min_cost_to_connect(cables))