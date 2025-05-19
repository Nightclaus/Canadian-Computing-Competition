import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

class Main {
    public static Scanner potato = new Scanner(System.in);

    static String input(String text) {
        if (text != null) {System.out.println(text);}
        return potato.nextLine();
    }
    public static void main(String[] args) {
        int maxInputs = Integer.parseInt(input(null));
        int radius = maxInputs / 2;
        List<String> array = new ArrayList<>();
        for (int i = 0; i < maxInputs; i++) {
            //System.out.println(i);
            array.add(input(null));
        }
        //String[] halfOfList = array.subList(0, radius).toArray(new String[0]);
        int results = 0;
        for (int i = 0; i < radius; i++) {
            if (array.get(i).equals(array.get(i+radius))) {
                results += 2;
            }
        }
        System.out.println(results);
    }
}