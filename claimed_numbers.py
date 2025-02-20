from get_column import get_column


def claimed_numbers_func(sheet):
    number_of_users = int(sheet.acell("L1").value)
    numbers = []

    column_e = get_column("F", sheet, "digit")
    for i in range(number_of_users):
        temp = str(column_e[i])
        if temp != "":
            numbers.append(temp)

    return f"The list of already claimed numbers is {sorted(numbers)}."
