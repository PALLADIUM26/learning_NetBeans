import java.io.*;

public class CallPython {
    public void send(String number, String text) {
        try {
            ProcessBuilder builder = new ProcessBuilder("python", "src\\test2.py", number, text);
            Process process = builder.start();
            
            BufferedReader br = new BufferedReader(new InputStreamReader(process.getInputStream()));
            BufferedReader br2 = new BufferedReader(new InputStreamReader(process.getErrorStream()));
            
            String lines = null;
            while ((lines = br.readLine()) != null) {
                System.out.println(lines);
            }
            
            while ((lines = br2.readLine()) != null) {
                System.out.println(lines);
            }
            
        } catch(Exception e) {
            System.out.println(e);
        }
    }
    
    public static void main(String arg[]) {
        String number = "11111";
        String text = "hello";
        
        new CallPython().send(number, text);
    }
}
