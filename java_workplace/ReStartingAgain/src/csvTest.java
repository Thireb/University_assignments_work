
// import java.io.File;
import java.io.*;
// import java.nio.*;
import java.nio.charset.StandardCharsets;
import java.util.*;

class csvTest {

    public static void main(String[] args) {

        try {
            File newFile = new File("program.csv");
            if(newFile.createNewFile()) {
                System.out.println("File YES");
            } else {
                System.out.println("File NO, it exists!!!");
            }
            // Path path = Paths.get("program.csv");

            // FileReader file = new FileReader(newFile);
            // BufferedReader bfr = new BufferedReader(file);
            
            // String line = bfr.readLine();
            // String line2 = bfr.readLine();
            // String[] spl1 = line.split(",");
            // String[] spl2 = line2.split(",");

            
            // //  for (String spl : spl1)
            //     //  System.out.println(spl);
            //  //for (String spl : spl2)
            //    // System.out.println(spl);
            // //System.out.println(line);
            // //System.out.println(line2);
            // System.out.println(spl1[0]);
            
            // System.out.println(line); 

            String[] strArray = StandAlone.readCertainLine(newFile, 0);
            for (String spl : strArray)
                 System.out.println(spl);

        } catch (Exception e) {
        	
            System.out.println("FUCK OFF");
        }

    }

} 