import time
from get_column import get_column


def whitelist_func(interaction, username, sheet):
    number_of_users = int(sheet.acell("L1").value)

    column_c = get_column("C", sheet, "digit")

    column_d = get_column("D", sheet, "digit")

    found_user = False
    for i in range(number_of_users):
        temp_id = str(column_c[i]) + str(column_d[i])
        print(f"- temp_id: {temp_id}\nauthorID: {interaction.user.id}")
        if str(temp_id) == str(interaction.user.id):
            found_user = True
            print("--------------- FOUND USER ---------------")

    print(found_user)
    if not found_user:

        # adds a new row to the sheet
        sheet.add_rows(1)

        number_of_users = number_of_users + 1

        # adds the users discord username to the sheet
        sheet.update_acell(f"A{number_of_users + 1}", str(interaction.user))

        # adds the users in-game username to the sheet
        sheet.update_acell(f"B{number_of_users + 1}", username)

        # adds the users ID and ID length to the sheet
        user_id = [char for char in str(interaction.user.id)]
        for i in range(len(user_id)):
            user_id[i - 1] = str(user_id[i - 1])

        id1 = ""
        for k in range(9):
            id1 = id1 + user_id[k]

        id2 = ""
        try:
            for k in range(10):
                id2 = id2 + user_id[k + 9]
        except IndexError:
            print("ID# only has 18 digits.")

        sheet.update_acell(f"C{number_of_users + 1}", id1)
        sheet.update_acell(f"D{number_of_users + 1}", id2)
        sheet.update_acell(f"E{number_of_users + 1}", len(user_id))

        # updates the user's rocket ID
        sheet.update_acell(f"F{number_of_users + 1}", "null")

        # writes the user down as not whitelisted
        sheet.update_acell(f"G{number_of_users + 1}", "no")

        # writes the user down as never having been whitelisted
        sheet.update_acell(f"H{number_of_users + 1}", "0")

        # fills in the date the user joined
        sheet.update_acell(f"I{number_of_users + 1}", time.ctime())

        # fills in the row to determine if the user has been notified that they have been whitelisted
        sheet.update_acell(f"J{number_of_users + 1}", "no")

        # fills in the row saying that the user has not received the "Player" role
        sheet.update_acell(f"K{number_of_users + 1}", "no")

        return f"Welcome to the server, {str(interaction.user)}!\nA mod will whitelist you within a few hours or days."

    if found_user:
        return "Your username has already been recorded. It does not need to be recorded again."
