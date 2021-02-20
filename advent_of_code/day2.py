
filename = "day2inputs"
with open(filename, "r") as file:
    contents = file.read()

passwords = contents.splitlines()

# 1-9 x: xwjgxtmrzxzmkx
def check_password(policy_and_password):
    policy, password = policy_and_password.split(": ")
    numbers, letter = policy.split(" ")
    minimum, maximum = map(int, numbers.split("-"))
    number_of = password.count(letter)
    if minimum <= number_of <= maximum:
        return True
    else:
        return False


# 4-5 v: vvfvvvn
def check_password_part2(policy_and_password):
    policy, password = policy_and_password.split(": ")
    numbers, letter = policy.split(" ")
    index_a, index_b = map(int, numbers.split("-"))
    letter_a = password[index_a - 1]
    letter_b = password[index_b - 1]
    if (letter_a == letter or letter_b == letter) and (not letter_a == letter_b):
        return True
    else:
        return False


valid_checks = []
for password in passwords:
    valid_checks.append(check_password_part2(password))

number_valid = sum(valid_checks)
print("Number of valid passwords:", number_valid)