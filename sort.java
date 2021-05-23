import java.util.ArrayList;
import java.util.Scanner;

class sort{
    public static void main(String [] args){
        ArrayList<Integer> ls = new ArrayList<Integer>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i =0; i<n; i++){
            int j = sc.nextInt();
            ls.add(j);
        }
        ls = sort_ls(ls);
        for(int i =0 ; i<n; i++){
            System.out.println(ls.get(i));
        }
       
    }
    static ArrayList<Integer> sort_ls(ArrayList<Integer> ls){
        if (ls.size() == 1){
            return ls;
        }
        //System.out.println(ls.size());
        int temp = ls.get(ls.size()-1);
        ls.remove(ls.size()-1);
        ls = sort_ls(ls);
        ls = insert(ls,temp);
        return ls;
    }
    static ArrayList<Integer> insert(ArrayList<Integer> ls, int temp){
        if (ls.size() == 0 || ls.get(ls.size()-1) <= temp){
            ls.add(temp);
            return ls;
        }
        int val = ls.get(ls.size()-1);
        ls.remove(ls.size()-1);
        ls = insert(ls, temp);
        ls.add(val);
        return ls;
    }
}