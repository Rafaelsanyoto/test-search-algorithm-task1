# main_test.py

import unittest
import main  # This imports the student's main.py file

class TestGraphAndHeuristics(unittest.TestCase):
    
    def setUp(self):
        # Set up your start and goal nodes
        self.start = 'A'
        self.goal = 'G'
        self.graph = main.graph
        self.heuristics = main.heuristics

    def test_bfs(self):
        expected_bfs_path = ['A', 'B', 'D', 'F', 'G']
        bfs_path = main.bfs(self.graph, self.start, self.goal)
        self.assertEqual(bfs_path, expected_bfs_path, f"BFS path should be {expected_bfs_path}")

    def test_dfs(self):
        expected_dfs_path = ['A', 'B', 'C', 'D', 'F', 'G']
        dfs_path = main.dfs(self.graph, self.start, self.goal)
        self.assertEqual(dfs_path, expected_dfs_path, f"DFS path should be {expected_dfs_path}")

    def test_ucs(self):
        expected_ucs_path = ['A', 'B', 'C', 'D', 'F', 'G']
        ucs_path = main.ucs(self.graph, self.start, self.goal)
        self.assertEqual(ucs_path, expected_ucs_path, f"UCS path should be {expected_ucs_path}")

    def test_greedy_bfs(self):
        expected_greedy_path = ['A', 'C', 'E', 'F', 'G']
        greedy_path = main.greedy_bfs(self.graph, self.start, self.goal, self.heuristics)
        self.assertEqual(greedy_path, expected_greedy_path, f"Greedy BFS path should be {expected_greedy_path}")

    def test_a_star(self):
        expected_a_star_path = ['A', 'B', 'C', 'D', 'F', 'G']
        a_star_path = main.a_star(self.graph, self.start, self.goal, self.heuristics)
        self.assertEqual(a_star_path, expected_a_star_path, f"A* path should be {expected_a_star_path}")

if __name__ == '__main__':
    unittest.main()
