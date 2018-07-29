package july.page60Problems.chapter1;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class ONE_one_allUniqueCharacters {

	final static String str1="abcd";
	final static String str2="abcdd";
	  static final int NO_OF_CHARS = 256;
	     
	    /* Fills count array with frequency of characters */
	    static void fillCharCounts(String str, int[] count)
	    {
	       for (int i = 0; i < str.length();  i++)
	          count[str.charAt(i)]++;
	    }
	      
	    /* Print duplicates present in the passed string */
	    static void printDups(String str)
	    {
	      // Create an array of size 256 and fill count of every character in it
	      int count[] = new int[NO_OF_CHARS];
	      fillCharCounts(str, count);
	     
	      for (int i = 0; i < NO_OF_CHARS; i++)
	        if(count[i] > 1)
	            System.out.printf("%c,  count = %d \n", i,  count[i]);
	      
	    }
	public static void main(String[] args) 
	{
		System.out.println("checking duplicates with ds start");
		System.out.println("input string is: "+str1);
		checkDuplictaesWithDS(str1);
		System.out.println("input string is: "+str2);
		checkDuplictaesWithDS(str2);
		System.out.println("checking duplicates with ds end");
		System.out.println("checking duplicates without ds start");
		System.out.println("input string is: "+str1);
		checkDuplictaesWithoutDS(str1);
		System.out.println("input string is: "+str2);
		checkDuplictaesWithoutDS(str2);
		System.out.println("checking duplicates without ds end");
		System.out.println("check and print duplicates with ds");
		System.out.println("input string is: "+str1);
		checkandprintDuplicates(str1);
		System.out.println("input string is: "+str2);
		checkandprintDuplicates(str2);
	}
	public static void checkDuplictaesWithoutDS(String str)
	{
		 /*initialize and array of 256 characters 
		and then based on string populate a count array 
		 now using another loop check how many positions have
		 count >1
		 and then print it 
		 */
		printDups(str);
	}
	public static void checkDuplictaesWithDS(String str)
	{
		// extract characters from string
		List<Character> list = new ArrayList<Character>();
		Set<Character> unique = new HashSet<Character>();
		for(char c : str.toCharArray()) {
		    list.add(c);
		    unique.add(c);
		}
		if(str.length()==unique.size())
			System.out.println("no duplicates found");
		else
			System.out.println(" duplicates exist in "+str);
	}
	public static void checkandprintDuplicates(String str)
	{
		 Map<Character, Integer> dupMap = new HashMap<Character, Integer>(); 
	        char[] chrs = str.toCharArray();
	        for(Character ch:chrs){
	            if(dupMap.containsKey(ch)){
	                dupMap.put(ch, dupMap.get(ch)+1);
	            } else {
	                dupMap.put(ch, 1);
	            }
	        }
	        Set<Character> keys = dupMap.keySet();
	        for(Character ch:keys){
	            if(dupMap.get(ch) > 1){
	                System.out.println(ch+" has duplicate count--->"+dupMap.get(ch));
	            }
	        }
	}

}
