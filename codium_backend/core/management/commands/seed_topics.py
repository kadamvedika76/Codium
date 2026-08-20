import os
import django

# 🚨 IMPORTANT: Change 'core' to your app name and 'your_project' to your project folder name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()



from django.core.management.base import BaseCommand
from core.models import TopicContent

class Command(BaseCommand):
    help = 'Seeds the database with ultra-comprehensive DSA sheets'
    from core.models import TopicContent

    def handle(self, *args, **options):
        topics = [
            {
                "topic": "Arrays",
                "category": "dsa",
                "data": {
                    "title": "Arrays",
                    "description": "An array is a fundamental data structure that stores a collection of elements at contiguous memory locations. It allows for O(1) random access but requires a fixed size allocation in most low-level languages.",
                    "sections": [
                        {
                            "heading": "Key Characteristics",
                            "content": "Arrays are highly efficient for reading data but can be costly for modifications.",
                            "points": [
                                "Contiguous Memory Allocation: Elements are stored next to each other, making CPU caching highly efficient.",
                                "Index-based Access: Any element can be accessed instantly using its index (0-based).",
                                "Fixed Size: Traditional arrays cannot change size dynamically (unlike Dynamic Arrays like ArrayList or std::vector)."
                            ]
                        },
                        {
                            "heading": "Time & Space Complexity",
                            "points": [
                                "Access: O(1) - The memory address is calculated instantly using base_address + (index * element_size).",
                                "Search (Unsorted): O(n) - Requires a linear scan.",
                                "Insertion/Deletion: O(n) - Requires shifting elements to maintain contiguous memory."
                            ]
                        }
                    ],
                    "examples": [
                        {
                            "title": "Kadane's Algorithm (Maximum Subarray)",
                            "code": "int maxSubArray(int[] nums) {\n    int maxSum = nums[0];\n    int currentSum = nums[0];\n    for (int i = 1; i < nums.length; i++) {\n        currentSum = Math.max(nums[i], currentSum + nums[i]);\n        maxSum = Math.max(maxSum, currentSum);\n    }\n    return maxSum;\n}",
                            "explanation": "Finds the contiguous subarray with the largest sum in O(n) time and O(1) space."
                        },
                        {
                            "title": "Two-Pointer Technique (Reverse Array)",
                            "code": "void reverse(int[] arr) {\n    int left = 0, right = arr.length - 1;\n    while (left < right) {\n        int temp = arr[left];\n        arr[left] = arr[right];\n        arr[right] = temp;\n        left++; right--;\n    }\n}",
                            "explanation": "Reverses an array in-place without using extra memory."
                        }
                    ]
                }
            },
            {
                "topic": "Strings",
                "category": "dsa",
                "data": {
                    "title": "Strings",
                    "description": "A String is a sequence of characters. In languages like Java, C#, and Python, strings are immutable, meaning once created, their values cannot be changed without creating a new object.",
                    "sections": [
                        {
                            "heading": "Immutability & Memory",
                            "content": "Understanding how strings are stored is crucial for system performance.",
                            "points": [
                                "String Pool: Many languages store string literals in a shared pool to save memory.",
                                "Concatenation Penalty: Using '+' to concatenate strings in a loop creates multiple garbage objects. Use StringBuilder instead.",
                                "Character Encodings: Strings are usually backed by ASCII or Unicode (UTF-8/UTF-16) byte arrays."
                            ]
                        },
                        {
                            "heading": "Common Algorithms",
                            "points": [
                                "Pattern Matching: Naive O(n*m), KMP O(n+m), Rabin-Karp (Hashing).",
                                "Anagrams: Usually solved using frequency arrays or sorting.",
                                "Palindromes: Solved efficiently using the two-pointer technique."
                            ]
                        }
                    ],
                    "examples": [
                        {
                            "title": "Valid Palindrome Check",
                            "code": "boolean isPalindrome(String s) {\n    int l = 0, r = s.length() - 1;\n    while (l < r) {\n        if (s.charAt(l++) != s.charAt(r--)) return false;\n    }\n    return true;\n}",
                            "explanation": "Checks if a string reads the same forwards and backwards in O(n) time."
                        }
                    ]
                }
            },
            {
                "topic": "Stack",
                "category": "dsa",
                "data": {
                    "title": "Stack",
                    "description": "A Stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. The last element added is the first one to be removed.",
                    "sections": [
                        {
                            "heading": "Core Operations",
                            "content": "All primary stack operations occur at the 'top' of the stack, making them extremely fast.",
                            "points": [
                                "Push: Adds an element to the top. Time Complexity: O(1).",
                                "Pop: Removes and returns the top element. Time Complexity: O(1).",
                                "Peek/Top: Returns the top element without removing it. Time Complexity: O(1)."
                            ]
                        },
                        {
                            "heading": "Real-World Applications",
                            "points": [
                                "Function Call Stack: Managing recursive function calls in memory.",
                                "Browser History: The 'Back' button uses a stack of visited URLs.",
                                "Syntax Parsing: Validating balanced parentheses and evaluating postfix/prefix expressions."
                            ]
                        }
                    ],
                    "examples": [
                        {
                            "title": "Valid Parentheses",
                            "code": "boolean isValid(String s) {\n    Stack<Character> stack = new Stack<>();\n    for (char c : s.toCharArray()) {\n        if (c == '(') stack.push(')');\n        else if (c == '{') stack.push('}');\n        else if (c == '[') stack.push(']');\n        else if (stack.isEmpty() || stack.pop() != c) return false;\n    }\n    return stack.isEmpty();\n}",
                            "explanation": "A classic stack problem. Pushes expected closing brackets and matches them as they appear."
                        }
                    ]
                }
            },
            {
                "topic": "Queue",
                "category": "dsa",
                "data": {
                    "title": "Queue",
                    "description": "A Queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. Elements are added at the rear and removed from the front.",
                    "sections": [
                        {
                            "heading": "Types of Queues",
                            "content": "Standard queues have limitations (like memory waste). Variations solve these issues:",
                            "points": [
                                "Circular Queue: The last position connects back to the first, reusing empty spaces.",
                                "Priority Queue: Elements are dequeued based on priority (usually implemented with a Heap), not arrival time.",
                                "Deque (Double Ended Queue): Elements can be added or removed from BOTH ends."
                            ]
                        },
                        {
                            "heading": "Real-World Applications",
                            "points": [
                                "Task Scheduling: CPU processes or thread management.",
                                "Breadth-First Search (BFS): Exploring nodes level-by-level in a graph or tree.",
                                "Message Brokers: Systems like RabbitMQ or Kafka use queues to handle async data."
                            ]
                        }
                    ],
                    "examples": [
                        {
                            "title": "Queue Implementation using LinkedList",
                            "code": "Queue<Integer> q = new LinkedList<>();\nq.offer(10); // Enqueue at rear\nq.offer(20);\nint first = q.poll(); // Dequeue from front (returns 10)",
                            "explanation": "In Java, Queue is an interface often implemented by LinkedList for O(1) operations."
                        }
                    ]
                }
            },
            {
                "topic": "Linked Lists",
                "category": "dsa",
                "data": {
                    "title": "Linked Lists",
                    "description": "A Linked List is a linear data structure where elements are not stored in contiguous memory. Instead, each element (node) contains data and a pointer to the next node.",
                    "sections": [
                        {
                            "heading": "Arrays vs. Linked Lists",
                            "content": "Linked lists solve the fixed-size problem of arrays but introduce pointer overhead.",
                            "points": [
                                "Dynamic Sizing: Grows and shrinks seamlessly without reallocation.",
                                "Fast Insert/Delete: O(1) if you have the pointer to the specific node (no shifting needed).",
                                "No Random Access: You cannot do arr[5]. You must traverse from the head, taking O(n) time."
                            ]
                        },
                        {
                            "heading": "Variations",
                            "points": [
                                "Singly Linked List: Nodes only point forward.",
                                "Doubly Linked List: Nodes point both forward and backward, allowing reverse traversal.",
                                "Circular Linked List: The tail node points back to the head node."
                            ]
                        }
                    ],
                    "examples": [
                        {
                            "title": "Reverse a Linked List",
                            "code": "ListNode reverseList(ListNode head) {\n    ListNode prev = null;\n    ListNode curr = head;\n    while (curr != null) {\n        ListNode nextTemp = curr.next;\n        curr.next = prev;\n        prev = curr;\n        curr = nextTemp;\n    }\n    return prev;\n}",
                            "explanation": "Iteratively reverses the direction of all pointers in O(n) time and O(1) space."
                        }
                    ]
                }
            },
            {
                "topic": "Trees",
                "category": "dsa",
                "data": {
                    "title": "Trees",
                    "description": "A Tree is a hierarchical non-linear data structure consisting of nodes connected by edges. The topmost node is called the Root.",
                    "sections": [
                        {
                            "heading": "Binary Search Tree (BST)",
                            "content": "A highly efficient structure for searching and sorting.",
                            "points": [
                                "Property: For any node, all elements in the left subtree are smaller, and all in the right subtree are larger.",
                                "Complexity: Average O(log n) for search, insert, and delete. Worst case is O(n) if the tree becomes skewed.",
                                "Self-Balancing: AVL and Red-Black trees automatically balance themselves to guarantee O(log n) performance."
                            ]
                        },
                        {
                            "heading": "Tree Traversals",
                            "points": [
                                "Inorder (Left, Root, Right): Prints a BST in sorted ascending order.",
                                "Preorder (Root, Left, Right): Used to create a copy of the tree.",
                                "Postorder (Left, Right, Root): Used to delete the tree."
                            ]
                        }
                    ],
                    "examples": [
                        {
                            "title": "Inorder Traversal (Recursive)",
                            "code": "void inorder(TreeNode root, List<Integer> res) {\n    if (root == null) return;\n    inorder(root.left, res);\n    res.add(root.val);\n    inorder(root.right, res);\n}",
                            "explanation": "Visits the left branch, then the root, then the right branch. Time complexity O(n)."
                        }
                    ]
                }
            },
            {
                "topic": "Graphs",
                "category": "dsa",
                "data": {
                    "title": "Graphs",
                    "description": "A Graph is a non-linear data structure consisting of Vertices (Nodes) and Edges (lines connecting them). It models pairwise relations between objects.",
                    "sections": [
                        {
                            "heading": "Representations",
                            "content": "How we store graphs in code depends on edge density.",
                            "points": [
                                "Adjacency Matrix: A 2D array. Fast for edge lookups O(1), but wastes space O(V^2) for sparse graphs.",
                                "Adjacency List: An array of lists. Space efficient O(V+E), best for most standard algorithm problems."
                            ]
                        },
                        {
                            "heading": "Graph Traversal",
                            "points": [
                                "Breadth-First Search (BFS): Explores level by level using a Queue. Best for finding shortest path in unweighted graphs.",
                                "Depth-First Search (DFS): Explores as deep as possible using a Stack (or Recursion). Best for cycle detection and topological sorting."
                            ]
                        }
                    ],
                    "examples": [
                        {
                            "title": "Breadth-First Search (BFS)",
                            "code": "void bfs(int start, List<List<Integer>> adj) {\n    boolean[] visited = new boolean[adj.size()];\n    Queue<Integer> q = new LinkedList<>();\n    \n    q.offer(start);\n    visited[start] = true;\n    \n    while (!q.isEmpty()) {\n        int node = q.poll();\n        System.out.print(node + \" \");\n        \n        for (int neighbor : adj.get(node)) {\n            if (!visited[neighbor]) {\n                visited[neighbor] = true;\n                q.offer(neighbor);\n            }\n        }\n    }\n}",
                            "explanation": "Guarantees that nodes are visited in order of their distance from the start node."
                        }
                    ]
                }
            }
        ]

        for item in topics:
            TopicContent.objects.update_or_create(
                topic_name=item['topic'],
                category=item['category'],
                defaults={'content_data': item['data']}
            )
        print("Successfully seeded ultra-comprehensive DSA sheets!")
