#String atau data non numerik
data = 'Ini adalah data string'
print(data)
print("\n")
# 1. Cara membuat string 
''' 
    1. Membuat string dengan menggunakan single quote '....'
    2. Membuat String dengan menggunakan double quote "...."
'''
data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

#single quote dan double quote dapat digunakan bersamaan
print('"Halo, siapa namamu?"')
print("'halo siapa namamu?'")
#Semua karakter yang berada di antara ".." atau '..' akan dianggap sebagai string

# 2. Membuat string dengan menggunakan "\"
# membuat tanda ' dan " menjadi string
print('Hari ini hari jum\'at')

#Backlash
print("Einstein\\ Wingentein\\")

#Tab
print("Einstein\tWingenstein")

#Backspace
print("Einstein \b Wingenstein")

#Newline
print("First Line#1\nsecond Line#2") # LF Line Feed -> Unix, MacOs, Linus
print("First Line#1\rsecond Line#2") # LF Line Feed -> Commodore, Acorn
print("First Line#1\r\nsecond Line#2") # LF Line Feed -> Windows

# 3. Membuat String Literal atau Raw
# menggunakan raw string
print(r'C:\newFolder') # apapun yang diawal "r" (raw) akan dianggap string
# multiline literal string
print("""
Djanggo Unchained\n
directed by Quentin Tarantino
Starring Leonardo DiCaprio
""")
#multiline literal raw string
print(r"""
Djanggo Unchained\n
directed by Quentin Tarantino
Starring Leonardo DiCaprio
""")
