```
// Allows the "System" library to be used, which includes the Console class and WriteLine function
using System;

// Namespaces are used to organise code into logical groups, and also prevents name collisions
namespace HelloWorld
{
    class Program
    {
        // "static" means that Main() doesn't belong to a specific object
        // "void" means that main() returns no value
        static void Main(string[] args)
        {
            Console.Write("Hello Jake! ");
            Console.WriteLine("How do you do?");

            int answer = 32;
            Console.WriteLine("The number is " + answer);

            answer = 50;
            Console.WriteLine("The number is now " + answer);

            const double e = 2.718;
            Console.WriteLine("The constant e in logarithms = " + e);


            // setting other variable data types
            char letter = 'D';
            bool state = true;
            string sentence = "Hello";


            // convert int to string
            Console.WriteLine(Convert.ToString(answer));


            // Type your username and press enter
            Console.WriteLine("Enter username:");

            // Create a string variable and get user input from the keyboard and store it in the variable
            string userName = Console.ReadLine();

            // Print the value of the variable (userName), which will display the input value
            Console.WriteLine("Username is: " + userName);

        }
    }
}
```
