import heapq
lines = []

with open('day1/day1.txt', 'r') as file:
    for line in file:
        lines.append(line.strip().split('   '))

heap_right = []
heap_left = []

for val in lines:
    heapq.heappush(heap_right, int(val[1]))
    heapq.heappush(heap_left, int(val[0]))

res = 0

while heap_left and heap_right:
    res += abs(int(heapq.heappop(heap_right)) - int(heapq.heappop(heap_left)))

print(res)    
