#### Initiating classes
```c#
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
        }
    }
}
```

<br>

#### Setting and rewriting variables
```c#
int answer = 32;
Console.WriteLine("The number is " + answer);

answer = 50;
Console.WriteLine("The number is now " + answer);
```

<br>

#### Setting other variable data types
```c#
char letter = 'D';
bool state = true;
string sentence = "Hello";
```

<br>

#### Setting a constant variable
Attempting to change this variable later in the code will result in an error
```c#
const double e = 2.718;
Console.WriteLine("The constant e in logarithms = " + e);
```

<br>

#### Converting int to string
```c#
Console.WriteLine(Convert.ToString(answer));
```

<br>

#### User inputs
```c#
// Type your username and press enter
Console.WriteLine("Enter username:");

// Create a string variable and get user input from the keyboard and store it in the variable
string userName = Console.ReadLine();

// Print the value of the variable (userName), which will display the input value
Console.WriteLine("Username is: " + userName);
```

<br>

#### Maths

Finding the maximum value between multiple values
```c#
Console.WriteLine(Math.Max(5, 10));
```

Finding the maximum value between multiple values
```c#
Console.WriteLine(Math.Min(5, 10));
```

Finding the maximum value between multiple values
```c#
Console.WriteLine(Math.Sqrt(64));
```











