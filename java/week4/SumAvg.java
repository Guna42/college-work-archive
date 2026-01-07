class SumAvg {
  public static void main(String[] a){
    int[] arr={3,6,9,12};
    int sum=0;
    for(int x:arr) sum+=x;
    System.out.println("Sum="+sum+" Avg="+(sum/(double)arr.length));
  }
}
