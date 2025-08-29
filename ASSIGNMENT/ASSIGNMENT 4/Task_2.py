'''Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
 

Expected Output:
 For example, if the user enters 25, the output should be:

Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.
Enter additional text to append: Learning file handling in Python.
Data successfully appended.
Final content of output.txt:

Hello, Python!
Learning file handling in Python.'''

try:
    file = open('output.txt', 'w')
    user_input = input("Enter text to write to the file:")
    file.write(user_input + "\n")
    file.close()
    print("Data successfully written to output.txt.")
    file = open('output.txt', 'a')
    additional_input = input("Enter additional text to append: ")
    file.write(additional_input + "\n")
    file.close()
    print("Data successfully appended.")
    file = open('output.txt', 'r')
    final_content = file.read()
    file.close()
    print("Final content of output.txt:")
    print(final_content)
except Exception as e:
    print("Error:", e)