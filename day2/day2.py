safe = 0

with open('day2/day2.txt', 'r') as file:
    for line in file:
        levels = line.strip().split(' ')

        # Check the difference between each one
        max_diff = float('-inf')
        min_diff = float('inf')

        increasing = int(levels[0]) < int(levels[1])
        FOLLOWS_ORDER = True

        for i in range(1, len(levels)):
            max_diff = max(max_diff, abs(int(levels[i-1]) - int(levels[i])))
            min_diff = min(min_diff, abs(int(levels[i-1]) - int(levels[i])))

            if i >= 2:
                if increasing and int(levels[i]) < int(levels[i-1]):
                    FOLLOWS_ORDER = False
                elif (increasing == False) and (int(levels[i]) > int(levels[i-1])):
                    FOLLOWS_ORDER = False
        
        if max_diff > 3 or min_diff < 1:
            continue

        if FOLLOWS_ORDER: 
            safe += 1

def test(levels):
    print(levels)        

    # Check the difference between each one
    max_diff = float('-inf')
    min_diff = float('inf')

    increasing = levels[0] < levels[1]
    print("Increasing: ", increasing)
    FOLLOWS_ORDER = True

    for i in range(1, len(levels)):
        max_diff = max(max_diff, abs(int(levels[i-1]) - int(levels[i])))
        min_diff = min(min_diff, abs(int(levels[i-1]) - int(levels[i])))

        if i >= 2:
            if increasing and levels[i] < levels[i-1]:
                FOLLOWS_ORDER = False
            elif (increasing == False) and (int(levels[i]) > int(levels[i-1])):
                FOLLOWS_ORDER = False
    
    print("Max diff found: ", max_diff)
    print("Min diff fouund: ", min_diff)
    
    print("Follows order after: ", FOLLOWS_ORDER)
    print("                    ")
    
    if max_diff > 3 or min_diff < 1:
        return

    if FOLLOWS_ORDER: 
        print("this is safe!")

print(safe)


            

