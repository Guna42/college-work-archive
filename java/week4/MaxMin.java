import java.util.*;
class MaxMin {
  public static void main(String[] a){
    int[] arr={5,9,-2,7,1};
    int max=arr[0],min=arr[0];
    for(int x:arr){
      if(x>max) max=x;
      if(x<min) min=x;
    }
    System.out.println("Max="+max+" Min="+min);
  }
}
