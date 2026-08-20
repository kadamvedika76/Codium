from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Problem, TestCase

class Command(BaseCommand):
    help = 'Seeds the database with updated DSA problems and hidden test cases'

    def handle(self, *args, **options):
        # 1. Ensure the specific Admin User exists
        admin_user, created = User.objects.get_or_create(username='Siddy1910')
        if created:
            admin_user.set_password('admin123') 
            admin_user.save()
            self.stdout.write(self.style.SUCCESS(f"Created admin user: {admin_user.username}"))

        problems_data = [
  {
    "title": "Find Maximum Element",
    "description": "Given N integers, find the maximum element in the array.",
    "difficulty": "Easy",
    "topic": "Arrays",
    "created_by": "Siddy1910",
    "sample_input": "5\n1 2 3 4 5",
    "sample_output": "5",
    "testcases": [
      {"input_data": "1\n10", "expected_output": "10"},
      {"input_data": "5\n-1 -2 -3 -4 -5", "expected_output": "-1"},
      {"input_data": "4\n0 0 0 0", "expected_output": "0"}
    ]
  },
  {
    "title": "Two Sum",
    "description": "Find indices of two numbers that sum to target.",
    "difficulty": "Medium",
    "topic": "Arrays",
    "created_by": "Siddy1910",
    "sample_input": "4\n2 7 11 15\n9",
    "sample_output": "0 1",
    "testcases": [
      {"input_data": "4\n2 7 11 15\n9", "expected_output": "0 1"},
      {"input_data": "3\n3 3 4\n6", "expected_output": "0 1"},
      {"input_data": "5\n1 2 3 4 5\n10", "expected_output": "-1"}
    ]
  },
  {
    "title": "Maximum Subarray",
    "description": "Find maximum sum of contiguous subarray.",
    "difficulty": "Hard",
    "topic": "Arrays",
    "created_by": "Siddy1910",
    "sample_input": "5\n-2 1 -3 4 -1",
    "sample_output": "4",
    "testcases": [
      {"input_data": "3\n-1 -2 -3", "expected_output": "-1"},
      {"input_data": "6\n1 2 3 4 5 6", "expected_output": "21"},
      {"input_data": "5\n-2 -3 4 -1 -2", "expected_output": "4"}
    ]
  },

  {
    "title": "Valid Parentheses",
    "description": "Check if brackets are balanced.",
    "difficulty": "Easy",
    "topic": "Stack",
    "created_by": "Siddy1910",
    "sample_input": "()",
    "sample_output": "True",
    "testcases": [
      {"input_data": "()", "expected_output": "True"},
      {"input_data": "(]", "expected_output": "False"},
      {"input_data": "({[]})", "expected_output": "True"}
    ]
  },
  {
    "title": "Next Greater Element",
    "description": "Find next greater element for each element.",
    "difficulty": "Medium",
    "topic": "Stack",
    "created_by": "Siddy1910",
    "sample_input": "4\n4 5 2 25",
    "sample_output": "5 25 25 -1",
    "testcases": [
      {"input_data": "3\n1 2 3", "expected_output": "2 3 -1"},
      {"input_data": "3\n3 2 1", "expected_output": "-1 -1 -1"},
      {"input_data": "5\n2 1 2 4 3", "expected_output": "4 2 4 -1 -1"}
    ]
  },
  {
    "title": "Largest Rectangle",
    "description": "Find largest rectangle in histogram.",
    "difficulty": "Hard",
    "topic": "Stack",
    "created_by": "Siddy1910",
    "sample_input": "6\n2 1 5 6 2 3",
    "sample_output": "10",
    "testcases": [
      {"input_data": "3\n2 2 2", "expected_output": "6"},
      {"input_data": "5\n1 2 3 4 5", "expected_output": "9"},
      {"input_data": "5\n5 4 3 2 1", "expected_output": "9"}
    ]
  },

  {
    "title": "Simple Queue",
    "description": "Perform queue operations.",
    "difficulty": "Easy",
    "topic": "Queue",
    "created_by": "Siddy1910",
    "sample_input": "enqueue 1 enqueue 2 dequeue",
    "sample_output": "1",
    "testcases": [
      {"input_data": "enqueue 5 dequeue", "expected_output": "5"},
      {"input_data": "enqueue 10 enqueue 20 dequeue dequeue", "expected_output": "10 20"},
      {"input_data": "enqueue 1 dequeue enqueue 2 dequeue", "expected_output": "1 2"}
    ]
  },
  {
    "title": "Circular Queue",
    "description": "Implement circular queue.",
    "difficulty": "Medium",
    "topic": "Queue",
    "created_by": "Siddy1910",
    "sample_input": "operations",
    "sample_output": "output",
    "testcases": [
      {"input_data": "case1", "expected_output": "case1"},
      {"input_data": "case2", "expected_output": "case2"},
      {"input_data": "case3", "expected_output": "case3"}
    ]
  },
  {
    "title": "Sliding Window Maximum",
    "description": "Find max in every window.",
    "difficulty": "Hard",
    "topic": "Queue",
    "created_by": "Siddy1910",
    "sample_input": "8\n1 3 -1 -3 5 3 6 7\n3",
    "sample_output": "3 3 5 5 6 7",
    "testcases": [
      {"input_data": "5\n1 2 3 4 5\n2", "expected_output": "2 3 4 5"},
      {"input_data": "3\n9 9 9\n1", "expected_output": "9 9 9"},
      {"input_data": "4\n4 3 2 1\n2", "expected_output": "4 3 2"}
    ]
  },

  {
    "title": "Reverse String",
    "description": "Reverse a string.",
    "difficulty": "Easy",
    "topic": "String",
    "created_by": "Siddy1910",
    "sample_input": "hello",
    "sample_output": "olleh",
    "testcases": [
      {"input_data": "abc", "expected_output": "cba"},
      {"input_data": "a", "expected_output": "a"},
      {"input_data": "", "expected_output": ""}
    ]
  },
  {
    "title": "Longest Substring",
    "description": "Find longest substring without repeating characters.",
    "difficulty": "Medium",
    "topic": "String",
    "created_by": "Siddy1910",
    "sample_input": "abcabcbb",
    "sample_output": "3",
    "testcases": [
      {"input_data": "bbbbb", "expected_output": "1"},
      {"input_data": "pwwkew", "expected_output": "3"},
      {"input_data": "", "expected_output": "0"}
    ]
  },
  {
    "title": "Regex Matching",
    "description": "Match string with pattern.",
    "difficulty": "Hard",
    "topic": "String",
    "created_by": "Siddy1910",
    "sample_input": "aa a*",
    "sample_output": "True",
    "testcases": [
      {"input_data": "aa a*", "expected_output": "True"},
      {"input_data": "ab .*", "expected_output": "True"},
      {"input_data": "mississippi mis*is*p*.", "expected_output": "False"}
    ]
  },

  {
    "title": "Reverse Linked List",
    "description": "Reverse a singly linked list.",
    "difficulty": "Easy",
    "topic": "Linked List",
    "created_by": "Siddy1910",
    "sample_input": "1->2->3",
    "sample_output": "3->2->1",
    "testcases": [
      {"input_data": "1->2", "expected_output": "2->1"},
      {"input_data": "1->2->3->4", "expected_output": "4->3->2->1"},
      {"input_data": "1", "expected_output": "1"}
    ]
  },
  {
    "title": "Detect Cycle",
    "description": "Detect if linked list has cycle.",
    "difficulty": "Medium",
    "topic": "Linked List",
    "created_by": "Siddy1910",
    "sample_input": "list",
    "sample_output": "True",
    "testcases": [
      {"input_data": "cycle", "expected_output": "True"},
      {"input_data": "no_cycle", "expected_output": "False"},
      {"input_data": "self_cycle", "expected_output": "True"}
    ]
  },
  {
    "title": "Merge K Lists",
    "description": "Merge multiple sorted lists.",
    "difficulty": "Hard",
    "topic": "Linked List",
    "created_by": "Siddy1910",
    "sample_input": "lists",
    "sample_output": "merged",
    "testcases": [
      {"input_data": "lists1", "expected_output": "merged"},
      {"input_data": "lists2", "expected_output": "merged"},
      {"input_data": "lists3", "expected_output": "merged"}
    ]
  },

  {
    "title": "Inorder Traversal",
    "description": "Perform inorder traversal of binary tree.",
    "difficulty": "Easy",
    "topic": "Trees",
    "created_by": "Siddy1910",
    "sample_input": "tree",
    "sample_output": "inorder",
    "testcases": [
      {"input_data": "tree1", "expected_output": "inorder"},
      {"input_data": "tree2", "expected_output": "inorder"},
      {"input_data": "tree3", "expected_output": "inorder"}
    ]
  },
  {
    "title": "Level Order Traversal",
    "description": "Perform BFS traversal of tree.",
    "difficulty": "Medium",
    "topic": "Trees",
    "created_by": "Siddy1910",
    "sample_input": "tree",
    "sample_output": "levels",
    "testcases": [
      {"input_data": "tree1", "expected_output": "levels"},
      {"input_data": "tree2", "expected_output": "levels"},
      {"input_data": "tree3", "expected_output": "levels"}
    ]
  },
  {
    "title": "Lowest Common Ancestor",
    "description": "Find LCA of two nodes.",
    "difficulty": "Hard",
    "topic": "Trees",
    "created_by": "Siddy1910",
    "sample_input": "tree",
    "sample_output": "node",
    "testcases": [
      {"input_data": "tree1", "expected_output": "node"},
      {"input_data": "tree2", "expected_output": "node"},
      {"input_data": "tree3", "expected_output": "node"}
    ]
  },

  {
    "title": "DFS Traversal",
    "description": "Perform depth-first search.",
    "difficulty": "Easy",
    "topic": "Graphs",
    "created_by": "Siddy1910",
    "sample_input": "graph",
    "sample_output": "dfs",
    "testcases": [
      {"input_data": "graph1", "expected_output": "dfs"},
      {"input_data": "graph2", "expected_output": "dfs"},
      {"input_data": "graph3", "expected_output": "dfs"}
    ]
  },
  {
    "title": "Shortest Path BFS",
    "description": "Find shortest path in unweighted graph.",
    "difficulty": "Medium",
    "topic": "Graphs",
    "created_by": "Siddy1910",
    "sample_input": "graph",
    "sample_output": "distance",
    "testcases": [
      {"input_data": "graph1", "expected_output": "distance"},
      {"input_data": "graph2", "expected_output": "distance"},
      {"input_data": "graph3", "expected_output": "distance"}
    ]
  },
  {
    "title": "Dijkstra Algorithm",
    "description": "Find shortest path in weighted graph.",
    "difficulty": "Hard",
    "topic": "Graphs",
    "created_by": "Siddy1910",
    "sample_input": "graph",
    "sample_output": "shortest",
    "testcases": [
      {"input_data": "graph1", "expected_output": "shortest"},
      {"input_data": "graph2", "expected_output": "shortest"},
      {"input_data": "graph3", "expected_output": "shortest"}
    ]
  },

  {
    "title": "Fibonacci",
    "description": "Find nth Fibonacci number.",
    "difficulty": "Easy",
    "topic": "Dynamic Programming",
    "created_by": "Siddy1910",
    "sample_input": "5",
    "sample_output": "5",
    "testcases": [
      {"input_data": "0", "expected_output": "0"},
      {"input_data": "1", "expected_output": "1"},
      {"input_data": "10", "expected_output": "55"}
    ]
  },
  {
    "title": "Knapsack",
    "description": "Solve 0/1 knapsack problem.",
    "difficulty": "Medium",
    "topic": "Dynamic Programming",
    "created_by": "Siddy1910",
    "sample_input": "items",
    "sample_output": "value",
    "testcases": [
      {"input_data": "case1", "expected_output": "value"},
      {"input_data": "case2", "expected_output": "value"},
      {"input_data": "case3", "expected_output": "value"}
    ]
  },
  {
    "title": "Longest Increasing Subsequence",
    "description": "Find LIS length.",
    "difficulty": "Hard",
    "topic": "Dynamic Programming",
    "created_by": "Siddy1910",
    "sample_input": "array",
    "sample_output": "length",
    "testcases": [
      {"input_data": "arr1", "expected_output": "length"},
      {"input_data": "arr2", "expected_output": "length"},
      {"input_data": "arr3", "expected_output": "length"}
    ]
  },

  {
    "title": "Activity Selection",
    "description": "Select max non-overlapping activities.",
    "difficulty": "Easy",
    "topic": "Greedy",
    "created_by": "Siddy1910",
    "sample_input": "activities",
    "sample_output": "count",
    "testcases": [
      {"input_data": "act1", "expected_output": "count"},
      {"input_data": "act2", "expected_output": "count"},
      {"input_data": "act3", "expected_output": "count"}
    ]
  },
  {
    "title": "Coin Change",
    "description": "Minimum coins required.",
    "difficulty": "Medium",
    "topic": "Greedy",
    "created_by": "Siddy1910",
    "sample_input": "coins",
    "sample_output": "min",
    "testcases": [
      {"input_data": "coins1", "expected_output": "min"},
      {"input_data": "coins2", "expected_output": "min"},
      {"input_data": "coins3", "expected_output": "min"}
    ]
  },
  {
    "title": "Huffman Coding",
    "description": "Construct Huffman tree.",
    "difficulty": "Hard",
    "topic": "Greedy",
    "created_by": "Siddy1910",
    "sample_input": "freq",
    "sample_output": "tree",
    "testcases": [
      {"input_data": "freq1", "expected_output": "tree"},
      {"input_data": "freq2", "expected_output": "tree"},
      {"input_data": "freq3", "expected_output": "tree"}
    ]
  },

  {
    "title": "Permutations",
    "description": "Generate all permutations.",
    "difficulty": "Easy",
    "topic": "Backtracking",
    "created_by": "Siddy1910",
    "sample_input": "1 2",
    "sample_output": "1 2,2 1",
    "testcases": [
      {"input_data": "1", "expected_output": "1"},
      {"input_data": "1 2", "expected_output": "1 2,2 1"},
      {"input_data": "1 2 3", "expected_output": "all"}
    ]
  },
  {
    "title": "N Queens",
    "description": "Solve N queens problem.",
    "difficulty": "Medium",
    "topic": "Backtracking",
    "created_by": "Siddy1910",
    "sample_input": "4",
    "sample_output": "solutions",
    "testcases": [
      {"input_data": "4", "expected_output": "solutions"},
      {"input_data": "1", "expected_output": "1"},
      {"input_data": "2", "expected_output": "0"}
    ]
  },
  {
    "title": "Sudoku Solver",
    "description": "Solve Sudoku puzzle.",
    "difficulty": "Hard",
    "topic": "Backtracking",
    "created_by": "Siddy1910",
    "sample_input": "grid",
    "sample_output": "solved",
    "testcases": [
      {"input_data": "grid1", "expected_output": "solved"},
      {"input_data": "grid2", "expected_output": "solved"},
      {"input_data": "grid3", "expected_output": "solved"}
    ]
  }
]

        for p_data in problems_data:
            problem, p_created = Problem.objects.update_or_create(
                title=p_data['title'],
                defaults={
                    'description': p_data['description'],
                    'difficulty': p_data['difficulty'],
                    'sample_input': p_data['sample_input'],
                    'sample_output': p_data['sample_output'],
                    'topic': p_data['topic'],
                    'created_by': admin_user
                }
            )

            TestCase.objects.filter(problem=problem).delete()

            for ts in p_data['testcases']:
                TestCase.objects.create(
                    problem=problem,
                    input_data=ts['input_data'],  # Match your list keys!
                    expected_output=ts['expected_output'] # Match your list keys!
                )

            status = "CREATED" if p_created else "UPDATED"
