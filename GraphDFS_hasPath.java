import java.util.ArrayList;
import java.util.Scanner;

public class GraphDFS_hasPath{
    static class Edges {
        int src;
        int nbr;
        int wt;

        public Edges(int v1, int v2, int wt){
            this.src = v1;
            this.nbr = v2;
            this.wt = wt;
        }
    }
    public static void main(String args[]) throws Exception, NumberFormatException{
        Scanner sc  = new Scanner(System.in);

        int vtces = sc.nextInt();
        ArrayList<Edges> [] graph = new ArrayList[vtces];

        for (int i =0; i < vtces; i++){
            graph[i] = new ArrayList<>();
        }
        int edges = sc.nextInt();
        for(int i= 0; i<edges; i++){
            
            int v1 = sc.nextInt();
            int v2 = sc.nextInt();
            int wt = sc.nextInt();
            graph[v1].add(new Edges(v1, v2, wt));
            graph[v2].add(new Edges(v1, v2, wt));
        }
        int src = sc.nextInt();
        int dest = sc.nextInt();
        boolean[] Visited = new boolean[vtces];
        boolean path = hasPath(graph, src, dest, Visited);
        System.out.println(path);
    }
    public static boolean hasPath(ArrayList<Edges> [] graph, int src, int dest, boolean[] visited){
        if (src == dest){
            return true;
        }
        visited[src] = true;
        for(Edges edge : graph[src]){
            if (visited[edge.nbr] == false){
            boolean hasNbrPath = hasPath(graph, edge.nbr, dest, visited);
            if (hasNbrPath == true){
                return true;
            }
        }
    }
        return false;

    }
}