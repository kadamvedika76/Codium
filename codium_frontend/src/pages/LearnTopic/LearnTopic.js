import React, { useState, useEffect } from 'react';
import '../../styles/LearnTopic.css';

function LearnTopic({ topic, category, onNavigate }) {
  const [content, setContent] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchContent();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [topic, category]);

  const fetchContent = async () => {
    try {
      // Dummy data for Arrays topic
      if (category === 'dsa' && topic === 'Arrays') {
        const dummyData = {
          title: "Arrays",
          description: "An array is a collection of elements stored at contiguous memory locations. It is one of the most fundamental data structures in computer science and is used to store multiple values of the same type in a single variable.",
          sections: [
            {
              heading: "Key Characteristics",
              content: "Arrays have several important properties that make them useful for various programming tasks:",
              points: [
                "Fixed size: Once declared, the size cannot be changed",
                "Contiguous memory: Elements are stored in adjacent memory locations",
                "Index-based access: Elements can be accessed using their index (0-based)",
                "Same data type: All elements must be of the same type",
                "Random access: O(1) time complexity for accessing any element"
              ]
            },
            {
              heading: "Time Complexity",
              content: "Understanding the time complexity of array operations is crucial for writing efficient code:",
              points: [
                "Access: O(1) - Direct access using index",
                "Search: O(n) - Linear search through all elements",
                "Insertion at end: O(1) - If space is available",
                "Insertion at beginning/middle: O(n) - Requires shifting elements",
                "Deletion: O(n) - Requires shifting elements after deletion"
              ]
            },
            {
              heading: "Common Operations",
              content: "Here are the most frequently used array operations:",
              code: `// Declaration and Initialization\nint[] arr = new int[5];\nint[] arr2 = {1, 2, 3, 4, 5};\n\n// Accessing elements\nint first = arr[0];\nint last = arr[arr.length - 1];\n\n// Traversing array\nfor (int i = 0; i < arr.length; i++) {\n    System.out.println(arr[i]);\n}\n\n// Using enhanced for loop\nfor (int num : arr) {\n    System.out.println(num);\n}`
            },
            {
              heading: "Common Array Problems",
              content: "Arrays are used to solve many algorithmic problems:",
              points: [
                "Two Sum Problem",
                "Maximum Subarray (Kadane's Algorithm)",
                "Rotate Array",
                "Find Duplicates",
                "Merge Sorted Arrays",
                "Binary Search",
                "Sliding Window Problems"
              ]
            }
          ],
          examples: [
            {
              title: "Example 1: Find Maximum Element",
              code: `public int findMax(int[] arr) {\n    if (arr == null || arr.length == 0) {\n        throw new IllegalArgumentException("Array is empty");\n    }\n    \n    int max = arr[0];\n    for (int i = 1; i < arr.length; i++) {\n        if (arr[i] > max) {\n            max = arr[i];\n        }\n    }\n    return max;\n}`,
              explanation: "This function iterates through the array once to find the maximum element. Time complexity: O(n), Space complexity: O(1)."
            },
            {
              title: "Example 2: Reverse an Array",
              code: `public void reverseArray(int[] arr) {\n    int left = 0;\n    int right = arr.length - 1;\n    \n    while (left < right) {\n        // Swap elements\n        int temp = arr[left];\n        arr[left] = arr[right];\n        arr[right] = temp;\n        \n        left++;\n        right--;\n    }\n}`,
              explanation: "This function uses two pointers to reverse the array in-place. Time complexity: O(n), Space complexity: O(1)."
            },
            {
              title: "Example 3: Two Sum Problem",
              code: `public int[] twoSum(int[] nums, int target) {\n    Map<Integer, Integer> map = new HashMap<>();\n    \n    for (int i = 0; i < nums.length; i++) {\n        int complement = target - nums[i];\n        \n        if (map.containsKey(complement)) {\n            return new int[] { map.get(complement), i };\n        }\n        \n        map.put(nums[i], i);\n    }\n    \n    return new int[] {};\n}`,
              explanation: "This function finds two numbers that add up to a target value using a hash map. Time complexity: O(n), Space complexity: O(n)."
            }
          ]
        };
        setContent(dummyData);
        setLoading(false);
        return;
      }

      const endpoint = category === 'dsa' 
        ? `http://localhost:8000/api/learn/dsa/?topic=${topic}`
        : `http://localhost:8000/api/learn/sql/?topic=${topic}`;
      
      const response = await fetch(endpoint);
      const data = await response.json();
      setContent(data);
    } catch (error) {
      console.error('Error fetching content:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleBack = () => {
    onNavigate(category === 'dsa' ? 'dsa-sheets' : 'sql-sheets');
  };

  if (loading) {
    return <div className="learn-loading">Loading content...</div>;
  }

  if (!content) {
    return (
      <div className="learn-loading">
        <p>No content available for this topic.</p>
        <button className="back-btn" onClick={handleBack}>
          Back to Topics
        </button>
      </div>
    );
  }

  return (
    <div className="learn-topic-container">
      <div className="learn-header">
        <button className="back-btn" onClick={handleBack}>
          ← Back
        </button>
        <h1>{content.title || topic}</h1>
        <p className="topic-category">{category.toUpperCase()}</p>
      </div>

      <div className="learn-content">
        <div className="content-card">
          {content.description && (
            <div className="content-section">
              <h2>Overview</h2>
              <p>{content.description}</p>
            </div>
          )}

          {content.sections && content.sections.map((section, index) => (
            <div key={index} className="content-section">
              <h2>{section.heading}</h2>
              <p>{section.content}</p>
              {section.code && (
                <pre className="code-block">
                  <code>{section.code}</code>
                </pre>
              )}
              {section.points && (
                <ul className="content-list">
                  {section.points.map((point, idx) => (
                    <li key={idx}>{point}</li>
                  ))}
                </ul>
              )}
            </div>
          ))}

          {content.examples && (
            <div className="content-section">
              <h2>Examples</h2>
              {content.examples.map((example, index) => (
                <div key={index} className="example-block">
                  <h3>{example.title}</h3>
                  <pre className="code-block">
                    <code>{example.code}</code>
                  </pre>
                  {example.explanation && <p>{example.explanation}</p>}
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default LearnTopic;