# from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User
# from core.models import Problem, TestCase

# class Command(BaseCommand):
#     help = 'Seeds the database with updated DSA problems and hidden test cases'

#     def handle(self, *args, **options):
#         # 1. Ensure the specific Admin User exists
#         admin_user, created = User.objects.get_or_create(username='Siddy1910')
#         if created:
#             admin_user.set_password('admin123') 
#             admin_user.save()
#             self.stdout.write(self.style.SUCCESS(f"Created admin user: {admin_user.username}"))

#         problems_data = [
#   {
#     "title": "Find Maximum Element",
#     "description": "Given N integers, find the maximum element in the array.",
#     "difficulty": "Easy",
#     "topic": "Arrays",
#     "created_by": "Siddy1910",
#     "sample_input": "5\n1 2 3 4 5",
#     "sample_output": "5",
#     "testcases": [
#       {"input_data": "1\n10", "expected_output": "10"},
#       {"input_data": "5\n-1 -2 -3 -4 -5", "expected_output": "-1"},
#       {"input_data": "4\n0 0 0 0", "expected_output": "0"}
#     ]
#   },
#   {
#     "title": "Two Sum",
#     "description": "Find indices of two numbers that sum to target.",
#     "difficulty": "Medium",
#     "topic": "Arrays",
#     "created_by": "Siddy1910",
#     "sample_input": "4\n2 7 11 15\n9",
#     "sample_output": "0 1",
#     "testcases": [
#       {"input_data": "4\n2 7 11 15\n9", "expected_output": "0 1"},
#       {"input_data": "3\n3 3 4\n6", "expected_output": "0 1"},
#       {"input_data": "5\n1 2 3 4 5\n10", "expected_output": "-1"}
#     ]
#   },
#   {
#     "title": "Maximum Subarray",
#     "description": "Find maximum sum of contiguous subarray.",
#     "difficulty": "Hard",
#     "topic": "Arrays",
#     "created_by": "Siddy1910",
#     "sample_input": "5\n-2 1 -3 4 -1",
#     "sample_output": "4",
#     "testcases": [
#       {"input_data": "3\n-1 -2 -3", "expected_output": "-1"},
#       {"input_data": "6\n1 2 3 4 5 6", "expected_output": "21"},
#       {"input_data": "5\n-2 -3 4 -1 -2", "expected_output": "4"}
#     ]
#   },

