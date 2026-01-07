class SortArray {
  public static void main(String[] a){
    int[] arr={7,2,5,1};
    for(int i=0;i<arr.length-1;i++)
      for(int j=0;j<arr.length-i-1;j++)
        if(arr[j]>arr[j+1]){
          int t=arr[j]; arr[j]=arr[j+1]; arr[j+1]=t;
        }
    for(int x:arr) System.out.print(x+" ");
  }
}
