def convert_temperature():
    # ask the user for input temperature value
    temperature = float(input("Enter temperature value: "))

    # ask the user for input temperature unit
    input_unit = input("Enter temperature unit (C/F/K/R): ").upper()

    # define a dictionary of conversion ratios for each temperature unit
    ratios = {
        "C": {"F": 9/5, "K": 1, "R": 9/5},
        "F": {"C": 5/9, "K": 5/9 + 273.15, "R": 1},
        "K": {"C": 1, "F": 9/5 - 273.15, "R": 1.8},
        "R": {"C": 5/9 - 273.15, "F": 1, "K": 5/9}
    }

    # define a function to perform the conversion
    def convert(value, input_unit, output_unit):
        return value * ratios[input_unit][output_unit]

    # ask the user for output temperature unit
    output_unit = input("Enter output temperature unit (C/F/K/R): ").upper()

    # perform the conversion
    result = convert(temperature, input_unit, output_unit)

    # print the result
    print(f"{temperature} {input_unit} = {result} {output_unit}")

# call the function to run the program
convert_temperature()
