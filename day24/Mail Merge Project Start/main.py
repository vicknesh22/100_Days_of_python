# Read and ready the list of names

with open("./Input/Names/invited_names.txt", mode="r") as persons:
    invites = persons.readlines()

# Remove the extras from the name
corrected_invites = []
for i in invites:
    y = i.rstrip()
    corrected_invites.append(y)

# Going to replace the name in the letter
for j in corrected_invites:
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
        wed_letter = letter.read()
        data = wed_letter.replace("[name]", j)

    with open(f"./Output/ReadyToSend/letter_{j}.txt", mode="w") as letter:
        personal_letter = letter.write(data)