#   {
#     "title": "Valid Parentheses",
#     "description": "Check if brackets are balanced.",
#     "difficulty": "Easy",
#     "topic": "Stack",
#     "created_by": "Siddy1910",
#     "sample_input": "()",
#     "sample_output": "True",
#     "testcases": [
#       {"input_data": "()", "expected_output": "True"},
#       {"input_data": "(]", "expected_output": "False"},
#       {"input_data": "({[]})", "expected_output": "True"}
#     ]
#   },
#   {
#     "title": "Next Greater Element",
#     "description": "Find next greater element for each element.",
#     "difficulty": "Medium",
#     "topic": "Stack",
#     "created_by": "Siddy1910",
#     "sample_input": "4\n4 5 2 25",
#     "sample_output": "5 25 25 -1",
#     "testcases": [
#       {"input_data": "3\n1 2 3", "expected_output": "2 3 -1"},
#       {"input_data": "3\n3 2 1", "expected_output": "-1 -1 -1"},
#       {"input_data": "5\n2 1 2 4 3", "expected_output": "4 2 4 -1 -1"}
#     ]
#   },
#   {
#     "title": "Largest Rectangle",
#     "description": "Find largest rectangle in histogram.",
#     "difficulty": "Hard",
#     "topic": "Stack",
#     "created_by": "Siddy1910",
#     "sample_input": "6\n2 1 5 6 2 3",
#     "sample_output": "10",
#     "testcases": [
#       {"input_data": "3\n2 2 2", "expected_output": "6"},
#       {"input_data": "5\n1 2 3 4 5", "expected_output": "9"},
#       {"input_data": "5\n5 4 3 2 1", "expected_output": "9"}
#     ]
#   },

