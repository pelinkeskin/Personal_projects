package java_solns;

public class Factorial {
	public int factorial (int n) {
		int result=1;
		for (int i = 1; i<n+1; i++) {
			result *=i;
		}
		if (n == 0) {
			return 1;
			}
		else if (n<0 || n>12 ) {
			throw new IllegalArgumentException();
		}
		else {
			return result;
			}
	}

	public static void main(String[]args) {
		int fact = new Factorial().factorial(0);
		System.out.println(fact);
	}
}
