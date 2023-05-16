package java_solns;

import java.lang.Math;
public class Prime {
	  public static boolean isPrime(int num) {
		  if (num<=1) 
			  return false;
		  else if (num ==2) 
			  return true;
		  else if (num %2 ==0)
			  return false;

		  for(int i = 3; i < Math.sqrt(num)+1; i+=2) {
			  if (num% i==0)
				  return false;
			  }
		  return true;
		  }

		public static void main(String[]args) {

			System.out.println(Prime.isPrime(75));
		}
}
