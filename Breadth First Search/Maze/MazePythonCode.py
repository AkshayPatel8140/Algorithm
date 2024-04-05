def hasPath(maze, start, destination):
    def dfs(x, y):
        if visitedList[x][y]:
            return False
        visitedList[x][y] = True
        if [x, y] == destination:
            return True
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_x, next_y = x, y
            while (
                (0 <= next_x + dx < len(maze))
                and (0 <= next_y + dy < len(maze[0]))
                and (maze[next_x + dx][next_y + dy] == 0)
            ):
                next_x += dx
                next_y += dy
            if dfs(next_x, next_y):
                return True
        return False

    visitedList = [[False] * len(maze[0]) for _ in range(len(maze))]
    return dfs(start[0], start[1])


maze1 = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
start1 = [0, 4]
destination1 = [4, 4]
print("\n\n\n\n\n\n")
print("Example 1: \n")
print("Input: \nmaze =", maze1, ", \nstart =", start1, ", \ndestination =", destination1)
print("\nOutput:", hasPath(maze1, start1, destination1))
print("\n")

maze2 = [
    [9, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 2],
    [0, 0, 0, 0, 0],
]
start2 = [0, 4]
destination2 = [3, 2]
print("\n")
print("Example 2: \n")
print("Input: \nmaze =", maze2, ",\nstart =", start2, ",\ndestination =", destination2)
print("Output:", hasPath(maze2, start2, destination2))
print("\n")

maze3 = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0],
]
start3 = [4, 3]
destination3 = [0, 1]
print("\n")
print("Example 1: \n")
print("Input: \nmaze =", maze3, ",\nstart =", start3, ",\ndestination =", destination3)
print("Output:", hasPath(maze3, start3, destination3))
print("\n\n\n\n\n\n")
