package java_solns;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Collections;
public class EnoughIsEnough {
	public static int[] deleteNth(int[] elements, int maxOccurrences) {
		//creating hashmap to hold key(element)/value(occurance) pairs.
				HashMap<Integer, Integer> mydict =new HashMap<Integer, Integer>();
				int count;
				for(int i=0; i<elements.length;i++) {
					if(mydict.get(elements[i])==null) {
						mydict.put(elements[i],1);
					}
					else {
						count=mydict.get(elements[i]);
						count++;
						mydict.put(elements[i],count);
					}
				}
				
				//creating an arrayList to hold new array
				ArrayList<Integer> listv0 = new ArrayList<Integer>();		
				// looping the array from the end
				for(int i=elements.length-1; i>=0; i-- ) {
					//comparing if elements occurance at hashmap bigger then max occurance
					// if bigger decrement occurance at hashmap and pass
					//if not bigger then add element to array list
					if(mydict.get(elements[i])>maxOccurrences) {
						mydict.put(elements[i],mydict.get(elements[i])-1);
					}
					else {
						listv0.add(elements[i]);
					}
				}
				Collections.reverse(listv0);
				int[]listv1 = new int[listv0.size()];
				
				for (int i=0; i < listv1.length; i++)
					
			    {
			        listv1[i] = listv0.get(i).intValue();
			    }
				return listv1;
				
			}

}