#   {
#     "title": "Simple Queue",
#     "description": "Perform queue operations.",
#     "difficulty": "Easy",
#     "topic": "Queue",
#     "created_by": "Siddy1910",
#     "sample_input": "enqueue 1 enqueue 2 dequeue",
#     "sample_output": "1",
#     "testcases": [
#       {"input_data": "enqueue 5 dequeue", "expected_output": "5"},
#       {"input_data": "enqueue 10 enqueue 20 dequeue dequeue", "expected_output": "10 20"},
#       {"input_data": "enqueue 1 dequeue enqueue 2 dequeue", "expected_output": "1 2"}
#     ]
#   },
#   {
#     "title": "Circular Queue",
#     "description": "Implement circular queue.",
#     "difficulty": "Medium",
#     "topic": "Queue",
#     "created_by": "Siddy1910",
#     "sample_input": "operations",
#     "sample_output": "output",
#     "testcases": [
#       {"input_data": "case1", "expected_output": "case1"},
#       {"input_data": "case2", "expected_output": "case2"},
#       {"input_data": "case3", "expected_output": "case3"}
#     ]
#   },
#   {
#     "title": "Sliding Window Maximum",
#     "description": "Find max in every window.",
#     "difficulty": "Hard",
#     "topic": "Queue",
#     "created_by": "Siddy1910",
#     "sample_input": "8\n1 3 -1 -3 5 3 6 7\n3",
#     "sample_output": "3 3 5 5 6 7",
#     "testcases": [
#       {"input_data": "5\n1 2 3 4 5\n2", "expected_output": "2 3 4 5"},
#       {"input_data": "3\n9 9 9\n1", "expected_output": "9 9 9"},
#       {"input_data": "4\n4 3 2 1\n2", "expected_output": "4 3 2"}
#     ]
#   },

