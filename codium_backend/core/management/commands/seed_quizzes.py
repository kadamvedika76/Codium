from django.core.management.base import BaseCommand
from core.models import QuizQuestion

class Command(BaseCommand):
    help = 'Seeds the database with 10 questions per DSA topic'

    def handle(self, *args, **kwargs):
        quiz_data = {
            "Strings": [
                {"q": "What is the time complexity of the KMP algorithm for pattern matching?", "o": ["O(n+m)", "O(n*m)", "O(n log m)", "O(m^2)"], "a": "O(n+m)"},
                {"q": "Which data structure is best suited for storing a dictionary of words for fast prefix search?", "o": ["Hash Map", "Trie", "Binary Search Tree", "Stack"], "a": "Trie"},
                {"q": "In Python/Java, why are strings immutable?", "o": ["To save memory", "Security and Thread Safety", "Because they are primitive", "To make them faster"], "a": "Security and Thread Safety"},
                {"q": "The 'Rabin-Karp' algorithm uses which concept for pattern matching?", "o": ["Dynamic Programming", "Hashing", "Greedy Approach", "Backtracking"], "a": "Hashing"},
                {"q": "What is the space complexity of creating a string of length 'n'?", "o": ["O(1)", "O(log n)", "O(n)", "O(n^2)"], "a": "O(n)"},
                {"q": "Which of these is NOT a standard string algorithm?", "o": ["Z-Algorithm", "Boyer-Moore", "Kruskal's", "Aho-Corasick"], "a": "Kruskal's"},
                {"q": "What is the length of the string 'Codium\0' in C language using strlen()?", "o": ["7", "6", "8", "Depends on Compiler"], "a": "6"},
                {"q": "To find if two strings are Anagrams, what is the best complexity?", "o": ["O(n log n)", "O(n)", "O(n^2)", "O(1)"], "a": "O(n)"},
                {"q": "The 'Naive' pattern searching algorithm has a worst-case complexity of:", "o": ["O(n)", "O(m)", "O(n*m)", "O(n+m)"], "a": "O(n*m)"},
                {"q": "Which method is used to combine strings in Python efficiently?", "o": ["+", "join()", "concat()", "append()"], "a": "join()"}
            ],
            "Stack": [
                {"q": "Which principle does a Stack follow?", "o": ["FIFO", "LIFO", "LILO", "FILO"], "a": "LIFO"},
                {"q": "Which of these is a typical application of a Stack?", "o": ["CPU Scheduling", "Function Calls (Recursion)", "Printer Buffer", "BFS"], "a": "Function Calls (Recursion)"},
                {"q": "What happens when you 'pop' from an empty stack?", "o": ["Overflow", "Underflow", "Null Pointer Exception", "Stack Smash"], "a": "Underflow"},
                {"q": "Which notation is best parsed using a Stack?", "o": ["Infix", "Prefix", "Postfix", "Both Prefix and Postfix"], "a": "Both Prefix and Postfix"},
                {"q": "Time complexity of 'peek' operation in a Stack?", "o": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], "a": "O(1)"},
                {"q": "A stack can be implemented using which other data structure?", "o": ["Queue", "Linked List", "Array", "All of the above"], "a": "All of the above"},
                {"q": "The 'undo' feature in text editors uses which structure?", "o": ["Stack", "Queue", "Tree", "Graph"], "a": "Stack"},
                {"q": "How many stacks are needed to implement a Queue?", "o": ["1", "2", "3", "4"], "a": "2"},
                {"q": "Balanced Parentheses checking uses:", "o": ["Stack", "Queue", "Deque", "Priority Queue"], "a": "Stack"},
                {"q": "The minimum number of stacks to implement a Priority Queue is:", "o": ["1", "2", "3", "Not possible"], "a": "2"}
            ],
            "Queue": [
                {"q": "Which principle does a Queue follow?", "o": ["FIFO", "LIFO", "FILO", "Random Access"], "a": "FIFO"},
                {"q": "What is the condition for a full circular queue (size N)?", "o": ["rear == front", "(rear+1)%N == front", "rear == N-1", "front == N-1"], "a": "(rear+1)%N == front"},
                {"q": "A Deque is a:", "o": ["Double Ended Queue", "Distributed Queue", "Data Entry Queue", "Direct Queue"], "a": "Double Ended Queue"},
                {"q": "Which algorithm uses a Queue?", "o": ["DFS", "BFS", "Binary Search", "Quicksort"], "a": "BFS"},
                {"q": "Adding an element to a Queue is called:", "o": ["Push", "Pop", "Enqueue", "Dequeue"], "a": "Enqueue"},
                {"q": "Which of these is NOT a type of Queue?", "o": ["Circular Queue", "Priority Queue", "Double Ended Queue", "Single Ended Stack"], "a": "Single Ended Stack"},
                {"q": "Time complexity to dequeue an element from an array-based queue?", "o": ["O(1)", "O(n)", "O(log n)", "O(1) if front is tracked"], "a": "O(1) if front is tracked"},
                {"q": "A Priority Queue can be efficiently implemented using:", "o": ["Stack", "Array", "Heap", "Linked List"], "a": "Heap"},
                {"q": "Where are elements removed from a Queue?", "o": ["Front", "Rear", "Middle", "Anywhere"], "a": "Front"},
                {"q": "In a linear queue using an array, 'shifting' elements on dequeue leads to:", "o": ["O(1) time", "O(n) time", "O(log n) time", "No time"], "a": "O(n) time"}
            ],
            "Linked Lists": [
                {"q": "In a Singly Linked List, each node contains data and a:", "o": ["Pointer to Prev", "Pointer to Next", "Pointer to Head", "Index"], "a": "Pointer to Next"},
                {"q": "Random access is possible in Linked Lists.", "o": ["True", "False", "Only in Doubly LL", "Only in Circular LL"], "a": "False"},
                {"q": "Which LL has no NULL at the end?", "o": ["Singly LL", "Doubly LL", "Circular LL", "Skip List"], "a": "Circular LL"},
                {"q": "Complexity to insert a node at the head?", "o": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], "a": "O(1)"},
                {"q": "How many pointers does a node in a Doubly Linked List have?", "o": ["1", "2", "3", "0"], "a": "2"},
                {"q": "To delete a node in Singly LL, you need a pointer to the:", "o": ["Node itself", "Next node", "Previous node", "Head"], "a": "Previous node"},
                {"q": "What is the worst-case time to search an element in a LL of size N?", "o": ["O(1)", "O(log n)", "O(n)", "O(n log n)"], "a": "O(n)"},
                {"q": "Which LL is used to implement a Deque?", "o": ["Singly LL", "Doubly LL", "Static Array", "Stack"], "a": "Doubly LL"},
                {"q": "Finding the middle of a LL in one pass uses:", "o": ["Two pointers", "Recursion", "Two loops", "A Stack"], "a": "Two pointers"},
                {"q": "Linked lists are considered:", "o": ["Static data structures", "Dynamic data structures", "Primitive types", "Cache friendly"], "a": "Dynamic data structures"}
            ],
             "Trees": [
                {"q": "In a Binary Tree, a node can have at most how many children?", "o": ["1", "2", "3", "Unlimited"], "a": "2"},
                {"q": "Which traversal visit nodes in sorted order for a BST?", "o": ["Pre-order", "In-order", "Post-order", "Level-order"], "a": "In-order"},
                {"q": "The height of an empty tree is usually considered:", "o": ["0", "1", "-1", "undefined"], "a": "-1"},
                {"q": "A full binary tree with L leaves has how many internal nodes?", "o": ["L-1", "L+1", "2L", "log L"], "a": "L-1"},
                {"q": "Which traversal is used for Breadth-First Search (BFS)?", "o": ["Pre-order", "In-order", "Post-order", "Level-order"], "a": "Level-order"},
                {"q": "What is the worst-case search time in a skewed BST?", "o": ["O(log n)", "O(n)", "O(1)", "O(n log n)"], "a": "O(n)"},
                {"q": "AVL trees are:", "o": ["Heaps", "Self-balancing BSTs", "Graphs", "B-Trees"], "a": "Self-balancing BSTs"},
                {"q": "Which data structure is used for non-recursive Level-order traversal?", "o": ["Stack", "Queue", "Linked List", "Priority Queue"], "a": "Queue"},
                {"q": "Number of edges in a tree with N nodes?", "o": ["N", "N-1", "N+1", "log N"], "a": "N-1"},
                {"q": "What is a leaf node?", "o": ["Root", "Node with no children", "Node with one child", "The deepest node"], "a": "Node with no children"}
            ],
            "Graphs": [
                {"q": "What is the number of edges in a complete graph with N vertices?", "o": ["N", "N(N-1)/2", "N^2", "2N"], "a": "N(N-1)/2"},
                {"q": "Which algorithm is used for finding Shortest Path in a weighted graph?", "o": ["Prim's", "Kruskal's", "Dijkstra's", "BFS"], "a": "Dijkstra's"},
                {"q": "A graph with no cycles is called:", "o": ["Cyclic", "Acyclic", "Complete", "Bipartite"], "a": "Acyclic"},
                {"q": "DFS uses which data structure?", "o": ["Queue", "Stack", "Heap", "Hash Set"], "a": "Stack"},
                {"q": "Which representation of a graph is better for sparse graphs?", "o": ["Adjacency Matrix", "Adjacency List", "Incidence Matrix", "Array"], "a": "Adjacency List"},
                {"q": "Kruskal's algorithm is used for:", "o": ["Shortest Path", "MST", "Cycle Detection", "Topological Sort"], "a": "MST"},
                {"q": "Topological sorting can be performed on:", "o": ["Any graph", "Undirected graphs", "Directed Acyclic Graphs (DAG)", "Complete graphs"], "a": "Directed Acyclic Graphs (DAG)"},
                {"q": "Time complexity of BFS using Adjacency List (V vertices, E edges)?", "o": ["O(V+E)", "O(V^2)", "O(E^2)", "O(V*E)"], "a": "O(V+E)"},
                {"q": "Which of these is a greedy algorithm?", "o": ["BFS", "DFS", "Prim's", "Bellman-Ford"], "a": "Prim's"},
                {"q": "Detecting a cycle in a directed graph uses:", "o": ["BFS", "DFS with recursion stack", "Dijkstra", "Binary Search"], "a": "DFS with recursion stack"}
            ]
        }

        for topic, questions in quiz_data.items():
            for q in questions:
                QuizQuestion.objects.get_or_create(
                    topic=topic,
                    question_text=q["q"],
                    option_a=q["o"][0],
                    option_b=q["o"][1],
                    option_c=q["o"][2],
                    option_d=q["o"][3],
                    correct_answer=q["a"]
                )
        self.stdout.write(self.style.SUCCESS('Successfully seeded quiz questions'))