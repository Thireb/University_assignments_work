import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class StandAlone {

    public static String[] readCertainLine(File file, int num) throws Exception {
    	String[] strArray = null;
    	try {
            FileReader fileRead = new FileReader(file);
            BufferedReader bfr = new BufferedReader(fileRead);
            String str = null;
            
            for (int i = 0; i <= num; i++) {
                str = bfr.readLine();
                if(num == i) {
                    strArray = str.split(",");
                }
            }
            return strArray;
        } catch (Exception e) {
            return null;
        }
    }
    
    public static String readLine(File file, int num) throws Exception {
    	String strArray = null;
    	try {
            FileReader fileRead = new FileReader(file);
            BufferedReader bfr = new BufferedReader(fileRead);
            String str = null;
            
            for (int i = 0; i <= num; i++) {
                str = bfr.readLine();
            }
            return strArray;
        } catch (Exception e) {
            return null;
        }
    }
    
	public static void writeLine(File file, ArrayList<String> strLine) {
        try {
            FileWriter filewrite = new FileWriter(file);
            for (String strings : strLine) {
                filewrite.append(strings);
                filewrite.append('\n');
            }
            filewrite.flush();
            filewrite.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static ArrayList<String> replace(ArrayList<String> list, int indexToReplace, String stringReplace) {
        list.remove(indexToReplace);
        list.add(indexToReplace, stringReplace);
        return list;
    }

} // class