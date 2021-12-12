import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;
public class Main{
    public static void main(String[] args){
        Dane tab[] = new Dane[3];
        tab[0] = new Dane("ghi","789");
        tab[1] = new Dane("def","456");
        tab[2] = new Dane("abc","123");
        Arrays.sort(tab);
        for (Dane dane : tab) {
            System.out.println(dane.getImie());            
        }
    }
}
