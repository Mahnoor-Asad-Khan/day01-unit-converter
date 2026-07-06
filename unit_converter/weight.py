""" functions for weight conversion """

CONVERSION_FACTOR = 2.20462  #kg to pounds

def kg_to_pounds(kg: float) -> float:
    return kg * CONVERSION_FACTOR

def pounds_to_kg(pounds: float) -> float:
    return pounds / CONVERSION_FACTOR