package java_solns;


public class PhoneNumber {
	public static String createPhoneNumber(int[] numbers) {
		
		String first_3 = "";
		String second_3 = "";
		String last_4 = "";
		
		for (int i=0; i <3; i++) {
			first_3 += Integer.toString(numbers[i]);
		} 
		

		for (int i=3; i <6; i++) {
			second_3 += Integer.toString(numbers[i]);
		}
		
		
		for (int i=6; i <10; i++) {
			last_4 += Integer.toString(numbers[i]);
		}

		String result = new String("("+first_3+") "+second_3+"-"+last_4);
		return result;
	}

	public static void main(String[]args) {
		System.out.println(PhoneNumber.createPhoneNumber(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}));
	}
	
}