#   {
#     "title": "Reverse String",
#     "description": "Reverse a string.",
#     "difficulty": "Easy",
#     "topic": "String",
#     "created_by": "Siddy1910",
#     "sample_input": "hello",
#     "sample_output": "olleh",
#     "testcases": [
#       {"input_data": "abc", "expected_output": "cba"},
#       {"input_data": "a", "expected_output": "a"},
#       {"input_data": "", "expected_output": ""}
#     ]
#   },
#   {
#     "title": "Longest Substring",
#     "description": "Find longest substring without repeating characters.",
#     "difficulty": "Medium",
#     "topic": "String",
#     "created_by": "Siddy1910",
#     "sample_input": "abcabcbb",
#     "sample_output": "3",
#     "testcases": [
#       {"input_data": "bbbbb", "expected_output": "1"},
#       {"input_data": "pwwkew", "expected_output": "3"},
#       {"input_data": "", "expected_output": "0"}
#     ]
#   },
#   {
#     "title": "Regex Matching",
#     "description": "Match string with pattern.",
#     "difficulty": "Hard",
#     "topic": "String",
#     "created_by": "Siddy1910",
#     "sample_input": "aa a*",
#     "sample_output": "True",
#     "testcases": [
#       {"input_data": "aa a*", "expected_output": "True"},
#       {"input_data": "ab .*", "expected_output": "True"},
#       {"input_data": "mississippi mis*is*p*.", "expected_output": "False"}
#     ]
#   },

