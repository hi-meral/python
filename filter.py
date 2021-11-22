# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels


def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False


filteredVowels = filter(filterVowels, alphabets)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)


def newfilter(numbers):
    fixnumbers = [3, 6, 9]

    if (numbers in fixnumbers):
        return True
    else:
        return False


marks = {'meral': 9, 'ankit': 8}


hello = filter(newfilter, marks.values())


for h in hello:
    print(h)
