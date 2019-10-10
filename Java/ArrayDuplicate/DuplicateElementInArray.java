/* To find Duplicate in an array.
 eg.
 input => int[] arr= {1, 3, 4, 5, 7, 8, 4}
 output=> 4

*/

public class DuplicateElementInArray{	

	public static int duplicate(int[] arr){  
         int arrsum=0;
		int nsum;
		int n=arr.length-2;
		nsum=(n*n+n)/2;
		for(int i=0;i<arr.length;i++){
			arrsum=arrsum+arr[i];
			}
		int diff=arrsum-nsum;
		return diff;
	}
}