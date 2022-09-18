"""
Env 2D
original author: huiming zhou
edition: Tim Liu
"""

from pickle import TRUE
from random import randint
class Env:
    # def __init__(self, x_size, y_size, obs_pos):
    def __init__(self) -> None:
        '''
        parameters:
        x_size, y_size: x and y size of the entire map
        obs_pos: contains the 2-d indecies of obstacles blobs
        dof: available directions of movement, typically 4 and 8
        animation: plot the outcome
        MonteCarlo: repeat numerours time to access time
        random_obs: generate random obstacle
        
        '''
        
        dof = 8
        self.x_size = 51  
        self.y_size = 51
        self.animation = 0
        self.MonteCarlo = 1
        self.repeat_times = 100
        random_obs = False
        if dof == 8:
            self.motions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                (1, 0), (1, -1), (0, -1), (-1, -1)]
        else:
            self.motions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        obs_vertices = [[(2, 2), (3, 4)], [(5, 10), (5, 20)], [(10, 1), (10, 6)], 
        [(14, 3),(17, 7)], [(13, 20),(20, 20)],[(35, 30), (37, 35)], [(40, 40), (40, 45)]]
        # self.obs = self.obs_map(obs_vertices)
        self.obs = set()
        self.fill_obs(obs_vertices)
        

    def fill_obs(self, obs_vertices):
        """
        Initialize obstacles' positions
        :return: map of obstacles
        """

        # map boundaries are set to be obstacles
        x = self.x_size
        y = self.y_size
        for i in range(x):
            self.obs.add((0, i))
            self.obs.add((y - 1, i))
        for i in range(y):
            self.obs.add((i, 0))
            self.obs.add((i, x - 1))

        # for blob in self.obs_pos:
        #     obs.add(blob)
        for blob in obs_vertices:
            pA = blob[0]
            pB = blob[1]
            for x in range(pA[0], pB[0] + 1):
                for y in range(pA[1], pB[1] + 1):
                    self.obs.add((x, y))

