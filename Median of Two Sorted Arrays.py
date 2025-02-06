class Solution {
 public:
  double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    const int n1 = nums1.size();
    const int n2 = nums2.size();
    
    // Ensure nums1 is the smaller array to optimize binary search
    if (n1 > n2)
      return findMedianSortedArrays(nums2, nums1);

    int l = 0, r = n1; // Binary search boundaries

    while (l <= r) {
      const int partition1 = (l + r) / 2;
      const int partition2 = (n1 + n2 + 1) / 2 - partition1;

      // Get boundary elements, handling edge cases with INT_MIN and INT_MAX
      const int maxLeft1 = (partition1 == 0) ? INT_MIN : nums1[partition1 - 1];
      const int maxLeft2 = (partition2 == 0) ? INT_MIN : nums2[partition2 - 1];
      const int minRight1 = (partition1 == n1) ? INT_MAX : nums1[partition1];
      const int minRight2 = (partition2 == n2) ? INT_MAX : nums2[partition2];

      // Valid partition found
      if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
        return (n1 + n2) % 2 == 0
