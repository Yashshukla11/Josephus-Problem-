def josephus(n):
    # Convert n to binary
    binary = bin(n)[2:]
    
    # Move the first digit to the end
    rotated = binary[1:] + binary[0]
    
    # Convert the new binary number back to decimal
    return int(rotated, 2)

# Example usage
n = 41324
last_person = josephus(n)
print("The last person standing is at position", last_person)
