package machineassignment4;

public class MachineAssignment4 {

    public static void main(String[] args) {
        
        double a = 4.0 / 3.0;
        double b = a - 1.0;
        double c = b + b + b;

        double eps = Math.abs(1.0 - c);

        System.out.println(eps);
    }
}
