"""
Env 2D
original author: huiming zhou
edition: Tim Liu
"""


class Env:
    # def __init__(self, x_size, y_size, obs_pos):
    def __init__(self) -> None:
        '''
        parameters:
        x_size, y_size: x and y size of the entire map
        obs_pos: contains the 2-d indecies of obstacles blobs
        dof: available directions of movement, typically 4 and 8
        '''
        # todo: wrap these parameters into a config file
        x_size = 31
        y_size = 31
        # obs_pos = ((5,10),(20,15))
        # x_size = 5
        # y_size = 5
        obs_pos = ((2, 1), (2, 2), (3, 3), (3, 4), (3, 5), (3, 6), (4, 5))
        
        dof = 8
        # map size
        self.x_size = x_size  
        self.y_size = y_size

        if dof == 8:
            self.motions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                (1, 0), (1, -1), (0, -1), (-1, -1)]
        else:
            self.motions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.obs_pos = obs_pos
        self.obs = self.obs_map()
        

    def update_obs(self, obs):
        self.obs = obs

    def obs_map(self):
        """
        Initialize obstacles' positions
        :return: map of obstacles
        """
        obs = set()
        # map boundaries are set to be obstacles
        x = self.x_size
        y = self.y_size
        for i in range(x):
            obs.add((0, i))
            obs.add((y - 1, i))
        for i in range(y):
            obs.add((i, 0))
            obs.add((i, x - 1))

        for blob in self.obs_pos:
            obs.add(blob)
        
        return obs
