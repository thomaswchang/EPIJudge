import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# [PROBLEM_TYPE=GRAPH] P18.1 PG 287
# Given a 2D matrix, where black=obstacle white=available, find a path from entrance to exit

# Analysis: Since problem did not ask for shortest path, let's use DFS since it is easier to code


WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:

    def helper(cur):
        if not ((0 <= cur.x < len(maze)) and
                (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
            return False

        # Let's assume cur is a solution candidate
        path.append(cur)

        maze[cur.x][cur.y] = BLACK

        if cur == e:
            return True

        if any(
            map(helper,
                 # Interesting: map takes the constructor, and 2 tuples
                 map( Coordinate, (cur.x -1, cur.x+1, cur.x, cur.x), (cur.y, cur.y, cur.y-1, cur.y+1))
            )):
            return True

        del path[-1] # our assumption that cur is a solution is invalid; let's undo
        return False

    path: List[Coordinate] = []
    helper(s)
    return path




@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
