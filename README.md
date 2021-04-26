# Java-Slicer-Version-1.0-
Download the slicer file (rutvik.cpp), any of the source file and the GUI code.

Pre-requisites:
    
      -- Java Compiler
      -- Python
      -- The name of the test file should be "source.java" and in the class name should be intuitively "Source"
      -- To slice the statements excecuted under loop, please enter the line numbe like "linenumber_counter":
            For example there is 37th line of the code and if it is present inside some loop, then inorder to slice 4th iteration of that 37th line the input should be "37_3" 

        
# How it Works?

Method 1 : Using the GUI 

Open a Python terminal and run the GUI using the command "py app.py"
After successfully executing the command, you will be guided to a file selecter window to select the Java code file to slice it.
Select the file and after succefully completing previous step, you will be able to see a GUI which is as shown below :

![UI_1](https://user-images.githubusercontent.com/34269503/116076551-013b8700-a6b2-11eb-8922-63e79a161bc2.jpg)

Left side of the window is a frame which gives the preview of the code (scrollable) and right side's frame is used to give the inputs.
Inputs are as follows:

      -- Variable name : Enter the name of the variable for which you want to check the slice
      -- Input : This input is dedicated to the input given to the Java code (which you are slicing), give the program input since slicer will calculate dynamic slice
      -- Line number : Enter the line number of the variable which you want to check the slice

Above inputs are as shown here:

![UI_2](https://user-images.githubusercontent.com/34269503/116076911-7c04a200-a6b2-11eb-84db-b109a9acc908.png)

On executing the "run" button, you will be provided with the 2 outputs:

      -- 1. The respective dynamic slice for your input
      -- 2. The dependency graph of the slice from the program
      
Following image shows you the output of the tested java Program and the slice of the program:

![UI_3](https://user-images.githubusercontent.com/34269503/116077200-d6056780-a6b2-11eb-870c-c100e1f24c88.png)

Following image shows you the dependency graph of the program:

![UI_4](https://user-images.githubusercontent.com/34269503/116077336-00572500-a6b3-11eb-9a78-af6a4cb617fc.png)

Method 2: Without using GUI (Directly from the terminal)

If there is no python support then also you can directly run the slicer from the terminal

  Prequisite:
      -- 1. Text File : named "inputt1" - This file shoud have 2 things written in it, first one the line number and second the variable name
      -- 2. Text File : named "inputt2" - This file shoud have the input of the Java code which is to be tested
      
Following images show both the files for the code mentioned in the above example (in the example of GUI method):

![UI_5](https://user-images.githubusercontent.com/34269503/116078495-4fea2080-a6b4-11eb-923b-c7a1ad38264e.png)

![UI_6](https://user-images.githubusercontent.com/34269503/116078521-58425b80-a6b4-11eb-8c89-3fa38473a9f1.png)

After manually writing the two files, open the terminal and compile the slicer code with following command "g++ -o x rutvikk.cpp"
After successfully compiling, run the slicer in the terminal with the command ".\x" and you will achieve the slice for the inputs mentioned by you in the "inputt1.txt"

Following image shows the result acheived in the terminal for the above inputs:

![UI_7](https://user-images.githubusercontent.com/34269503/116078795-aa837c80-a6b4-11eb-95be-8644e7db1f2e.png)


# Following functionalities for slicing of Java Code is achieved in this 1.0 version

    -- Basic Parsing of Java Code
    -- Parsing of Dependencies (All the import statements)
    -- Parsing and handling of basic functions in Java
    -- For loop
    -- While loop
    -- If else
    -- Try catch block
    -- Return statements
    -- Data Types (int, float, double, string, void, long)
    -- Scanner class
    -- Methods : Public static methods (void and int)
    -- Threading : Basic methods (object.start(), run method, thread.getid())
    -- API calls
    -- Iterators
    -- Arithmetic operations
    -- String operations
    -- Assignment operations
    
    















      
