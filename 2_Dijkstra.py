'''
author: Tim Liu
Dijkstra`s algorithm can be seen as derivation of the breadth-first search
It introduces the idea of **cost**
'''

from queue import PriorityQueue
import time
from math import inf, sqrt
from utils import env, plotting


class Djikstra():
    def __init__(self) -> None:
        self.frontier = PriorityQueue()
        self.parent = dict()
        self.g = dict() # a critical change compared with BFS
        self.env = env.Env()
        self.path = []

        self.start = (1,1)
        self.goal = (self.env.x_size - 2, self.env.y_size - 2)

        self.frontier.put((0, self.start))
        self.g[self.start] = 0
        self.parent[self.start] = None

    def search(self):
        '''
        searching process
        params: none
        return: path and visited nodes
        '''
        found = False
        while not self.frontier.empty():
            cur_node = self.frontier.get()[1]
            if cur_node == self.goal:
                found = True
                break
            for new_node in self.get_neighbor(cur_node):

                new_cost = self.g[cur_node] + self.cal_dist(cur_node, new_node)

                if new_node not in self.g or new_cost < self.g[new_node]:
                    self.g[new_node] = new_cost
                    self.parent[new_node] = cur_node                
                    self.frontier.put((self.g[new_node], new_node))
        if found:
            self.get_path()
            return self.path, self.parent
        else:
            return None, None
        

    def get_neighbor(self, s):
        """
        find neighbors of state s that not in obstacles.
        param: s - state
        return: list of neighbors nodes
        """
        l = list()
        for move in self.env.motions:
            if (s[0] + move[0], s[1] + move[1]) not in self.env.obs:
                l.append((s[0] + move[0], s[1] + move[1]))
        return l

    def cal_dist(self, nA, nB):
        '''
        calculate distance between 2 nodes
        in grid space, use Euclidian distance
        param: 2 nodes
        return: Euclidian distance or Manhattan ditance
        '''
        if nA in self.env.obs or nB in self.env.obs:
            return inf
        if len(self.env.motions) == 8:
            return sqrt((nA[0] - nB[0]) ** 2 + (nA[1] - nB[1]) ** 2)
        else:
            return abs(nA[0] - nB[0]) + abs(nA[1] - nB[1])

    def get_path(self):
        '''
        construct the selected path from the search function
        params: none
        return: update self.path
        '''
        cur = self.goal
        while cur != self.start:
            self.path.append(cur)
            cur = self.parent[cur] # iterate until reaching the start
        self.path.reverse() # note that the constructed path is from goal to start, in reverse order
        # print("path found!")

def main():
    planner = Djikstra()
    name = "Djikstra"
    
    if planner.env.MonteCarlo:
        t_start = time.time()
        for _ in range(planner.env.repeat_times):
            path, visited = planner.search();
            planner = Djikstra()
        t_end = time.time();
        print(name + " Duration of repeating " + str(planner.env.repeat_times) + " times is: " + str(t_end - t_start))
    if planner.env.animation:
        path, visited = planner.search();
        draw = plotting.Plotting(planner.start, planner.goal)
        draw.animation(path, visited, name)

if __name__=="__main__":
    main()