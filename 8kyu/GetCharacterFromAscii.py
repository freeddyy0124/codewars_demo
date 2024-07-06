# Write a function which takes a number and returns the corresponding ASCII char for that value.

# Example:

# 65 --> 'A'
# 97 --> 'a'
# 48 --> '0

def get_char(c):
    
    try:
        return chr(c)
    except ValueError:
        return "Invalid input, not in range"
    