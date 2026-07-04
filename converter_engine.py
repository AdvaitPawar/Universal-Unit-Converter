#Conversion Dictionary for backend math
ConversionFactors = {
    'Distance': {'Millimeter': 0.001, 'Centimeter': 0.01, 'Meter': 1.0, 'Kilometer': 1000.0, 'Feet': 0.3048, 'Inch': 0.0254, 'Yard': 0.9144, 'Mile': 1609.34},
    'Weight': {'Gram': 1.0, 'Milligram': 0.001, 'Kilogram': 1000.0, 'Ton': 1000000.0, 'Pound': 453.592},
    'Volume': {'Ounce': 1.0, 'Cup': 8.0, 'Pint': 16.0, 'Quart': 32.0, 'Gallon': 128.0},
    'Time': {'Seconds': 1.0, 'Minutes': 60.0, 'Hour': 3600.0, 'Day': 86400.0, 'Month': 2592000.0, 'Year': 31536000.0}
}

def calculate_standard(input_val, category, unit_from, unit_to, factors_dict):
    """Handles Distance, Weight, Volume, and Time math."""
    rate_from = factors_dict[category][unit_from]
    rate_to = factors_dict[category][unit_to]
    base_value = input_val * rate_from
    return base_value / rate_to

def calculate_temperature(input_val, unit_from, unit_to):
    """Handles Temperature logic."""
    if unit_from == 'Celsius':
        celsius = input_val
    elif unit_from == 'Fahrenheit':
        celsius = (input_val - 32) * 5 / 9
    elif unit_from == 'Kelvin':
        celsius = input_val - 273.15
        
    if unit_to == 'Celsius':
        return celsius
    elif unit_to == 'Fahrenheit':
        return (celsius * 9 / 5) + 32
    elif unit_to == 'Kelvin':
        return celsius + 273.15