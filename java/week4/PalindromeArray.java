class PalindromeArray {
  public static void main(String[] a){
    int[] arr={1,2,3,2,1};
    boolean pal=true;
    for(int i=0,j=arr.length-1;i<j;i++,j--)
      if(arr[i]!=arr[j]) { pal=false; break; }
    System.out.println(pal?"Palindrome":"Not Palindrome");
  }
}
