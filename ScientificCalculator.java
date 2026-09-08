import java.util.Scanner;

public class ScientificCalculator {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int choice = -1;

        while (choice != 0) {

            System.out.println("\n===== JAVA MATH CALCULATOR =====");
            System.out.println("1. Power");
            System.out.println("2. Square Root");
            System.out.println("3. Absolute Value");
            System.out.println("4. Maximum");
            System.out.println("5. Minimum");
            System.out.println("6. Sin");
            System.out.println("7. Cos");
            System.out.println("8. Tan");
            System.out.println("9. Log10");
            System.out.println("10. Round");
            System.out.println("0. Exit");

            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            double a, b, result;

            switch (choice) {

                case 1:
                    System.out.print("Enter base: ");
                    a = sc.nextDouble();

                    System.out.print("Enter power: ");
                    b = sc.nextDouble();

                    result = Math.pow(a, b);
                    System.out.println("Result = " + result);
                    break;

                case 2:
                    System.out.print("Enter number: ");
                    a = sc.nextDouble();

                    result = Math.sqrt(a);
                    System.out.println("Square Root = " + result);
                    break;

                case 3:
                    System.out.print("Enter number: ");
                    a = sc.nextDouble();

                    result = Math.abs(a);
                    System.out.println("Absolute Value = " + result);
                    break;

                case 4:
                    System.out.print("Enter first number: ");
                    a = sc.nextDouble();

                    System.out.print("Enter second number: ");
                    b = sc.nextDouble();

                    result = Math.max(a, b);
                    System.out.println("Maximum = " + result);
                    break;

                case 5:
                    System.out.print("Enter first number: ");
                    a = sc.nextDouble();

                    System.out.print("Enter second number: ");
                    b = sc.nextDouble();

                    result = Math.min(a, b);
                    System.out.println("Minimum = " + result);
                    break;

                case 6:
                    System.out.print("Enter angle: ");
                    a = sc.nextDouble();

                    result = Math.sin(Math.toRadians(a));
                    System.out.println("Sin = " + result);
                    break;

                case 7:
                    System.out.print("Enter angle: ");
                    a = sc.nextDouble();

                    result = Math.cos(Math.toRadians(a));
                    System.out.println("Cos = " + result);
                    break;

                case 8:
                    System.out.print("Enter angle: ");
                    a = sc.nextDouble();

                    result = Math.tan(Math.toRadians(a));
                    System.out.println("Tan = " + result);
                    break;

                case 9:
                    System.out.print("Enter number: ");
                    a = sc.nextDouble();

                    result = Math.log10(a);
                    System.out.println("Log10 = " + result);
                    break;

                case 10:
                    System.out.print("Enter decimal number: ");
                    a = sc.nextDouble();

                    result = Math.round(a);
                    System.out.println("Rounded = " + result);
                    break;

                case 0:
                    System.out.println("Calculator closed.");
                    break;

                default:
                    System.out.println("Invalid choice!");
            }
        }

        sc.close();
    }
}