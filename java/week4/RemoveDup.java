import java.util.*;
class RemoveDup {
  public static void main(String[] a){
    int[] arr={1,2,2,3,1};
    boolean[] seen=new boolean[arr.length];
    for(int i=0;i<arr.length;i++){
      if(seen[i]) continue;
      System.out.print(arr[i]+" ");
      for(int j=i+1;j<arr.length;j++)
        if(arr[i]==arr[j]) seen[j]=true;
    }
  }
}
