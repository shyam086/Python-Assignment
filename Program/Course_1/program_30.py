# Raising a ValueError for Invalid Age (Console)

def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")
    print(f"Age set to: {age}")