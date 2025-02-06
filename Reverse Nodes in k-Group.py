class Solution {
 public:
  ListNode* reverseKGroup(ListNode* head, int k) {
    if (head == nullptr) 
      return nullptr;

    ListNode* tail = head;

    // Check if there are at least k nodes to reverse
    for (int i = 0; i < k; ++i) {
      if (tail == nullptr)  // If fewer than k nodes, return head as is
        return head;
      tail = tail->next;
    }

    // Reverse the first k nodes
    ListNode* newHead = reverse(head, tail);
    
    // Recursively process the remaining list
    head->next = reverseKGroup(tail, k);
    
    return newHead;
  }

 private:
  // Reverses nodes in the range [head, tail) (excluding tail)
  ListNode* reverse(ListNode* head, ListNode* tail) {
    ListNode* prev = nullptr;
    ListNode* curr = head;
    
    while (curr != tail) {
      ListNode* next = curr->next; // Store next node
      curr->next = prev; // Reverse current node's pointer
      prev = curr; // Move prev forward
      curr = next; // Move curr forward
    }
    
    return prev; // Return new head of the reversed segment
  }
};
