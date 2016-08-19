/**
 * Created by rimahsaini on 10/26/15.
 */
public class Exercise3 {

        public static void main(String [] args){

            int [] numbers = new int [20];
            int i = 0;
            numbers [0]=1;
            for (i=1; i<20; i++){
                numbers[i] = numbers [i-1]*2;

                System.out.println(numbers[i]);
            }
    }




}
