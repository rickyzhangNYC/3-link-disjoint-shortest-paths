# Calculate minimum distances
def calcMinDist(distances,nodesToVisit):
    minDistance = float("INF")
    nextNode = -1
    for i in range(len(distances)):
        if (distances[i] < minDistance) and (i in nodesToVisit):
            minDistance = distances[i]
            nextNode = i
        elif (distances[i] == float("INF") and i not in nodesToVisit):
            break
    return nextNode

# If the source node has no neighbors, return to raise error
def srcNoEdges(matrix, src, columnlength,):
    hasEdge = False
    for j in range(columnlength):
        if matrix[src][j] != 0:
            hasEdge = True
    if hasEdge == False:
        return True

# Append all possible nodes that can be visited (nodes that have any edge connected)
def appendPossibleNodes(matrix, rowlength, columnlength, nodesToVisit):
    for i in range(rowlength):
        hasEdge = False
        for j in range(columnlength):
            if matrix[i][j] != 0:
                hasEdge = True
        if hasEdge == True:
            nodesToVisit.append(i)

# Recursively remove path using parent array
def removePath(matrix, parent, j):
    if parent[j] == -1:
        return
    removePath(matrix,parent, parent[j])
    matrix[j][parent[j]] = 0
    matrix[parent[j]][j] = 0

# Recursively print the path back to root using parent array
def printPath(parent, j):
    if parent[j] == -1 :
        print (j+1, end = " ")
        return
    printPath(parent , parent[j])
    print (j+1, end = " ")
     
# Print the vertices, and distance from path to destination
def printAnswer(matrix,dist, parent,sourceNode,destinationNode):
    src = sourceNode
    print("Vertex \t\tDistance from Source\tPath")
    for i in range(0, len(dist)):
       	if i==destinationNode:
            print("\n%d --> %d \t\t%d \t\t" % (src+1, i+1, dist[i]), end = " "),
            printPath(parent,i)
            removePath(matrix,parent, i)
            print(" ")
            

def dijkstra(matrix, src, dest):
    # Iterators for row and column length
    rowlength = len(matrix)
    columnlength = len(matrix[0])
    # Create an array of all possible points default INF
    distances = [float("INF")]*rowlength
    # Distance to source node is 0 
    distances[src] = 0
    # Nodes to visit next
    nodesToVisit = []
    # Array for parent nodes to keep track of traversal
    parentNodeArray = [-1]*rowlength

    # Check if source node has no edges
    srcNoEdges(matrix, src, columnlength)
    if srcNoEdges(matrix, src, columnlength):
        raise ValueError
    
    # Append initial nodes
    appendPossibleNodes(matrix, rowlength, columnlength, nodesToVisit)
    
    print('Routing Table')
    while nodesToVisit:
    
        # Check for next node to visit
        currentNode = calcMinDist(distances,nodesToVisit)
        # Remove the node from nodes to visit
        nodesToVisit.remove(currentNode)

        # Check every node
        for j in range(columnlength):
            # If current node and target node is connected by edge (!= 0) and it is a not visited node
            if matrix[currentNode][j] and j in nodesToVisit:
                # If the cost from current node to j (target node) and cost of path to current node is less than the previous cost directly to j (target node) then replace cost
                # Also input currentNode as child of j
                if distances[currentNode] + matrix[currentNode][j] < distances[j]:
                    distances[j] = distances[currentNode] + matrix[currentNode][j]
                    parentNodeArray[j] = currentNode

        print(distances)
    printAnswer(matrix, distances,parentNodeArray,src,dest)

def main():
    matrix =[[0,10,2,0,0,0,8],
        [10,0,2,16,2,0,0],
        [2,2,0,8,0,1,0],
        [0,16,8,0,2,6,1],
        [0,2,0,2,0,0,4],
        [0,0,1,6,0,0,1],
        [8,0,0,1,4,1,0]]


    try:
        print ('\nFirst iteration')
        dijkstra(matrix,0,3)

        print ('\nSecond iteration')
        dijkstra(matrix,0,3)

        print ('\nThird iteration')
        dijkstra(matrix,0,3)

    except ValueError:
        print("Error: Source node has no edges.")
        
if __name__ == '__main__':
    main() 