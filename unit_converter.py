def convert_length(value, from_unit, to_unit):
    units = {
        "metre": 1.0,
        "foot": 0.3048,
        "inch": 0.0254,
        "kilometre": 1000,
        "mile": 1609.34,
    }
    if from_unit not in units or to_unit not in units:
        raise ValueError("Unsupported unit")
    return value * units[from_unit] / units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    """Convert temperatures between Celsius and Fahrenheit."""
    temp_units = ("celsius", "fahrenheit")
    if from_unit not in temp_units or to_unit not in temp_units:
        raise ValueError("Unsupported temperature unit")

    if from_unit == to_unit:
        return value

    if from_unit == "celsius" and to_unit == "fahrenheit":
        return value * 9 / 5 + 32
    if from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5 / 9

    raise ValueError("Invalid temperature conversion")

if __name__ == "__main__":
    print("Welcome to the Unit Converter!")
    value = float(input("Enter value: "))
    from_unit = input("Convert from (e.g. metre or celsius): ").lower()
    to_unit = input("Convert to (e.g. foot or fahrenheit): ").lower()
    try:
        if from_unit in ["celsius", "fahrenheit"] or to_unit in ["celsius", "fahrenheit"]:
            result = convert_temperature(value, from_unit, to_unit)
        else:
            result = convert_length(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result:.2f} {to_unit}")
    except ValueError as e:
        print("Error:", e)
