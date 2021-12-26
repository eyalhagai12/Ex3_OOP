# import and init pygame
import math

import pygame
import GraphAlgo
from Button import Button

b_width = 150
b_height = 75


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

        self.gui_font = pygame.font.Font(None, 30)
        self.screen = pygame.display.set_mode([1500, 900], pygame.RESIZABLE)

        self.algo = algo
        self.graph = algo.get_graph()
        self.points = {}
        self.dots = {}
        self.buttons = []

        # flags
        self.add_node_flag = False
        self.remove_node_flag = False
        self.add_edge_flag = False
        self.remove_edge_flag = False

        # create buttons
        self.create_buttons()

        # variables for different functions
        self.max_x = 0
        self.min_x = math.inf

        self.max_y = 0
        self.min_y = math.inf

        self.width, self.height = self.screen.get_size()

        self.last_id = self.graph.v_size()

        self.press_counter = 0
        self.pressed_nodes = []

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
                if event.type == pygame.MOUSEBUTTONDOWN and self.add_node_flag:
                    pos = pygame.mouse.get_pos()
                    self.add_node_gui(pos)
                if event.type == pygame.MOUSEBUTTONDOWN and self.remove_node_flag:
                    pos = pygame.mouse.get_pos()
                    self.remove_node_gui(pos)
                if event.type == pygame.MOUSEBUTTONDOWN and self.remove_edge_flag:
                    pos = pygame.mouse.get_pos()
                    self.press_counter += 1
                    self.pressed_nodes.append(self.node_pressed(pos))
                    if self.press_counter >= 2:
                        self.remove_edge_gui(self.pressed_nodes[0], self.pressed_nodes[1])
                        self.pressed_nodes = []
                        self.press_counter = 0

            # paint screen white
            self.screen.fill((255, 255, 255))

            # draw the graph on the screen
            self.draw_graph()
            self.handle_buttons()

            # update display
            pygame.display.flip()
            pygame.display.update()

        pygame.quit()

    def draw_graph(self):
        """
        Draw the graph on the screen
        """
        self.width, self.height = self.screen.get_size()

        # draw all nodes
        nodes = [node for node in self.graph.get_all_v().values()]
        self.max_x = 0
        self.min_x = math.inf

        self.max_y = 0
        self.min_y = math.inf

        # get max and min x and y coord
        for node in nodes:
            x = node.get_pos()[0]
            y = node.get_pos()[1]

            # max x
            if x > self.max_x:
                self.max_x = x

            # max y
            if y > self.max_y:
                self.max_y = y

            # min x
            if x < self.min_x:
                self.min_x = x

            # min y
            if y < self.min_y:
                self.min_y = y

        # transform nodes position and save them
        for node in nodes:
            # get point and transform its coordinates
            point = node.get_pos()

            x = point[0] - self.min_x
            x = (x / (self.max_x - self.min_x)) * self.width * 0.8 + (self.width * 0.1)

            y = point[1] - self.min_y
            y = (y / (self.max_y - self.min_y)) * self.height * 0.8 + (self.height * 0.1)

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
        point_list = [point for point in self.points.items()]
        for key, point in point_list:
            # draw node amd save keys
            self.dots[key] = pygame.draw.circle(self.screen, (255, 0, 0), point, 10)

    def create_buttons(self):
        """
        Create the relevant buttons
        """
        b1 = Button(self.screen, "Add node", self.gui_font, b_width, b_height, (5, 5), 5, self.enable_add_node)
        b2 = Button(self.screen, "Add edge", self.gui_font, b_width, b_height, (b_width + 5, 5), 5, self.add_edge_gui)
        b3 = Button(self.screen, "Remove node", self.gui_font, b_width, b_height, (2 * b_width + 5, 5), 5,
                    self.enable_remove_node)
        b4 = Button(self.screen, "Remove edge", self.gui_font, b_width, b_height, (3 * b_width + 5, 5), 5,
                    self.enable_remove_edge)

        self.buttons.append(b1)
        self.buttons.append(b2)
        self.buttons.append(b3)
        self.buttons.append(b4)

    def handle_buttons(self, draw=True):
        """
        look for any press on the buttons
        """
        # draw and handle buttons
        if draw:
            for button in self.buttons:
                button.check_click()
                button.draw()

    def node_pressed(self, mouse_pos):
        """
        Detect if a node was pressed at that moment
        """
        for node in self.dots.values():
            if node.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    keys = [k for k, v in self.dots.items() if v == node]
                    key = keys[0]
                    return key

    def remove_node_gui(self, mouse_pos):
        """
        Remove a node from the graph using GUI
        """
        key = self.node_pressed(mouse_pos)
        if key is not None:
            self.graph.remove_node(key)
            self.points.pop(key)
            self.dots.pop(key)
            print(f"Removed node: {key}")
            self.remove_node_flag = False

    def enable_add_node(self):
        """
        Enable add node
        """
        self.add_node_flag = True
        self.remove_node_flag = False
        self.remove_edge_flag = False
        self.add_edge_flag = False
        self.pressed_nodes = []
        self.press_counter = 0

    def enable_remove_node(self):
        """
        Enable remove node
        """
        self.remove_node_flag = True
        self.add_node_flag = False
        self.remove_edge_flag = False
        self.add_edge_flag = False
        self.pressed_nodes = []
        self.press_counter = 0

    def enable_remove_edge(self):
        """
        Enable remove edge
        """
        self.remove_edge_flag = True
        self.remove_node_flag = False
        self.add_node_flag = False
        self.add_edge_flag = False
        self.pressed_nodes = []
        self.press_counter = 0

    def add_node_gui(self, mouse_pos):
        """
        Add a new node to the graph using GUI
        """
        x = ((mouse_pos[0] - (self.width * 0.1)) / (self.width * 0.8)) * (self.max_x - self.min_x)
        y = ((mouse_pos[1] - (self.height * 0.1)) / (self.height * 0.8)) * (self.max_y - self.min_y)

        x = x + self.min_x
        y = y + self.min_y

        new_point = (x, y)

        self.graph.add_node(self.last_id, new_point)
        self.last_id += 1

        self.add_node_flag = False

    def add_edge_gui(self):
        pass

    def remove_edge_gui(self, src, dest):
        self.graph.remove_edge(src, dest)
