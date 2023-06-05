package java_solns;
/*6 kyu Stop gninnipS My sdroW!
DESCRIPTION:
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
STRINGSALGORITHMS 
 */
public class SpinWords {
	 public String spinWords(String sentence) {
		 
		 //splitting sentence to words
		 String [] sentence_array = sentence.split(" ",-1);
		 // declaring a string to hold new string
		 String new_string="";
		 
		 //looping through sentence array
		 for (String substring: sentence_array) {
			 //if word in sentence array is longer then or equal to 5 chars do;
			 if(substring.length()>=5) {
				 //converting substring to char array
				 char[]substring_chars=new char[substring.length()];
				 substring.getChars(0,substring.length(),substring_chars,0);

				 // declaring a new substring char array 
				 char[]new_substring_array=new char[substring.length()];
				 
				 //declaring a counter variable equal to length of substring char array
				 int array_lenght=substring_chars.length;
				 
				 //looping from 0 to substring_chars array length
				 for (int i=0; i<substring_chars.length; i++) {
					 
					 //adding first char in substring char array to new substring char array in reverse order
					 new_substring_array[array_lenght-1]=substring_chars[i];
					 array_lenght-=1;
				 }
				 
				 // converting new substring chars array to a new substring
				 String new_substring=String.valueOf(new_substring_array);
				
				 // adding new substring to new string
				 new_string+=new_substring+" ";
			 }
			 
			 //if word in sentence array is longer then or equal to 5 chars add it to new string
			 else {
				 //adding substring to new string
				 new_string+=substring+" ";
			 }
			 
		 }
		
		 return new_string.trim();

	}
	 
	public static void main(String[]args) {
		String test_string = new SpinWords().spinWords("emocleW");
			System.out.println(test_string);
		String test_string2 = new SpinWords().spinWords("Hey fellow warriors");
			System.out.println(test_string2);
		}
}
