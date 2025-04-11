from pathfinding.core import Grid
from pathfinding.finder import AStarFinder


class AI_NPC:
    def __init__(self):
        self.path = []

    def update_path(self, target, obstacle_map):
        grid = Grid(matrix=obstacle_map)  # 0 = walkable, 1 = wall
        start = grid.node(self.x, self.y)
        end = grid.node(target.x, target.y)
        finder = AStarFinder()
        self.path, _ = finder.find_path(start, end, grid)
        
    def move(self):
        if self.path:
            next_node = self.path.pop(0)
            self.x, self.y = next_node.x, next_node.y