/**
 * 
 * Merge k sorted linked lists and return it as one sorted list. 
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 19, 2015
 *
 */

import java.util.ArrayList;
import java.util.List;

public class MergeKSortedList {
	
    public ListNode mergeKLists(List<ListNode> lists) {
    	//if(lists.size() == 1){
    	//	return lists.get(0);
    	//}
    	
    	List<ListNode> pointerList = new ArrayList<ListNode>();
    	for(ListNode head : lists){
    		pointerList.add(head);
    	}
    	
    	int size = pointerList.size();
    	ListNode pseudoHead = new ListNode(0);
    	ListNode next = null, iter = pseudoHead;
    	
    	int nullCount, min, min_i;
    	
    	while(true){	
    		nullCount = 0;
    		min = Integer.MAX_VALUE;
    		min_i = 0;
    		
    		for(int i=0; i<size; ++i){
    			ListNode head = pointerList.get(i);
    			
    			if(head == null){
    				nullCount ++;
        			continue;	
    			}
    			
    			if(head.val <= min){
    				next = head;
    				min = head.val;
    				min_i = i;
    			}
    		}
    		
    		if(nullCount == size-1 || next == null){
    			break; // Reach all tails of the lists but one.
    		}
    		
    		iter.next = next;
    		iter = next;
    		
			pointerList.set(min_i, next.next); // move on
    	}
    	
    	iter.next = next;
    	
    	return pseudoHead.next;
    }
    
    public static void main(String[] args) {
    	ListNode l1 = Utils.array2LinkedList(new int[]{});
    	
    	//ListNode l1 = Utils.array2LinkedList(new int[]{1, 3, 4, 6});
    	//ListNode l2 = Utils.array2LinkedList(new int[]{2, 5, 7, 10});
    	//ListNode l3 = Utils.array2LinkedList(new int[]{9, 11});
    	
    	List<ListNode> lists = new ArrayList<ListNode>();
    	lists.add(l1);
    	//lists.add(l2);
    	//lists.add(l3);
    	
    	MergeKSortedList solution = new MergeKSortedList();
    	
    	ListNode head = solution.mergeKLists(lists);
    	Utils.printLinkedNodeList(head);
	}

}