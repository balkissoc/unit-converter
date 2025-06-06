# unit_converter.py

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


if __name__ == "__main__":
    print("Welcome to the Unit Converter!")
    value = float(input("Enter value: "))
    from_unit = input("Convert from (e.g. metre): ").lower()
    to_unit = input("Convert to (e.g. foot): ").lower()
    try:
        result = convert_length(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result:.2f} {to_unit}")
    except ValueError as e:
        print("Error:", e)
