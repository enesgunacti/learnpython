is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male or tall")

if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either nat mall or not tall or both")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are short male")
elif not(is_male) and is_tall:
    print("You are not a male bot are tall")
else:
    print("You are not male and not tall")