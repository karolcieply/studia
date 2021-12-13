public class Algorytm {
    public static int[] bubbleSort(int[] tab){
        int temp = 0;
        for(int i=0; i<tab.length; i++){
            for(int j=1; j<(tab.length-i); j++){
                if(tab[j]<tab[j-1]){
                    temp = tab[j-1];
                    tab[j-1] = tab[j];
                    tab[j] = temp;
                }
            }

        }
        return tab;
    }
}