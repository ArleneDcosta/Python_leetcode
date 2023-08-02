from itertools import izip_longest as zip_longest

def multiply(num1, num2):
    if num1 == "0" or num2 == "0": 
        return "0"
    
    # Reverse both numbers.
    first_number = num1[::-1]
    second_number = num2[::-1]
    print first_number
    print second_number
    # For each digit in second_number, multipy the digit by first_number and then
    # store the multiplication result (reversed) in the results array.
    results = []
    for index, digit in enumerate(second_number):
        print(digit,index,first_number)
        results.append(multiply_one_digit(digit, index, first_number))
    print(results)
    # Add all of the results together to get our final answer (in reverse order)
    answer = sum_results(results)

    # Reverse answer and join the digits to get the final answer.
    return ''.join(str(digit) for digit in reversed(answer))

def multiply_one_digit( digit2, num_zeros, first_number) :
    """Multiplies first_number by a digit from second_number (digit2)."""
    # Insert zeros at the beginning of the current result based on the current digit's place.
    print('Inside')
    current_result = [0] * num_zeros
    print(current_result)
    carry = 0

    # Multiply each digit in first_number with the current digit of the second_number.
    for digit1 in first_number:
        multiplication = int(digit1) * int(digit2) + carry
        # Set carry equal to the tens place digit of multiplication.
        carry = multiplication // 10
        # Append last digit to the current result.
        current_result.append(multiplication % 10)

    if carry != 0:
        current_result.append(carry)
    print current_result
    return current_result

def sum_results(results) :
    # Initialize answer as a number from results.
    answer = results.pop()
    print('Answeer',answer)
    # Add each result to answer one at a time.
    for result in results:
        new_answer = []
        carry = 0
        # Sum each digit from answer and result. Note: zip_longest is the
        # same as zip, except that it pads the shorter list with fillvalue.
        for digit1, digit2 in zip_longest(result, answer, fillvalue=0):
            # Add current digit from both numbers.
            curr_sum = digit1 + digit2 + carry
            # Set carry equal to the tens place digit of curr_sum.
            carry = curr_sum // 10
            # Append the ones place digit of curr_sum to the new answer.
            new_answer.append(curr_sum % 10)

        if carry != 0:
            new_answer.append(carry)

        # Update answer to new_answer which equals answer + result
        answer = new_answer

    return answer
    
print multiply(num1 = "123", num2 = "456")
