public class Dane implements Comparable<Dane>{
    String imie,numerTelefonu;
    public Dane(String imie,String numerTelefonu){
        this.imie=imie;
        this.numerTelefonu=numerTelefonu;
    }
    public String getPhoneNumber(){
        return this.numerTelefonu;
    }
    public String getImie(){
        return this.imie;
    }
    @Override
    public int compareTo(Dane dane){
        return -this.imie.compareTo(dane.imie);
    }
}
