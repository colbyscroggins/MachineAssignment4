# About
 This program uses the Cleve Moler Algorith to calculate machine precision. The input is hardcoded and the output is a single number (eps) representing machine precision.

# Analysis
 $$eps = 2.220446049250313 × 10^(-16)$$
 $$\sqrt{eps} = 1.4901161193847656 × 10^(−8)$$



# Requirements

 * Java Development Kit 21
 * No libraries or built-in functions are required to execute the program

# Compilation

 The program can be compiled with the included Gradle wrapper by running:

 ```
 ./gradlew build
 ```

# Execution

 After compiling, the program can be executed with the Gradle run task:

 ```
 ./gradlew run
 ```

# Sample Execution & Output

 Sample Compilation:
 ```
 ./gradlew build
 ```

 Sample Execution:
 ```
 ./gradlew run
 ```

 Sample Output:
 ```
 2.220446049250313E-16
 ```