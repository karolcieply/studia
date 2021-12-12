public class Algorytm {
    public static int search(int[] tab){
        int index=0;
        int min = tab[0];
        for (int i = 0;i<tab.length;i++) {
            if(min>tab[i]){
                min=tab[i];
                index=i;
            }
        }
        return index;
    }
    public static int avg(int[] tab){
        int suma=0;
        for (int i : tab) {
            suma+=i;            
        }
        return suma/tab.length;
    }
   }