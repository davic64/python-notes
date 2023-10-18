### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string )

my_new_line_string = "Este es un string\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un String \n escapado"
print(my_scape_string)


## Formatting

name, lastname, age = "David", "Victoria", 27

print("Mi nombre es {} {} y mi edad es {}".format(name, lastname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, lastname, age))
print(f"Mi nombre es {name} {lastname} y mi edad es {age}")

## Character unpacking

lang = "python" # First, the variable
a, b, c, d, e, f = lang # Then it is unpacked
print(a)
print(e)


## División

language_slice = lang[1:3]
print(language_slice)

language_slice = lang[1:]
print(language_slice)

language_slice = lang[0:6:2]
print(language_slice)

### 0: This is the starting index of the slice. In Python, indexes start from 0, so 1 refers to the second element of the sequence.

### 6: This is the slice completion index. The slice will include elements up to just before this index. In this case, 2 refers to the third element of the sequence.

### 2: This is the "step" or "step". It indicates how many elements an element is taken in the slice. In this case, one element is taken and the next element is omitted (a gap of 2).


## Reverse
reverse_lang = lang[::-1]
print(reverse_lang)


## Methods

print(lang.capitalize())
print(lang.upper())
print(lang.count("t"))
print(lang.isnumeric())
print("1".isnumeric())
print(lang.startswith("py"))
print(lang.endswith("cript"))
print(lang.upper().isupper())