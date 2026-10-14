
def check_password_strength(password):
    common_passwords = [
        "password",
        "password123",
        "123456",
        "12345678",
        "qwerty",
        "admin123",
        "welcome123"
    ]

    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)
    has_length = len(password) >= 12

    score = sum([
        has_uppercase,
        has_lowercase,
        has_number,
        has_special,
        has_length
    ])

    is_common = password.lower() in common_passwords
    has_low_variety = len(set(password)) <= 3

    if is_common or has_low_variety or score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return score, strength
