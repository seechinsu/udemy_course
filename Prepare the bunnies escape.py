import cProfile
import sys

# maze = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

maze = [[0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]]

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous


def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        print v.previous
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return


import heapq


def dijkstra(aGraph, start, target):
    #print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(), v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        # for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                'updated : current = %s next = %s new_dist = %s' \
                      % (current.get_id(), next.get_id(), next.get_distance())
            else:
                'not updated : current = %s next = %s new_dist = %s' \
                      % (current.get_id(), next.get_id(), next.get_distance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(), v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)

def legalCoord(i,j):
    if i <= (len(maze)-1) and j <= (len(maze)-1):
        return True
    else:
        return False


def adjacent_to((maze_dim, point)):
    neighbors = (
        (point[0] - 1, point[1]),
        (point[0], point[1] - 1),
        (point[0], point[1] + 1),
        (point[0] + 1, point[1]))

    return [p for p in neighbors if 0 <= p[0] < maze_dim[0] and 0 <= p[1] < maze_dim[1]]


def removable(maz, ii, jj):
    counter = 0
    for p in adjacent_to(((len(maz), len(maz[0])), (ii, jj))):
        if not maz[p[0]][p[1]]:
            if counter:
                return True
            counter += 1
    return False

def answer(map):
    g = Graph()
    counter = 0
    mazematrix = {}
    edges = []
    passable_walls = []

    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 1 and removable(maze, i, j):
                passable_walls.append((i, j))

    for i in range(len(maze) ** 2):
        g.add_vertex(i)

    for i in range(len(maze)):
        mazematrix[i] = {}
        for j in range(len(maze)):
            mazematrix[i][j] = counter
            counter = counter + 1

    for i in range(len(mazematrix)):
        for j in range(len(mazematrix[i])):

            if legalCoord(i, j) == True:

                # center grid
                if 0 < i < (len(mazematrix) - 1) and 0 < j < (len(mazematrix) - 1):
                    # print i, j, "start"
                    edges.extend([(mazematrix[i][j], mazematrix[i][j + 1], maze[i][j + 1]),
                                  (mazematrix[i][j], mazematrix[i + 1][j], maze[i + 1][j]),
                                  (mazematrix[i][j], mazematrix[i][j - 1], maze[i][j - 1]),
                                  (mazematrix[i][j], mazematrix[i - 1][j], maze[i - 1][j])])

                # top mid edge
                if i == 0 and j != 0 and j != (len(mazematrix) - 1):
                    # print i, j, "start"
                    edges.extend([(mazematrix[i][j], mazematrix[i + 1][j], maze[i + 1][j]),
                                  (mazematrix[i][j], mazematrix[i][j + 1], maze[i][j + 1]),
                                  (mazematrix[i][j], mazematrix[i][j - 1], maze[i][j - 1])])

                # bottom mid range
                if i == (len(mazematrix) - 1) and j != 0 and j != (len(mazematrix) - 1):
                    # print i, j, "start"
                    edges.extend([(mazematrix[i][j], mazematrix[i][j + 1], maze[i][j + 1]),
                                  (mazematrix[i][j], mazematrix[i][j - 1], maze[i][j - 1]),
                                  (mazematrix[i][j], mazematrix[i - 1][j], maze[i - 1][j])])

                # left mid range
                if j == 0 and i != 0 and i != (len(mazematrix) - 1):
                    # print i, j, "start"
                    edges.extend([(mazematrix[i][j], mazematrix[i - 1][j], maze[i - 1][j]),
                                  (mazematrix[i][j], mazematrix[i + 1][j], maze[i + 1][j]),
                                  (mazematrix[i][j], mazematrix[i][j + 1], maze[i][j + 1])])

                # Right mid range
                if j == (len(mazematrix) - 1) and i != 0 and i != (len(mazematrix) - 1):
                    # print i, j, "start"
                    edges.extend([(mazematrix[i][j], mazematrix[i - 1][j], maze[i - 1][j]),
                                  (mazematrix[i][j], mazematrix[i + 1][j], maze[i + 1][j]),
                                  (mazematrix[i][j], mazematrix[i][j - 1], maze[i][j - 1])])

                # left top corner
                if i == 0 and j == 0:
                    # print i, j, "start"
                    edges.extend([(mazematrix[i][j], mazematrix[i][j + 1], maze[i][j + 1]),
                                  (mazematrix[i][j], mazematrix[i + 1][j], maze[i + 1][j])])

                # right bottom corner
                if i == (len(mazematrix) - 1) and j == (len(mazematrix) - 1):
                    # print i, j, "start"
                    edges.extend([(mazematrix[i][j], mazematrix[i][j - 1], maze[i][j - 1]),
                                  (mazematrix[i][j], mazematrix[i - 1][j], maze[i - 1][j])])

                # right top corner
                if i == 0 and j == (len(mazematrix) - 1):
                    # print i, j, "start"
                    edges.extend([(mazematrix[i][j], mazematrix[i][j - 1], maze[i][j - 1]),
                                  (mazematrix[i][j], mazematrix[i + 1][j], maze[i + 1][j])])

                # left bottom corner
                if i == (len(mazematrix) - 1) and j == 0:
                    # print i, j, "start"
                    edges.extend([(mazematrix[i][j], mazematrix[i][j + 1], maze[i][j + 1]),
                                  (mazematrix[i][j], mazematrix[i - 1][j], maze[i - 1][j])])
            else:
                print "not in bound"

    for i in edges:
        g.add_edge(i[0], i[1], i[2])

    entrancetowall = []
    walltoexit = []
    passable_walls_node = []

    #dijkstra(g, g.get_vertex(0), g.get_vertex(len(maze)**2-1))

    for i in passable_walls:
        passable_walls_node.append(mazematrix[i[0]][i[1]])

    # for i in passable_walls_node:
    #     dijkstra(g, g.get_vertex(0), g.get_vertex(i))
    #
    #     target = g.get_vertex(i)
    #     path = [target.get_id()]
    #     shortest(target, path)
    #     entrancetowall.append(path)

    # for i in passable_walls_node:
    #     dijkstra(g, g.get_vertex(i), g.get_vertex(len(maze)**2-1))
    #
    #     target = g.get_vertex(len(maze)**2-1)
    #     path = [target.get_id()]
    #     shortest(target, path)
    #     walltoexit.append(path[::-1])

    dijkstra(g, g.get_vertex(6), g.get_vertex(35))

    target = g.get_vertex(35)
    path = [target.get_id()]
    shortest(target, path)
    walltoexit.append(path[::-1])

    #print entrancetowall
    #print walltoexit

    # print mazematrix
    # print edges

    return None

answer(maze)

# maze = [[0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 1],
#         [0, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0]]