#   {
#     "title": "Reverse Linked List",
#     "description": "Reverse a singly linked list.",
#     "difficulty": "Easy",
#     "topic": "Linked List",
#     "created_by": "Siddy1910",
#     "sample_input": "1->2->3",
#     "sample_output": "3->2->1",
#     "testcases": [
#       {"input_data": "1->2", "expected_output": "2->1"},
#       {"input_data": "1->2->3->4", "expected_output": "4->3->2->1"},
#       {"input_data": "1", "expected_output": "1"}
#     ]
#   },
#   {
#     "title": "Detect Cycle",
#     "description": "Detect if linked list has cycle.",
#     "difficulty": "Medium",
#     "topic": "Linked List",
#     "created_by": "Siddy1910",
#     "sample_input": "list",
#     "sample_output": "True",
#     "testcases": [
#       {"input_data": "cycle", "expected_output": "True"},
#       {"input_data": "no_cycle", "expected_output": "False"},
#       {"input_data": "self_cycle", "expected_output": "True"}
#     ]
#   },
#   {
#     "title": "Merge K Lists",
#     "description": "Merge multiple sorted lists.",
#     "difficulty": "Hard",
#     "topic": "Linked List",
#     "created_by": "Siddy1910",
#     "sample_input": "lists",
#     "sample_output": "merged",
#     "testcases": [
#       {"input_data": "lists1", "expected_output": "merged"},
#       {"input_data": "lists2", "expected_output": "merged"},
#       {"input_data": "lists3", "expected_output": "merged"}
#     ]
#   },

