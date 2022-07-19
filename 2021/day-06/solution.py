def parse_file(input_file):
    with open(input_file, "r", encoding="utf-8") as fp:
        file_lines = [line.strip() for line in fp.readlines()]
    return list(map(int, file_lines[0].split(",")))


def pass_day(fish_list):
    new_fish = []
    for index, timer in enumerate(fish_list):
        if timer == 0:
            fish_list[index] = 6
            new_fish.append(8)
        else:
            fish_list[index] -= 1
    fish_list.extend(new_fish)
    return


def solution_1(input_file):
    fish = parse_file(input_file)
    days = 80
    for i in range(days):
        pass_day(fish)

    return len(fish)


def solution_2(input_file):
    return
