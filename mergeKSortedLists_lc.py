from typing import List


#problem link:- https://leetcode.com/problems/merge-k-sorted-lists/



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #simple 
        #merge two lists ata a time
        #time complexity n
        #overall complexity (log(k)*average no of elements)
        l=lists
        if len(lists)==0:
            return None
        while len(l)>1:
            ln=len(l)
            l1=[]
            
            for i in range(ln):
                if i%2==0 and i!=(ln-1):
                    l1.append(self.merge(l[i], l[i+1]))
                elif i%2==0:
                    l1.append(l[i])
            l=l1
        
        return l[0]
    
    
    
    def merge(self, list1, list2):
        if not list1:
            return list2
        elif not list2:
            return list1
        
        
        node1=list1
        node2=list2
        
        if node1.val<=node2.val:
            head=node1
            last=node1
            node1=node1.next
        else:
            head=node2
            last=node2
            node2=node2.next
            
        
        while node1 or node2:
            if not node1:
                # print('not node1')
                last.next=node2
                last=node2
                node2=node2.next
                
            elif not node2:
                # print('not node2')
                last.next=node1
                last=node1
                node1=node1.next
                
            elif node1.val<=node2.val:
                # print('node1<node2')
                last.next=node1
                last=node1
                node1=node1.next
            else:
                # print('node2<node1')
                last.next=node2
                last=node2
                node2=node2.next

        return head        
l1=ListNode(1)
l1.next=ListNode(3)
l1.next.next=ListNode(4)
l1.next.next.next=ListNode(5)
l1.next.next.next.next=ListNode(5)
l1.next.next.next.next.next=ListNode(6)
l1.next.next.next.next.next.next=ListNode(15)

l2=ListNode(3)
l2.next=ListNode(5)
l2.next.next=ListNode(6)
l2.next.next.next=ListNode(8)
l2.next.next.next.next=ListNode(10)
l2.next.next.next.next.next=ListNode(13)
l2.next.next.next.next.next.next=ListNode(148)
l2.next.next.next.next.next.next.next=ListNode(334)


l3=ListNode(0)
l3.next=ListNode(1)
l3.next.next=ListNode(4)
l3.next.next.next=ListNode(8)
l3.next.next.next.next=ListNode(9)
l3.next.next.next.next.next=ListNode(14)
l3.next.next.next.next.next.next=ListNode(14)
l3.next.next.next.next.next.next.next=ListNode(19)

list1=[l1,l2,l3]

s=Solution()
sortedl=s.mergeKLists(list1)
while sortedl is not None:
    print(sortedl.val, end='->')
    sortedl=sortedl.next



"""
class Solution2(object):
    def mergeKLists(self, lists):
        
        # :type lists: List[ListNode]
        # :rtype: ListNode
        
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next

"""


