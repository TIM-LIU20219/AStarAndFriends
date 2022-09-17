'''
Best-first search is a greedy algorithm. It favors nodes that are close to the goal, by calculating a heuristic function
However, it is worth noting that it has a similar updating method with the Dijkstra.
'''
import time
from math import sqrt
from queue import PriorityQueue
from utils import env, plotting


class BestFirstSearch():
    def __init__(self, type = "Euclidian") -> None:
        self.frontier = PriorityQueue()
        self.parent = dict()
        self.visited = list()
        self.g = dict()
        self.type = type
        self.path = []
        self.found = False
        self.env = env.Env()
        self.start = (1, 1)
        self.goal = (self.env.x_size - 2, self.env.y_size - 2)

        self.parent[self.start] = None
        self.g[self.start] = 0
        self.frontier.put((self.cal_h(self.start), self.start))
        self.visited.append(self.start)
    
    def cal_h(self, p):
        if self.type == "Euclidian":
            return sqrt((p[0] - self.goal[0]) ** 2 + (p[1] - self.goal[1]) ** 2) 
        else:
            return abs(p[0] - self.goal[0]) + abs((p[1] - self.goal[1]))

    def get_path(self):
        '''
        construct the selected path from the search function
        params: none
        return: update self.path
        '''
        cur = self.goal
        max_iter = 10000;
        while cur != self.start:
            self.path.append(cur)
            cur = self.parent[cur] # iterate until reaching the start
            max_iter -= 1
            if max_iter < 0:
                print("Failed with loop path!")
                break
        self.path.reverse() # note that the constructed path is from goal to start, in reverse order
        print("path found!")
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
    
    def search(self):

        while not self.frontier.empty():
            cur_node = self.frontier.get()
            cur_node = cur_node[1]
            
            if cur_node == self.goal:
                self.found = True
                # self.get_path()
                break
            
            for new_node in self.get_neighbor(cur_node):
                h_val = self.cal_h(new_node)
                new_cost = self.g[cur_node] + h_val

                if new_node not in self.g or new_cost < self.g[new_node]:
                    self.g[new_node] = new_cost
                    self.parent[new_node] = cur_node                
                    self.frontier.put((h_val, new_node))
        
        if self.found:
            self.get_path()
            return self.path, self.parent
        else:
            return None, None
                    
def main():
    planner = BestFirstSearch()
    t_start = time.time()
    path, visited = planner.search();
    t_end = time.time();
    if planner.found:
        draw = plotting.Plotting(planner.start, planner.goal)
        draw.animation(path, visited, "BestFirstSearch")
    print(t_end - t_start)

if __name__=="__main__":
    main()            



