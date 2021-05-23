import java.util.Scanner;
import java.util.Stack;

public class delMidNodeOfStack {
    public static void main(String [] args){
    Stack<Integer> s = new Stack<Integer>();
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    for(int i=0; i<n; i++){
        int j = sc.nextInt();
        s.push(j);
    }
    int k = s.size()/2 +1;
    s = Solve(s,k);
    System.out.println("ans:");
    s.forEach(System.out::print);
        
    
}

 static Stack<Integer> Solve(Stack<Integer> s, int k){
     if (k == 1){
         s.pop();
         return s;
     }
     int temp = s.pop();
     s = Solve(s, k-1);
     s.push(temp);
     return s;

     

 }
}