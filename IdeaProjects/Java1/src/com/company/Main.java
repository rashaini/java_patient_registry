package com.company;

public class Main {

    public static class ArrayTraversal {

        //why can't the method be static?
        public static void main(String[] args){
            String[] students =  {"Bob", "Ela" , "Alex"};

            // traversing an array
            for (String s: students){
                System.out.println("student: " + s); }
        }
    }
}
