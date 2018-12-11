import random
from itertools import permutations, chain

base_vowels = ['a', 'e', 'i', 'o', 'u']
base_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

vowel_conjunctions = []
consonant_conjunctions = []

# Generate the random sequence of vowels
for num in range(1, 3):
    temp_vowel_conjunctions = list(permutations(base_vowels, num))
    temp_vowel_conjunctions = [''.join(vowels) for vowels in temp_vowel_conjunctions]
    vowel_conjunctions.append(temp_vowel_conjunctions)

vowel_conjunctions = list(chain.from_iterable(vowel_conjunctions))

# Generate the random sequence of consonants
for num in range(1, 3):
    temp_consonant_conjunctions = list(permutations(base_consonants, num))
    temp_consonant_conjunctions = [''.join(consonants) for consonants in temp_consonant_conjunctions]
    consonant_conjunctions.append(temp_consonant_conjunctions)

consonant_conjunctions = list(chain.from_iterable(consonant_conjunctions))

vowel_rand_choice = random.choice(vowel_conjunctions)
cons_rand_choice = random.choice(consonant_conjunctions)

random_name = '{}{}{}{}{}'.format(cons_rand_choice, vowel_rand_choice,cons_rand_choice, vowel_rand_choice,cons_rand_choice)

print(random_name)