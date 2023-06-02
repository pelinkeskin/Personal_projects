package java_solns;

import java.util.Arrays;


class MinMax {
    public static int[] minMax(int[] arr) {
    	Arrays.sort(arr);
    	int min= arr[0];
    	int max = arr[arr.length -1];
    	int []min_max= new int[2];
    	min_max[0]=min;
    	min_max[1]=max;
    	
		return min_max;
        // Your awesome code here
    }
    
	public static void main(String[]args) {
		System.out.println(java.util.Arrays.toString(MinMax.minMax(new int[]{1,2,3,4,5})));
	}
	
}