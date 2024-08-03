import java.util.LinkedList;
import java.util.Queue;
public class linkedlist{
    class Operations{
        void negative(int[] A, int n, int k){
            Queue<Integer> queue = new LinkedList<>();
            int i;
            for (i=0;i<k;i++){
                if(A[i]<0){
                    queue.add(i);
                
                }
            }
            for (; j<n;j++){
                if(!queue.isEmpty()){
                    System.out.println(A[queue]);
                }
            }

        }
    }
}