def solution(value):
    try:
        number = float(value)
        return round(number * 2, 2)
    except ValueError:
        return "Invalid number"
        