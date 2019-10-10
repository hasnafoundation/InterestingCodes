// Java code to print middle element in a given LinkedList.
class LinkedListNode<T> {
	public T data;
	public LinkedListNode<T> next;

	public LinkedListNode(T data) {
		this.setData(data);
		this.next = null;
	}

	public T getData() {
		return data;
	}

	public void setData(T data) {
		this.data = data;
	}

}
public class Solution {
	public static int printMiddel(LinkedListNode<Integer> head) {
       LinkedListNode<Integer> fast=head;
      LinkedListNode<Integer> slow=head;
      LinkedListNode<Integer> preslow=head;
      
      if(head!=null){
       while(fast!=null&& fast.next!=null){
        fast=fast.next.next;
         preslow=slow;
        slow=slow.next;
      }
   }  
      return preslow.data;
    }
    
}