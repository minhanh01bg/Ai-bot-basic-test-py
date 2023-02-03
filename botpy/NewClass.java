
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class NewClass {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        FileInputStream fis = new FileInputStream("C:\\Users\\vuanh\\OneDrive\\Desktop\\ex1.txt");
        byte[] data = new byte[1000];
        int i = fis.read(data);
        while (i != -1) {
            System.out.print(new String(data, 0, i, "utf-8"));
            i = fis.read(data);
        }
    }
}
