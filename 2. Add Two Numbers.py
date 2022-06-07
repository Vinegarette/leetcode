# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse linked list
        def reverse_list(nums, head):
            
            while head is not None:
                nums.append(head.val)
                head = head.next
            
            nums.reverse()
        
        # Form number
        
        nums1 = []
        nums2 = []
        
        reverse_list(nums1, l1)
        reverse_list(nums2, l2)        
        
        l1_num = ''.join([str(c) for c in nums1])
        l2_num = ''.join([str(c) for c in nums2])
        
        # print(l1_num)
        # Add together
        
        num3 = str(int(l1_num) + int(l2_num))[::-1]
        
        # Return as linked list
        head = ListNode(num3[0])
        curr = head
        for c in num3[1:]:
            new = ListNode(int(c))
            curr.next = new
            curr = curr.next
            
        return head
        
        
        
