""" functions for length conversions """

CONVERSION_FACTOR = 0.621371  #km to miles

def km_to_miles (kilometers: float) -> float:
    return kilometers * CONVERSION_FACTOR

def miles_to_kilometer (miles: float) -> float:
    return miles / CONVERSION_FACTOR

