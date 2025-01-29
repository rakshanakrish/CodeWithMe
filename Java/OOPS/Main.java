package OOPS;

/*no package*/
import java.util.*;
import java.lang.*;
import java.io.*;

//Base class
class Vehicle {  // Renamed to follow Java naming conventions
    String brand;
    
    void showBrand() {
        System.out.println("brand: " + brand);
    }
}

class Car extends Vehicle {  // Changed class name to match Java conventions
    String model;
    
    void showModel() {
        System.out.println("model: " + model); // Added missing space in output
    }
}

public class Main {
    public static void main(String[] args) {
        Car myCar = new Car(); // dynamic array is always used in java

        // Set values for inherited and new properties
        myCar.brand = "Toyota";
        myCar.model = "Corolla";

        // Access methods
        myCar.showBrand();
        myCar.showModel();
    }
}
