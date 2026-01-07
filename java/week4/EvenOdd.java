class EvenOdd {
  public static void main(String[] a){
    int[] arr={2,5,8,11};
    int even=0,odd=0;
    for(int x:arr) if(x%2==0) even++; else odd++;
    System.out.println("Even="+even+" Odd="+odd);
  }
}
