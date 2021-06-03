from file_extr import users
from send_email import sendEmail

# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filename = input('Path to attachment: ')
    names = input('Path to User Info: ')
    subject = input('Subject: ')
    message = input('Body: ')
    user = users()
    data = user.getData(names)
    sender = sendEmail(subject, message, filename)
    sender.prepare_email(data)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
