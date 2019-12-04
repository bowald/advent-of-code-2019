password_min = 109165
password_max = 576723

# Two adjacent digits are the same

def descending(candidate):
    return all([candidate[i] <= candidate[i+1] for i in range(5)])

def adjecent(candidate):
    return any([candidate[i] == candidate[i+1] for i in range(5)])

def a_double_nr(candidate):
    padded = 'x' + candidate + 'x'
    return any([padded[i-1] != padded[i] and padded[i] == padded[i+1] and padded[i+1] != padded[i+2] for i in range(1,6)])

part1_passwords = 0
part2_passwords = 0

for i in range(password_min, password_max):
    candidate = str(i)
    if not descending(candidate):
        continue

    if adjecent(candidate):
        part1_passwords += 1

    if a_double_nr(candidate):
        part2_passwords += 1

print(f'part1: {part1_passwords}')
print(f'part2: {part2_passwords}')