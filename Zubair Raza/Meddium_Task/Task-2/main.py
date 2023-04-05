def roman_to_int(roman):
    
# Converts a Roman numeral string to an integer.

    # Initialize a dictionary to map Roman numerals to integers
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize the result and the previous numeral value
    result = 0
    num = 0
    
    # Loop through the string in reverse order
    for c in reversed(roman):
        # Get the integer value of the current Roman numeral
        general = roman_to_int[c]
        
        # If the previous numeral value is less than the current value, subtract it from the result
        if num > general:
            result -= general
        # Otherwise, add it to the result
        else:
            result += general
        
        # Update the previous numeral value
        num = general
    
    # Return the final result
    return result
roman_to_int('III')
roman_to_int('IV')
roman_to_int('IX')
roman_to_int('LVIII')
roman_to_int('MCMXCIV')


