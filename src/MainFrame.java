//package FirstProject;
import javax.swing.JFrame;
import javax.swing.WindowConstants;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author User
 */
public class MainFrame extends JFrame {
    public void init() {
        setTitle("Welcome");
        setSize(450, 300);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setVisible(true);
    }
    public static void main(String args[]){
        MainFrame ob = new MainFrame();
        ob.init();
    }
}
