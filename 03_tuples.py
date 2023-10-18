### Tuples ###

empty_tuple = ()
empty_tuple_two = tuple()

languages = ('JavaScript', 'Python', 'Go', 'Perl', 'C++')
print(len(languages))

first_language = languages[0]
print(first_language)


## Slicing

middle_two_langiages = languages[1:4]
print(middle_two_langiages)


## Changing Tuples to Lists

languages = list(languages)
print(languages)

languages = tuple(languages)
print(languages)


## Joining Tuples

new_languages = ('Dart', 'Ruby', 'SQL')
all_languages = languages + new_languages

print(new_languages)
print(all_languages)


## Deleting tupples

del all_languages # Only the entire tuple can be deleted since it is not possible to delete an item within the tuple because it is immutable.