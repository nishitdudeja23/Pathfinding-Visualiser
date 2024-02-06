from typing import List, Tuple

class Solution:
    """Model a solution to a pathfinding problem."""

    def __init__(
        self,
        path: List[Tuple[int, int]],
        explored: List[Tuple[int, int]],
        time: float = 0,
        path_cost: int = 0
    ) -> None:
        """
        Initialize a Solution instance.

        Parameters:
        - path: List of tuples representing the path.
        - explored: List of tuples representing explored nodes.
        - time: Time taken for the pathfinding.
        - path_cost: Cost associated with the path.
        """
        self.path = path
        self.path_cost = path_cost
        self.path_length = len(path)
        self.explored = explored
        self.explored_length = len(explored)
        self.time = time

    def __repr__(self) -> str:
        return f"Solution(path={self.path}, explored={self.explored}, time={self.time})"
class NoSolution(Solution):
    """Model an empty pathfinding solution."""

    def __init__(self, explored: List[Tuple[int, int]], time: float = 0) -> None:
        """
        Initialize a NoSolution instance.

        Parameters:
        - explored: List of tuples representing explored nodes.
        - time: Time taken for the pathfinding.
        """
        # Call the constructor of the base class (Solution)
        super().__init__(path=[], explored=explored, time=time, path_cost=0)

    def __repr__(self) -> str:
        return f"NoSolution(explored={self.explored}, time={self.time})"