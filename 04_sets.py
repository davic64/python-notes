### Sets ###

new_set = set()

languages = {'JavaScript', 'Python', 'Dart', 'Perl', 'C++'}
print(len(languages))

print('Is Python on set?:', 'Python' in languages)


## Adding items to a Set

languages.add('Ruby')
print(languages)

languages.update(['HTML', 'SQL', 'CSS'])
print(languages)


## Removing Items from a Set

languages.remove('CSS')
print(languages)

removed_language = languages.pop()
print(languages) # Removes a random item from the set
print(removed_language)


## Joining Sets

new_languages = {'Go', 'Logo', 'Lisp', 'Pascal'}

all_languages = languages.union(new_languages)

print(all_languages)


## Deleting a Set

del languages


## Finding Intersection Items

a = {0, 1, 2, 3, 4, 5}
b = {0, 3, 9, 4, 8, 5, 6}

print(a.intersection(b)) # Check the numbers that match in both sets.


## Checking Subset and Super Set

c = {1, 2, 3, 4, 5, 6}
d = {3, 4, 5}

print(d.issubset(c)) # Returns True, because "d" is a subset of "c".
print(c.issubset(d))

print(c.issuperset(d)) # Returns True, because "c" is a superset of "d"
print(d.issuperset(b))


## Checking the Difference Between Two Sets

python = {'p', 'y', 't', 'h', 'o', 'n'}
rhythm = {'r', 'h', 'y', 't', 'h', 'm'}

print(python.difference(rhythm)) # Checks which items are different and returns them out of order
print(rhythm.difference(python))

