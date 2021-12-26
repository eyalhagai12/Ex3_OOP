# import and init pygame
import math

import pygame
import GraphAlgo


def arrow(screen, lcolor, tricolor, start, end, trirad, thickness=2):
    rad = math.pi / 180
    pygame.draw.line(screen, lcolor, start, end, thickness)
    rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi / 2
    pygame.draw.polygon(screen, tricolor, ((end[0] + trirad * math.sin(rotation),
                                            end[1] + trirad * math.cos(rotation)),
                                           (end[0] + trirad * math.sin(rotation - 120 * rad),
                                            end[1] + trirad * math.cos(rotation - 120 * rad)),
                                           (end[0] + trirad * math.sin(rotation + 120 * rad),
                                            end[1] + trirad * math.cos(rotation + 120 * rad))))


class GUI:
    """
    This class is responsible for the GUI
    """

    def __init__(self, algo: GraphAlgo):
        """
        Init a GUI object using the GraphAlgo object
        """
        pygame.init()

        self.algo = algo
        self.graph = algo.get_graph()
        self.points = {}

        # set up the screen size
        self.screen = pygame.display.set_mode([1500, 900], pygame.RESIZABLE)

    def run_gui(self):
        """
        Runs the GUI
        """
        # the main GUI loop
        running = True
        while running:

            # monitor events
            for event in pygame.event.get():
                # quit when closing window
                if event.type == pygame.QUIT:
                    running = False

            # paint screen white
            self.screen.fill((255, 255, 255))

            # draw the graph on the screen
            self.draw_graph()

            # update display
            pygame.display.flip()

        pygame.quit()

    def draw_graph(self):
        """
        Draw the graph on the screen
        """
        width, height = self.screen.get_size()

        # draw all nodes
        nodes = [node for node in self.graph.get_all_v().values()]
        max_x = 0
        min_x = math.inf

        max_y = 0
        min_y = math.inf

        # get max and min x and y coord
        for node in nodes:
            x = node.get_pos()[0]
            y = node.get_pos()[1]

            # max x
            if x > max_x:
                max_x = x

            # max y
            if y > max_y:
                max_y = y

            # min x
            if x < min_x:
                min_x = x

            # min y
            if y < min_y:
                min_y = y

        # transform nodes position and save them
        for node in nodes:
            # get point and transform its coordinates
            point = node.get_pos()

            x = point[0] - min_x
            x = (x / (max_x - min_x)) * width * 0.8 + (width * 0.1)

            y = point[1] - min_y
            y = (y / (max_y - min_y)) * height * 0.8 + (height * 0.1)

            point = (x, y)

            # save points to draw edges and nodes later
            self.points[node.get_id()] = point

        # draw edges
        edges = self.graph.get_edges().values()

        for edge in edges:
            # get points
            p1 = self.points[edge.get_src()]
            p2 = self.points[edge.get_dst()]

            # draw edge
            arrow(self.screen, (0, 0, 0), (0, 0, 0), p1, p2, 15)

            # draw nodes
            point_list = [point for point in self.points.values()]
            for point in point_list:
                # draw node
                pygame.draw.circle(self.screen, (255, 0, 0), point, 10)