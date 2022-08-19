def make_dict(file_name_arg):
    with open(file_name_arg, "r", encoding="utf-8") as my_f:
        lines = [line.split() for line in my_f]
    total_by_subject = {}
    for line in lines:
        total_hours = 0
        for word in line:
            stop = word.find('(')
            if stop != -1:
                total_hours += int(word[:stop])
            total_by_subject[line[0][:-1]] = total_hours
    return total_by_subject


file_name = "files/text_6.txt"
print(make_dict(file_name))
print('-' * 100)


# -------------------------- Второй вариант --------------------------

def make_dict1(file_name_arg):
    with open(file_name_arg, "r", encoding="utf-8") as my_f:
        lines = [line.split() for line in my_f]
        subject_to_hours = map(lambda l: (l[0][:-1], sum_hours(l)), lines)
        return {i[0]: i[1] for i in subject_to_hours}


def sum_hours(hour_details):
    return sum(map(lambda h: int(h[:h.find('(')]), [hours for hours in hour_details[1:] if hours != '-']))


file_name = "files/text_6.txt"
print(make_dict1(file_name))
