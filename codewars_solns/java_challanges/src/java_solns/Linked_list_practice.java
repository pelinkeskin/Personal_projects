package java_solns;
/* 
6 kyu  Node Mania
This kata is about singly linked list. 
A linked list is an ordered set of data elements, 
each containing a link to its successor (and sometimes its predecessor, known as a double linked list). 
You are you to implement an algorithm to find the kth to last element.

For example given a linked list of:
For example given a linked list of:

a -> b -> c -> d

if k is the number one then d should be returned
if k is the number two then c should be returned
if k is the number three then b should be returned
if k is the number four then a should be returned
if k exceeds the size of the list then null returned
Special Note --> Node classes contain two fields; data and next. 
So if you want to assign an int the node data from Node node do int example = node.data
 */
import java.util.ArrayList;

class Node
{
    int data;
    Node next;
    Node(int d)
    {
        data = d;
        next = null;
    }
}
// above class copied from https://www.geeksforgeeks.org/what-is-linked-list/ and class inherited it to be able to run
// this challenge locally while challenge only asks to implement searchKFromEnd method.

public class Linked_list_practice {
	  public static Integer searchKFromEnd(Node linkedList, int k){
		    
		    Node a = linkedList;
		    ArrayList<Integer> mylist =new ArrayList<Integer>();
		    while (a != null) {
		    	mylist.add(a.data);
		    	a = a.next;
		    	}
		    if (k> mylist.size()) {
		    	return null;
		    }else {
		    	return mylist.get(mylist.size()-k);
		    }

		  }

}
