import unittest
import os, sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from src.pyls import *

class TestPricePlan(unittest.TestCase):
    def test_ls_dir(self):
        structure_dict = {'name': 'ast', 'size': 4096, 'time_modified': 1699957739, 'permissions': '-rw-r--r--', 'contents': [{'name': 'go.mod', 'size': 225, 'time_modified': 1699957780, 'permissions': '-rw-r--r--'}, {'name': 'ast.go', 'size': 837, 'time_modified': 1699957719, 'permissions': 'drwxr-xr-x'}]}
        result = ls_dir(structure_dict, "contents")
        self.assertEqual(result, ['go.mod', 'ast.go'])

    def test_ls_dir_list_file(self):
        structure_dict = {'name': 'ast', 'size': 4096, 'time_modified': 1699957739, 'permissions': '-rw-r--r--', 'contents': [{'name': 'go_dir', 'size': 225, 'time_modified': 1699957780, 'permissions': '-rw-r--r--', 'contents': [{'name': 'go_file', 'size': 225, 'time_modified': 1699957780, 'permissions': '-rw-r--r--', }]}, {'name': 'ast.go', 'size': 837, 'time_modified': 1699957719, 'permissions': 'drwxr-xr-x'}]}
        result = ls_dir_list(structure_dict, sub_dir = "contents")
        expected = [['-rw-r--r--', 225, 1699957780, 'go_dir', 'dir'], ['drwxr-xr-x', 837, 1699957719, 'ast.go', 'file']]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()