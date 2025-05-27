from itertools import permutations

def solve_cryptarithmetic(word1, word2, result):
    # Get all unique letters
    unique_letters = set(word1 + word2 + result)
    if len(unique_letters) > 10:
        print("❌ Too many unique letters (max 10 allowed).")
        return

    letters = tuple(unique_letters)
    digits = range(10)

    for perm in permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        # No leading zeroes
        if (mapping[word1[0]] == 0 or
            mapping[word2[0]] == 0 or
            mapping[result[0]] == 0):
            continue

        # Convert word to number
        def word_to_number(word):
            return int(''.join(str(mapping[char]) for char in word))

        num1 = word_to_number(word1)
        num2 = word_to_number(word2)
        num_result = word_to_number(result)

        # Check if it satisfies the equation
        if num1 + num2 == num_result:
            print("✅ Solution Found!")
            print(f"{word1}: {num1}")
            print(f"{word2}: {num2}")
            print(f"{result}: {num_result}")
            print("Mapping:", mapping)
            return

    print("❌ No solution found.")

# 🚀 Take user input
word1 = input("Enter the first word: ").upper()
word2 = input("Enter the second word: ").upper()
result = input("Enter the result word: ").upper()

solve_cryptarithmetic(word1, word2, result)
