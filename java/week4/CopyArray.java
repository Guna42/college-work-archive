class CopyArray {
  public static void main(String[] a){
    int[] arr1={4,7,2};
    int[] arr2=new int[arr1.length];
    for(int i=0;i<arr1.length;i++) arr2[i]=arr1[i];
    for(int x:arr2) System.out.print(x+" ");
  }
}
