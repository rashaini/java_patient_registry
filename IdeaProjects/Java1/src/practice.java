/**
 * Created by rimahsaini on 10/26/15.
 */
import java.util.Scanner;

public class practice {

    public static void main(String[] args) {
        int studentsNumber;
        String[] students;
        Scanner console = new Scanner(System.in); System.out.print("How many students you want to register? ");
        studentsNumber = console.nextInt();
        students = new String [studentsNumber];
        for(int i = 0; i < studentsNumber; i++) { System.out.print("Enter student name " + (i+1) + ": "); students[i] = console.next();
        }
        System.out.println("\nThe names you entered are:"); for(int i = 0; i < studentsNumber; i++) { System.out.print(students[i] + " ");
        } }
}
