from collections import defaultdict

# For graph algorithms, try implementing both recursive and iterative solutions
# Actually, try doing with all the recursive problems as well

# IMPORTANT: In python, function parameters are passed by reference!

# This is the recursive DFS implementation
# TODO Implement non recursive one using stack
def do_dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    for n in graph[node] - visited:
        do_dfs(graph, n, visited)

    return visited

def dfs_adjlist(adjl):
    graph = defaultdict(set)

    for i in adjl:
        graph[i[0]].add(i[1])

    print do_dfs(graph, 0)

# This is a pretty tough bit of code
# Especially the way state is maintained across function calls
# This question was asked recently
def dfs_num_triangles(adjl):
    graph = defaultdict(set)

    for i in adjl:
        graph[i[0]].add(i[1])

    def find_triangles(graph, visited=None):
        num_triangles = 0
        for node in graph.keys():
            if node in visited:
                continue
            triangles, visited = dfs_triangle(graph, node, visited, [node], 3)
            num_triangles += triangles

        return num_triangles

    def dfs_triangle(graph, node, visited, dfs_path, c):
        if c == 0:
            if node == dfs_path[0]:
                if len(set(dfs_path) - visited) > 0:
                    return 1, visited
            return 0, visited

        num_triangles = 0
        for n in graph[node]:
            triangles, visited = dfs_triangle(graph, n, visited, dfs_path + [n], c-1)
            if triangles > 0:
                visited.add(n)
                num_triangles += triangles

        visited.add(node)

        return num_triangles, visited

    print find_triangles(graph, set())

# Topological sorting
# This solution takes full advantage of the fact that params are passed by reference
def topological_sort(adjl):
    graph = defaultdict(set)

    for i in adjl:
        graph[i[0]].add(i[1])

    def topological_sort(graph, start, visited, stack):
        visited.add(start)

        for n in graph[start] - visited:
            visited.add(n)
            topological_sort(graph, n, visited, stack)
            stack.append(n)

        return visited, stack

    visited = set()
    stack = []
    for node in graph.keys():
        if node in visited:
            continue

        visited, stack = topological_sort(graph, node, visited, stack)

        stack.append(node)

    print stack

# This problem is a twist on DFS
# See, not going for nodes that have been visited can be a problem in certain scenarios
# Instead, we just need to avoid nodes that have been seen in the current DFS traversal
def get_all_paths(adjl, start, end):
    graph = defaultdict(set)

    for i in adjl:
        graph[i[0]].add(i[1])

    paths = []
    #visited = set()

    def get_dfs_paths(graph, node, end, current_dfs, paths):
        if node == end:
            paths += [current_dfs]
            return

        for n in graph[node] - set(current_dfs): # - visited
            #visited.add(n)
            get_dfs_paths(graph, n, end, current_dfs + [n], paths)

    get_dfs_paths(graph, start, end, [start], paths)

    return paths

# Think about when you need the visited data structure
# Its only needed when the algorithm *requires* that you don't circle back
# to the same node again. Some algorithms however *depend* on it.
# ERRR, you're a fucking idiot. If there is no visited then we'll never
# terminate on a cyclic graph you dumbfuck.
# We have to be REALLY REALLY careful where the visited is put though
def check_bipartite(adjl):
    graph = defaultdict(set)

    for i in adjl:
        graph[i[0]].add(i[1])

    white = set()
    black = set()
    visited = set()

    def bipartite_dfs(graph, node, color, white, black, visited):
        if color == 0:
            white.add(node)
        else:
            black.add(node)

        for n in graph[node] - visited:
            bipartite_dfs(graph, n, not color, white, black, visited)

    for node in graph.keys():
        visited.add(node)
        if node in white:
            color = 0
        else:
            color = 1
        bipartite_dfs(graph, node, color, white, black, visited)

    return len(white.intersection(black)) == 0

# The above is the DFS solution and is more complex than it needs to be
# The BFS solution is much more straightforward

import queuelib

# BFS
# See how you are appending items into the queue, they determine the order
# in which you see things. Right now, we go from right to left, put change
# q.append to q.appendLeft and things will be different
def get_bfs(adjl, start):
    graph = defaultdict(set)

    for i in adjl:
        graph[i[0]].add(i[1])

    q = queuelib.queue.deque()
    visited = set()

    q.append(start)

    while len(q) > 0:
        current = q.pop()
        print current
        visited.add(current)
        for node in graph[current] - visited:
            q.append(node)

# This problem is tricky if you think about it from the perspective of
# the DFS. With the DFS one single run can be stored in a datastructure
# and purged once we are done with it, because of its recursive nature.
# The BFS instead is iterative, which means that we need to build up
# state one step at a time.
# Note that if you want to publish all paths, don't bother keeping
# a visited set. It serves no purpose
def get_shortest_path_bfs(adjl, start, end):
    graph = defaultdict(set)

    for i in adjl:
        graph[i[0]].add(i[1])

    q = queuelib.queue.deque()
    #visited = set()

    q.append((start, [start]))
    #visited.add(start)

    while len(q) > 0:
        current, path = q.pop()

        for node in graph[current] - set(path): # - visited
            if node == end:
                yield path + [node]
            q.append((node, path + [node]))

# The BFS bipartite check is easy but you have to be super careful about checks
# Look, be careful about when you decide to change colors. Be also vigilant about
# when you put elements into a queue
def bfs_bipartite(adjl, start):
    graph = defaultdict(set)

    for i in adjl:
        graph[i[0]].add(i[1])

    visited = set()
    color = defaultdict(bool)
    active_color = True
    color[start] = active_color

    q = queuelib.queue.deque()
    q.append(start)

    while len(q) > 0:
        current = q.pop()
        visited.add(current)

        for node in graph[current]:
            if color.has_key(node):
                if color[node] is active_color:
                    return False

            color[node] = not active_color

            if not node in visited and len(graph[node]) > 0:
                q.append(node)

        active_color = not active_color

    return True

# Implement Prim's MST
# Should be super straightforward

# Strongly connected graph
# Strongly connected -> path exists between any two vertices
# 
