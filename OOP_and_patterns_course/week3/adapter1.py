class Light:
    """
    Describes how light and obstacles should be added to the map
    """

    def __init__(self, dim):
        self.dim = dim
        self.grid = self.set_dim(dim)
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        self.dim = dim
        return [[0 for i in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self):
        """
        You can substitute your own way of adding lights
        """
        self.lights = []

        for i in range(self.dim[1]):
            for j in range(self.dim[0]):
                if j == 2 and i <= 3:                   # just a rule for being light
                    self.lights.append((i, j))

    def set_obstacles(self):
        """
        You can substitute your own way of adding obstacles
        """
        self.obstacles = []

        for i in range(self.dim[1]):
            for j in range(self.dim[0]):
                if j == 2 and i <= 3:                   # just a rule for being obstacle
                    self.obstacles.append((i, j+1))

    def generate_lights(self):
        # adds lights and obstacles marks
        self.set_lights()
        self.set_obstacles()

        # adds a light point or obstacle point to the map, if there is no any marks - adds an empty space mark
        for i in range(self.dim[1]):
            for j in range(self.dim[0]):
                if (i, j) in self.lights:
                    self.grid[i][j] = 1
                if (i, j) in self.obstacles:
                    self.grid[i][j] = -1

        return self.grid


class System:

    def __init__(self):
        # just some space
        self.map = []

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten()
        return self.__str__()

    def __str__(self):
        """
        Visualizes map in 2D format. 1 is a mark for a "light" on a map (-1 is a mark for an "obstacle")
        :return: str
        """
        res = ""
        light_place = 1
        obstacle_place = -1
        for i in self.lightmap:
            row_res = ""
            for j in i:
                if j == light_place:
                    row_res += "*"
                elif j == obstacle_place:
                    row_res += str("|")
                else:
                    row_res += " "
            row_res += "\n"
            res += row_res
        return res


class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    # actions for making list that will go to sytem, using function from Light
    def lighten(self):
        map_ = self.adaptee.generate_lights()  # all lights and obstacaals add in this func
        return map_


map_ = [[0 for i in range(5)] for _ in range(5)]
system = System()
light = Light([len(map[0]), len(map_)])
adapter = MappingAdapter(light)


print(system.get_lightening(adapter))
