# Data
movie = "Reservoir Dogs"
release_date= "October 8, 1992 (USA)"
director= "Quentin Tarantino"
budget= "1.2 million USD"
screenplay= "Quentin Tarantino, Roger Avary"
print("\n")

# String Standar
data_string = f"Movie : {movie}, Release Date : {release_date}, Diector : {director}, Budget : {budget}, Screenplay : {screenplay}"
print(" Data String Standar ".center(60,"-"))
print(data_string)
print("".center(60,"-"))
print("\n")

# String Multiline
data_string = f"Movie : {movie}, \nRelease Date : {release_date}, \nDiector : {director}, \nBudget : {budget}, \nScreenplay : {screenplay}"
print(" Data String Multiline ".center(60,"-"))
print(data_string)
print("".center(60,"-"))
print("\n")

# String Multiline triplet single quote
data_string = f'''
Movie        : {movie}
Release Date : {release_date}
Director     : {director}
Budget       : {budget}
Screenplay   : {screenplay}
'''
print(" Data String Multiline triplet single quote ".center(60,"-"))
print(data_string)
print("".center(60,"-"))
print("\n")