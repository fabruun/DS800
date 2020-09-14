


#%% Exercise 2: I wanna play a game
# 1. Tjek om spilleren har lyst til at spille
# 2. Generer et ttilfældigt tal mellem 1 0g 1000
# 3. Lad brugeren gætte et tal
# 4. For tæl brugeren om gættet er størrer eller mindre end vores hemmelige tal.
# 5. Stop og ønsk tillyke når brugeren har gættet tallet
#%% import
import random

user_input = input("You wanna play a game? enter y or yes\n")

if user_input == 'y' or user_input == "yes":
    print("Let the games begin.")
    print("Guess our secret number between 1 and 1000")
    secret_number = random.randint(1, 1000)
    print(secret_number)
    
    user_guess = int(input("yours guess: "))
    
    while user_guess != secret_number:
        if user_guess > secret_number:
            print("Your guess too high")
        else:
            print("Your guess is too low")
            
        user_guess = int(input("please guess again: "))
    print(f"Congratulations you guessed correctly! Your guess was {user_guess}")
    

#%% String formatting

navn = "Dorthe"
et_tal = 42
print("Hej " + str(et_tal) + " du er flink")
print(f"Hej {et_tal} du er flink")
print("Hej {} du er flink".format(et_tal))

#%% Exercise 3_ Relation between numbers

# TODO 
# 1. Bed om 2 tal fra brugeren
# 2. Sammenlign de 2 tal, er det første tal større eller mindre end det andet
# er de lige med hinanden

first_number = int(input("Give the first number: "))
second_number = int(input("Give me the second number: "))

if first_number == second_number:
    print("{} is equal to {}".format(first_number, second_number))

elif first_number > second_number:
    print("{} is greater than {}".format(first_number, second_number))
    
else:
    print("{} is lower than {}".format(first_number, second_number))
    
    
#%% Exercise 4: Fun with strings and vowels

# TODO
# 1. Tag imod input fra brugeren (et ord eller en sætning)
# 2. Tjek om alle vokaler er tilstede i sætning (a, e, i, o, u)
# 3. Tjek hvor mange vokaler der er i alt
# 4. Tjek om sætningen starter med a og slutter med z
# Genrelt - Udskriv de rigtige ting til brugeren

user_input = input("Write a sentence or a word: ")

vowel_string = "aeiou"

all_vowels = True
for vowel in vowel_string:
    if  vowel not in user_input:
        all_vowels = False
        
if all_vowels == True:
    print("You have all the vowels")
    
vowel_counter = 0
for character in user_input:
    if character in vowel_string:
        vowel_counter = vowel_counter + 1

print("There is {} vowels in the word/sentence".format(vowel_counter))

if user_input[0] == "a" and user_input[-1] == "z":
    print("And it it's sort of alphabetical")
    

#%%% Exercise 5: Loopy fun

# TODO
# 1. Iterær over alle lige tal fra 1 til og med 100
# 2. Tæl antallet af lige tal
# 3. Tæl antallet af ulige tal

even_number_count = 0
disable_by_6_counter = 0
for number in range(2, 102, 2):
    even_number_count = even_number_count + 1
    if number % 6 == 0:
        disable_by_6_counter = disable_by_6_counter + 1
        
print("There are {} even numbers between 1 and 100".format(even_number_count))
print("{} numbers were divisiable by 6".format(disable_by_6_counter))

#%% Exercise 6: Countdown song

# TODO
# 1. Ask for user input n
# 2. Count down from n to 1, insert each iteration count into the lyric
# 3. Handle the edge case, when it's not plural anymore

n = int(input("How many Python books do you want to pass around: "))

for i in range(n-1):
    print(f"{n - 1} books on Python on the shelf. Take one down. Pass it around {n - (i + 1)} books left")
    
