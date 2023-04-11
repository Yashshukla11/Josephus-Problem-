def find_last_soldier(n):
    # Create a list of soldiers and set all values to True (alive)
    soldiers = [True] * n

    # Start the killing cycle with the soldier at position 0
    current_soldier = 0
    while sum(soldiers) > 1:  # Continue the cycle until only one soldier remains
        # Find the next soldier to be killed (the next alive soldier)
        next_soldier = (current_soldier + 1) % n
        while not soldiers[next_soldier]:
            next_soldier = (next_soldier + 1) % n

        # Kill the next soldier
        soldiers[next_soldier] = False

        # Update the current soldier to the next alive soldier
        current_soldier = (next_soldier + 1) % n
        while not soldiers[current_soldier]:
            current_soldier = (current_soldier + 1) % n

    # Find the position of the last surviving soldier
    last_soldier = soldiers.index(True) + 1

    return last_soldier

# Example usage
n = 41324
last_soldier = find_last_soldier(n)
print("The last surviving soldier is at position", last_soldier)
