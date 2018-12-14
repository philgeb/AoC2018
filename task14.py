input = 540561

def part1():
    last_recipe = input

    recipes = [3, 7]
    elf1_index = 0
    elf2_index = 1

    while(len(recipes) < last_recipe + 11):
        curr_elf1_score = recipes[elf1_index]
        curr_elf2_score = recipes[elf2_index]
        recipes.extend(list(map(int, str(curr_elf1_score + curr_elf2_score))))
        elf1_index = (elf1_index + curr_elf1_score + 1) % len(recipes)
        elf2_index = (elf2_index + curr_elf2_score + 1) % len(recipes)

    print(''.join(str(r) for r in recipes[last_recipe : last_recipe + 10]))

def part2():
    sequence = input
    sequence_array = list(map(int, str(sequence)))
    last_digit = sequence_array[-1]

    recipes = [3, 7]
    elf1_index = 0
    elf2_index = 1

    while(True):
        curr_elf1_score = recipes[elf1_index]
        curr_elf2_score = recipes[elf2_index]
        recipes.extend(list(map(int, str(curr_elf1_score + curr_elf2_score))))

        if recipes[-1] == last_digit:
            len_diff = len(recipes) - len(sequence_array)
            if recipes[len_diff:] == sequence_array:
                print(len_diff)
                break

        if recipes[-2] == last_digit:
            len_diff = len(recipes) - len(sequence_array)
            if recipes[len_diff - 1 : -1] == sequence_array:
                print(len_diff - 1)
                break

        elf1_index = (elf1_index + curr_elf1_score + 1) % len(recipes)
        elf2_index = (elf2_index + curr_elf2_score + 1) % len(recipes)

part2()