#   {
#     "title": "Inorder Traversal",
#     "description": "Perform inorder traversal of binary tree.",
#     "difficulty": "Easy",
#     "topic": "Trees",
#     "created_by": "Siddy1910",
#     "sample_input": "tree",
#     "sample_output": "inorder",
#     "testcases": [
#       {"input_data": "tree1", "expected_output": "inorder"},
#       {"input_data": "tree2", "expected_output": "inorder"},
#       {"input_data": "tree3", "expected_output": "inorder"}
#     ]
#   },
#   {
#     "title": "Level Order Traversal",
#     "description": "Perform BFS traversal of tree.",
#     "difficulty": "Medium",
#     "topic": "Trees",
#     "created_by": "Siddy1910",
#     "sample_input": "tree",
#     "sample_output": "levels",
#     "testcases": [
#       {"input_data": "tree1", "expected_output": "levels"},
#       {"input_data": "tree2", "expected_output": "levels"},
#       {"input_data": "tree3", "expected_output": "levels"}
#     ]
#   },
#   {
#     "title": "Lowest Common Ancestor",
#     "description": "Find LCA of two nodes.",
#     "difficulty": "Hard",
#     "topic": "Trees",
#     "created_by": "Siddy1910",
#     "sample_input": "tree",
#     "sample_output": "node",
#     "testcases": [
#       {"input_data": "tree1", "expected_output": "node"},
#       {"input_data": "tree2", "expected_output": "node"},
#       {"input_data": "tree3", "expected_output": "node"}
#     ]
#   },

#   {
#     "title": "DFS Traversal",
#     "description": "Perform depth-first search.",
#     "difficulty": "Easy",
#     "topic": "Graphs",
#     "created_by": "Siddy1910",
#     "sample_input": "graph",
#     "sample_output": "dfs",
#     "testcases": [
#       {"input_data": "graph1", "expected_output": "dfs"},
#       {"input_data": "graph2", "expected_output": "dfs"},
#       {"input_data": "graph3", "expected_output": "dfs"}
#     ]
#   },
#   {
#     "title": "Shortest Path BFS",
#     "description": "Find shortest path in unweighted graph.",
#     "difficulty": "Medium",
#     "topic": "Graphs",
#     "created_by": "Siddy1910",
#     "sample_input": "graph",
#     "sample_output": "distance",
#     "testcases": [
#       {"input_data": "graph1", "expected_output": "distance"},
#       {"input_data": "graph2", "expected_output": "distance"},
#       {"input_data": "graph3", "expected_output": "distance"}
#     ]
#   },
#   {
#     "title": "Dijkstra Algorithm",
#     "description": "Find shortest path in weighted graph.",
#     "difficulty": "Hard",
#     "topic": "Graphs",
#     "created_by": "Siddy1910",
#     "sample_input": "graph",
#     "sample_output": "shortest",
#     "testcases": [
#       {"input_data": "graph1", "expected_output": "shortest"},
#       {"input_data": "graph2", "expected_output": "shortest"},
#       {"input_data": "graph3", "expected_output": "shortest"}
#     ]
#   },

#   {
#     "title": "Fibonacci",
#     "description": "Find nth Fibonacci number.",
#     "difficulty": "Easy",
#     "topic": "Dynamic Programming",
#     "created_by": "Siddy1910",
#     "sample_input": "5",
#     "sample_output": "5",
#     "testcases": [
#       {"input_data": "0", "expected_output": "0"},
#       {"input_data": "1", "expected_output": "1"},
#       {"input_data": "10", "expected_output": "55"}
#     ]
#   },
#   {
#     "title": "Knapsack",
#     "description": "Solve 0/1 knapsack problem.",
#     "difficulty": "Medium",
#     "topic": "Dynamic Programming",
#     "created_by": "Siddy1910",
#     "sample_input": "items",
#     "sample_output": "value",
#     "testcases": [
#       {"input_data": "case1", "expected_output": "value"},
#       {"input_data": "case2", "expected_output": "value"},
#       {"input_data": "case3", "expected_output": "value"}
#     ]
#   },
#   {
#     "title": "Longest Increasing Subsequence",
#     "description": "Find LIS length.",
#     "difficulty": "Hard",
#     "topic": "Dynamic Programming",
#     "created_by": "Siddy1910",
#     "sample_input": "array",
#     "sample_output": "length",
#     "testcases": [
#       {"input_data": "arr1", "expected_output": "length"},
#       {"input_data": "arr2", "expected_output": "length"},
#       {"input_data": "arr3", "expected_output": "length"}
#     ]
#   },

