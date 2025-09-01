'''Task 2: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
 
Expected Output:
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]'''

numbers = list(range(1,11))

extracted = numbers[:5]

reversed_extracted = extracted[::-1]

print(f"Original list: {numbers}")
print(f"Extracted first five elements: {extracted}")
print(f"Reversed extracted elements: {reversed_extracted}")