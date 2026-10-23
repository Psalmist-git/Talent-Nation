def solution(kilograms):
    kilograms = float(kilograms)
    grams = kilograms * 1000
    pounds = round(kilograms * 2.20462, 2)

    return f"Kilograms: {kilograms}\nGrams: {grams}\nPounds: {pounds}"