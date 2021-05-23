import java.util.Scanner;
import java.util.Stack;

public class reverseStack {
    public static void main(String [] args){
    Stack<Integer> s = new Stack<Integer>();
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    for(int i=0; i<n; i++){
        int j = sc.nextInt();
        s.push(j);
    }
    s = reverse(s);
    System.out.println("ans:");
    s.forEach(System.out::println);
 }

 static Stack<Integer> reverse(Stack<Integer> stack){
    if (stack.size() == 1){
        return stack;
    }
    int temp = stack.pop();
    stack = reverse(stack);
    stack = insert(stack, temp);
    return stack;
 }

 static Stack<Integer> insert(Stack<Integer> stack, int temp){
     if (stack.size() == 0){
         stack.push(temp);
         return stack;
     } 
     int p = stack.pop();
     stack = insert(stack, temp);
     stack.push(p);
     return stack;
 }
}