def safe_divide(numerator, denominator) :
    try :
       result = int(numerator) / int(denominator)
       return f"The result of the division is {result}"
    except ZeroDivisionError:
        return"Error: Cannot divide by zero."
    except ValueError:
        return"Error: Please enter numeric values only."
