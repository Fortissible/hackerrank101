#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

# CHANGE LOGIC TO SEARCH EVERY OBSTACLE ON PATH DIRECTION
# THEN SELECT THE CLOSEST ONE TO QUEEN, THEN COUNT THE DIFF BETWEEN QUEEN AND OBSTACLE
def countBlockedScore(n, r_q, c_q, r_o, c_o):
    countedBlock = 0
    direction = -1
    if (r_q - r_o == c_q - c_o):
        # Horizontal obstacle check
        print("triggered diagonal")
        
        # TOP LEFT OBSTACLE
        if r_q > r_o and c_q > c_o:
            countedBlock += min(r_o, c_o)
            direction = 4
        # TOP RIGHT OBSTACLE
        elif r_q > r_o and c_o > c_q:
            countedBlock += min(r_o, n-c_o+1)
            direction = 5
        # BOTTOM RIGHT OBSTACLE
        elif r_o > r_q and c_o > c_q:
            countedBlock += min(n-r_o+1, n-c_o+1)
            direction = 6
        # BOTTOM LEFT OBSTACLE
        elif r_o > r_q and c_q > c_o:
            countedBlock += min(n-r_o+1, c_o)
            direction = 7
            
    elif (c_q == c_o):
        # Vertical obstacle check
        print("triggered vertical")
        
        # TOP OBSTACLE
        if r_q > r_o:
            countedBlock += r_o
            direction = 0
        # BOTTOM OBSTACLE
        else:
            countedBlock += n-r_o+1
            direction = 2
        
    elif (r_q == r_o):
        # Horizontal obstacle check
        print("triggered horizontal")
        
        # LEFT OBSTACLE
        if c_q > c_o:
            countedBlock += c_o
            direction = 3
        # RIGHT OBSTACLE
        else:
            countedBlock += n-c_o+1
            direction = 1
            
    print(f"direction {direction} with total block {countedBlock}")
    return direction, countedBlock
    
def countAllScore(n, r_q, c_q,):
    left = c_q-1
    right = n-c_q
    top = r_q-1
    bottom = n-r_q
    top_left = min(top, left)
    top_right = min(top, right)
    bottom_left = min(bottom, left)
    bottom_right = min(bottom, right)
    return left+right+top+bottom+top_left+top_right+bottom_left+bottom_right

def queensAttack(n, k, r_q, c_q, obstacles):
    queen_all_score = countAllScore(n, r_q, c_q)
                  # ^, >, v, <, <^, ^>, v>, v<
    blockedScores = [0, 0, 0, 0, 0, 0, 0, 0]
    for obstacle in obstacles:
        print(f"Obstacle at: {obstacle[0]}, {obstacle[1]}")
        direction, countedBlock = countBlockedScore(
            n, r_q, c_q, obstacle[0], obstacle[1]
        )
        if direction > -1:
            blockedScores[direction] = max(blockedScores[direction], countedBlock)
    print(f"Total queen attack score: {queen_all_score}")
    print(f"Total obscructed path: {blockedScores}")
    for blockedScore in blockedScores:
        queen_all_score -= blockedScore
    return queen_all_score

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)