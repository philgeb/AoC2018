grid_serial_number = 2187

grid = [[0 for _ in range(300)] for _ in range(300)]

# stores the sums of sub-squares for faster computation in next higher square_size
# starts with sums of all 2x2 sub-grids, then 3x3, and so on, values from previous iteration are overwritten
# to store the sum of all 2x2 sub-grids we need 299*299 entires, for 3x3 298*298, and so on
sub_grid_sums = [[0 for _ in range(299)] for _ in range(299)]

# initial grid values
for x in range(300):
    for y in range(300):
        rackID = x + 11 # 11 because array starts at 0
        power_level = (rackID * (y + 1) + grid_serial_number) * rackID
        grid[x][y] = ((power_level // 100) % 10) - 5

# compute 2x2 sub-grids sums
for x in range(299):
    for y in range(299):
        sub_grid_sums[x][y] = grid[x][y] + grid[x+1][y] + grid[x][y+1] + grid[x+1][y+1]

def total_power(top_left_x, top_left_y, square_size):
    # square_size denotes length of the the square
    total = sub_grid_sums[top_left_x][top_left_y]
    for x in range(top_left_x, top_left_x + square_size):
        total += grid[x][top_left_y + square_size - 1]
    for y in range(top_left_y, top_left_y + square_size - 1):
        total += grid[top_left_x + square_size - 1][y]
    sub_grid_sums[top_left_x][top_left_y] = total
    return total

def part1():
    max_total_power = -9999
    max_x = -1
    max_y = -1
    for x in range(0, 298):
        for y in range(0, 298):
            curr_total = total_power(x,y,3)
            if curr_total > max_total_power:
                max_total_power = curr_total
                (max_x, max_y) = (x, y)

    # +1 for x and y because the matrix starts at 1,1 in AOC
    print(str(max_x + 1) + "," + str(max_y + 1))

def part2():
    max_total_power = -9999
    max_x = -1
    max_y = -1
    max_size = -1
    for size in range(3, 300):
        for x in range(300 - size + 1):
            for y in range(300 - size + 1):
                curr_total = total_power(x,y,size)
                if curr_total > max_total_power:
                    max_total_power = curr_total
                    (max_x, max_y, max_size) = (x, y, size)
        print(size) # check current progress

    # +1 for x and y because the matrix starts at 1,1 in AOC
    print(str(max_x + 1) + "," + str(max_y + 1) + "," + str(max_size))

part2()