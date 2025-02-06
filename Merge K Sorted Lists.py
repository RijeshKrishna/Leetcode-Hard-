class Solution {
 public:
  ListNode* mergeKLists(vector<ListNode*>& lists) {
    ListNode dummy(0);  // Dummy node to simplify edge cases
    ListNode* curr = &dummy; // Pointer to track merged list

    // Lambda function for min-heap comparison
    auto compare = [](ListNode* a, ListNode* b) { return a->val > b->val; };

    // Min-heap to store list nodes
    priority_queue<ListNode*, vector<ListNode*>, decltype(compare)> minHeap(compare);

    // Push all non-null lists' head nodes into the heap
    for (ListNode* list : lists)
      if (list != nullptr)
        minHeap.push(list);

    // Process the heap and construct merged list
    while (!minHeap.empty()) {
      ListNode* minNode = minHeap.top(); // Get the smallest node
      minHeap.pop(); // Remove it from the heap
      
      if (minNode->next) // Push the next node in the list to heap if exists
        minHeap.push(minNode->next);

      curr->next = minNode; // Append to result list
      curr = curr->next; // Move forward
    }

    return dummy.next; // Return merged list starting from dummy's next
  }
};
