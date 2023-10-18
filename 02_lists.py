### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))
print(len(my_other_list))

languages = ['JavaScript', 'Python', 'Ruby', 'Dart', 'Go', 'Java', 'C++']

print('Languages:', languages)
print('number of languages:', len(languages))
print('The first language:', languages[0])
print('The first language:', languages[-5])
print('The last language:', languages[-1])

languages[5] = "Perl"
print(languages)


## Unpacking list items

first_language, second_language, third_language, *rest, last_language = languages

print(first_language)
print(second_language)
print(third_language)
print(rest)
print(last_language)


## Checking items in the list

html_exist = 'HTML' in languages
print(html_exist)
py_exist = 'Python' in languages
print(py_exist)


## Adding items to the list

languages.append('PHP')
print(languages)


## Inserting items to the list
languages.insert(3, 'SQL')
print(languages)


## Removing items from the list
languages.remove('Ruby')
print(languages)

languages.pop()
print(languages)

languages.pop(2)
print(languages)

del languages[2]
print(languages)

# del languages -> Delete the complete list


## Copying lists

new_languages_list = languages.copy()
print(new_languages_list)


## Joining lists
other_languages = ['HTML', 'CSS']
all_languages = new_languages_list + other_languages
print(all_languages)

other_languages_list = ['Logo', 'Pascal']
new_languages_list.extend(other_languages_list)
print(new_languages_list)


## Sorting list items
new_languages_list.sort()
print(new_languages_list)

new_languages_list.sort(reverse=True)
print(new_languages_list)

print(sorted(languages)) # Sorted sorts the items without modifying the original list
print(languages)