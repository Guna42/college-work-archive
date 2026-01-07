class ReverseArray {
  public static void main(String[] a){
    int[] arr={1,2,3,4};
    for(int i=0,j=arr.length-1;i<j;i++,j--){
      int t=arr[i]; arr[i]=arr[j]; arr[j]=t;
    }
    for(int x:arr) System.out.print(x+" ");
  }
}
