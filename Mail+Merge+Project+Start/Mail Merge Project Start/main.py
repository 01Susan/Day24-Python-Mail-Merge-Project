# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# TODO 1. Reading  all the name from invited_names.txt
names_invited = []


def reading_invited_names():
    with open(r".\Input\Names\invited_names.txt", mode="r") as invited_names:
        for names in invited_names:
            names_invited.append(names)


# TODO 2. Replacing [name] by user_name
def replacing_name():
    with open(r".\Input\Letters\starting_letter.txt", mode='r') as reading_letter:
        reading_mail = reading_letter.read()
        return reading_mail


# TODO 3. Making each file for each emails
def ready_to_send():
    reading_invited_names()
    for name in names_invited:
        replace_space = name.replace(" ", "_")
        invited_name = replace_space.strip("\n")
        # Path for creating each user files that consist email
        email_to = r".\Output\ReadyToSend\letter_to_" + invited_name + ".txt"
        with open(email_to, mode="w") as write_emails:
            mail_name = replacing_name().replace("[name]", invited_name)
            write_emails.write(mail_name)


ready_to_send()
