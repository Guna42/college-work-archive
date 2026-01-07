class MergeArrays {
  public static void main(String[] a){
    int[] a1={1,2}, a2={3,4};
    int[] merged=new int[a1.length+a2.length];
    int k=0;
    for(int x:a1) merged[k++]=x;
    for(int x:a2) merged[k++]=x;
    for(int x:merged) System.out.print(x+" ");
  }
}
