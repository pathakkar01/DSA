def isSafe(row, col, m, n, visited):
    print("xyz1", row, col)
    if row == -1 or row == n or col == -1 or col== n or visited[row][col] or m[row][col] == 0 :
        print(visited)
        print(False)
        return False
    print(True)
    return True
def printPath(row, col, m, possiblePath, currPath, visited) :
    if row == -1 or row == len(m) or col == -1 or visited[row][col] or m[row][col] == 0 :
        print("xyz")
        return 
    if row == (len(m)-1) and col == (len(m[0])-1) :
        print(currPath)
        possiblePath.append(currPath)
        return 
    visited[row][col] = True

    if isSafe(row+1, col, m, 2, visited) :
        print(currPath)

        currPath.append("D")
        printPath(row+1, col, m, possiblePath, currPath, visited)
        currPath.pop()
    if isSafe(row-1, col, m, 2, visited):
        print(currPath)
        currPath.append("U")
        printPath(row-1, col, m, possiblePath, currPath, visited)
        currPath.pop()
    if isSafe(row, col+1, m, len(m), visited):
        print(currPath)
        currPath.append("R")
        printPath(row, col+1, m, possiblePath, currPath, visited)
        currPath.pop()
    if isSafe(row, col-1, m, len(m), visited):
        print(currPath)
        currPath.append("L")
        printPath(row, col-1, m, possiblePath, currPath, visited)
        currPath.pop()
    visited[row][col] = False
m = [ [1,1],
      [0,1]]
possiblePath = []
currPath = []
visited = [[False]*2]*2
print(printPath(0, 0, m, possiblePath, currPath, visited))
#print(possiblePath)
print(len(m))