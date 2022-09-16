'''
author: Tim Liu
BFS is a very basic search-based path finding algorithm
It uniformly (important!) explores nodes in all directions
'''
import queue
from utils import env, plotting
import time

class BFS:
    def __init__(self) -> None:
        '''
        BFS maintains a frontier
        after exploring the head`s neighbour, the head node goes to another collection
        thus, frontier is a queue

        To generate the path, we need to record the node`s parent (where it comes from)
        in python, use a dict to track
        '''
        self.frontier = queue.Queue()
        self.parent = dict()

        self.env = env.Env()
        self.start = (3, 3)
        self.goal = (self.env.x_size - 2, self.env.y_size - 2)

        self.path = []

    def get_neighbor(self, s):
        """
        find neighbors of state s that not in obstacles.
        :param s: state
        :return: neighbors
        """
        l = list()
        for move in self.env.motions:
            if (s[0] + move[0], s[1] + move[1]) not in self.env.obs:
                l.append((s[0] + move[0], s[1] + move[1]))
        return l

    def search(self):
        # init with pushing the starting node
        found = False
        self.frontier.put(self.start)
        self.parent[self.start] = None # the starting point`s parent can be None
        while not self.frontier.empty():
            # fetch the queue`s head
            cur_node = self.frontier.get()
            if cur_node == self.goal:
                # self.parent[self.goal] = 
                # self.get_path()
                found = True
                break
            for new_node in self.get_neighbor(cur_node): # get adjacent none-obstacle grid
                if new_node not in self.parent: # this node has not been explored
                    # update frontier and parent
                    self.frontier.put(new_node)
                    self.parent[new_node] = cur_node
        if found:
            self.get_path()
            return self.path, self.parent
        else:
            return None, None

    def get_path(self):
        # now that the frontier has reached the goal
        # we can reconstruct the path bia traversing the parent collection
        
        cur = self.goal
        while cur != self.start:
            self.path.append(cur)
            cur = self.parent[cur] # iterate until reaching the start
        self.path.reverse() # note that the constructed path is from goal to start, in reverse order
        print("path found!")
def main():
    planner = BFS()
    t_start = time.time()
    path, visited = planner.search();
    t_end = time.time();
    draw = plotting.Plotting(planner.start, planner.goal)
    draw.animation(path, visited, "BFS")
    print(t_end - t_start)

if __name__=="__main__":
    main()

