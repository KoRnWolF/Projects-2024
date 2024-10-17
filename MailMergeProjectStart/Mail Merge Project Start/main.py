with open("./Input/Letters/starting_letter.txt") as letter:
    letter_body = letter.read()
with open("./Input/Names/invited_names.txt") as names:
    for name in names:
        stripped_name = name.rstrip
        new_letter = letter_body.replace("[name]",f"{name}".rstrip())
        with open(f"./Output/ReadyToSend/letter_for_{name}".rstrip(),"w") as new_let:
            new_let.write(new_letter)