#   {
#     "title": "Activity Selection",
#     "description": "Select max non-overlapping activities.",
#     "difficulty": "Easy",
#     "topic": "Greedy",
#     "created_by": "Siddy1910",
#     "sample_input": "activities",
#     "sample_output": "count",
#     "testcases": [
#       {"input_data": "act1", "expected_output": "count"},
#       {"input_data": "act2", "expected_output": "count"},
#       {"input_data": "act3", "expected_output": "count"}
#     ]
#   },
#   {
#     "title": "Coin Change",
#     "description": "Minimum coins required.",
#     "difficulty": "Medium",
#     "topic": "Greedy",
#     "created_by": "Siddy1910",
#     "sample_input": "coins",
#     "sample_output": "min",
#     "testcases": [
#       {"input_data": "coins1", "expected_output": "min"},
#       {"input_data": "coins2", "expected_output": "min"},
#       {"input_data": "coins3", "expected_output": "min"}
#     ]
#   },
#   {
#     "title": "Huffman Coding",
#     "description": "Construct Huffman tree.",
#     "difficulty": "Hard",
#     "topic": "Greedy",
#     "created_by": "Siddy1910",
#     "sample_input": "freq",
#     "sample_output": "tree",
#     "testcases": [
#       {"input_data": "freq1", "expected_output": "tree"},
#       {"input_data": "freq2", "expected_output": "tree"},
#       {"input_data": "freq3", "expected_output": "tree"}
#     ]
#   },

#   {
#     "title": "Permutations",
#     "description": "Generate all permutations.",
#     "difficulty": "Easy",
#     "topic": "Backtracking",
#     "created_by": "Siddy1910",
#     "sample_input": "1 2",
#     "sample_output": "1 2,2 1",
#     "testcases": [
#       {"input_data": "1", "expected_output": "1"},
#       {"input_data": "1 2", "expected_output": "1 2,2 1"},
#       {"input_data": "1 2 3", "expected_output": "all"}
#     ]
#   },
#   {
#     "title": "N Queens",
#     "description": "Solve N queens problem.",
#     "difficulty": "Medium",
#     "topic": "Backtracking",
#     "created_by": "Siddy1910",
#     "sample_input": "4",
#     "sample_output": "solutions",
#     "testcases": [
#       {"input_data": "4", "expected_output": "solutions"},
#       {"input_data": "1", "expected_output": "1"},
#       {"input_data": "2", "expected_output": "0"}
#     ]
#   },
#   {
#     "title": "Sudoku Solver",
#     "description": "Solve Sudoku puzzle.",
#     "difficulty": "Hard",
#     "topic": "Backtracking",
#     "created_by": "Siddy1910",
#     "sample_input": "grid",
#     "sample_output": "solved",
#     "testcases": [
#       {"input_data": "grid1", "expected_output": "solved"},
#       {"input_data": "grid2", "expected_output": "solved"},
#       {"input_data": "grid3", "expected_output": "solved"}
#     ]
#   }
# ]

#         for p_data in problems_data:
#             problem, p_created = Problem.objects.update_or_create(
#                 title=p_data['title'],
#                 defaults={
#                     'description': p_data['description'],
#                     'difficulty': p_data['difficulty'],
#                     'sample_input': p_data['sample_input'],
#                     'sample_output': p_data['sample_output'],
#                     'topic': p_data['topic'],
#                     'created_by': admin_user
#                 }
#             )

#             TestCase.objects.filter(problem=problem).delete()

#             for ts in p_data['testcases']:
#                 TestCase.objects.create(
#                     problem=problem,
#                     input_data=ts['input_data'],  # Match your list keys!
#                     expected_output=ts['expected_output'] # Match your list keys!
#                 )

#             status = "CREATED" if p_created else "UPDATED"
#             self.stdout.write(f"{status}: {problem.title}")