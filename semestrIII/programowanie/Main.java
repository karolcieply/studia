import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] tab = new int[n];
        for(int i=0; i<n; i++){
            tab[i] = in.nextInt();
        }
        tab = Algorytm.bubbleSort(tab);
        for (int i : tab) {
            System.out.print(i);            
            System.out.print(",");            
        }

    }
}