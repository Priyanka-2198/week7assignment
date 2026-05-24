def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for letter in text:
        print("not vowel:", letter)

        if letter in vowels:
            count += 1
            print("Vowel found:", letter)

    return count

print(count_vowels("Hello"))