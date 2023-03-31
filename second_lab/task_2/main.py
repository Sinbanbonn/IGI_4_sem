import re
from data_storage import DataStorage

storage = DataStorage()
username = input('Enter your username: ')
status = 'start'
answer = ""

while True:

    if status == 'start':

        if not storage.user_exists(username):
            storage.add_user(username)

        answer = input('You are on the main menu.\n')
        status = 'main_menu'

    elif status == 'main_menu':

        if re.match('add ', answer):

            data = answer.split()
            if len(data) > 1:

                if not storage.find_element(username, ' '.join(data[1:])):
                    storage.add_element(username, ' '.join(data[1:]))
                    answer = input('Element was successfully added\n')
                else:
                    answer = input(f'Element {" ".join(data[1:])} is already in your container.\n')

            else:
                answer = input('Input add <value> to add element: ')

        elif re.match('find ', answer):

            data = answer.split()
            if len(data) > 1:

                element = "".join(data[1:])
                if storage.find_element(username, element):
                    answer = input(f'Element "{element}" is in your container.\n')
                else:
                    answer = input('There is no such element in your container.\n')

            else:
                answer = input('Input find <value> to find element: ')

        elif re.match('remove ', answer):

            data = answer.split()
            if len(data) > 1:

                element = "".join(data[1:])
                if storage.find_element(username, element):
                    storage.remove_element(username, element)
                    answer = input(f'Element "{element}" was removed.\n')
                else:
                    answer = input('There is no such element in your container.\n')

            else:
                answer = input('Input remove <value> to remove element: ')

        elif re.match('grep ', answer):

            data = answer.split()
            if len(data) > 1:

                element = "".join(data[1:])
                result = storage.grep_element(username, element)
                if result:
                    i = 1
                    print('Elements satisfying the regular expression:')
                    for element in result:
                        print(f'{i}) {element}')
                    answer = input('You are on the main menu.\n')
                else:
                    answer = input('There is no such element in your container.\n')

            else:
                answer = input('Input grep <regex> to find element by regular expression: ')

        elif answer == 'switch':
            if not storage.is_saved(username):
                answer = input('Do you want to save changes?(Y/n)\n')
                status = 'switch_user'
            else:
                username = input('Enter username: ')
                status = 'start'

        elif answer == 'save':
            if not storage.is_saved(username):
                storage.save_data(username)
                answer = input('Changes was saved.\n')
            else:
                answer = input('Nothing to save. Everything is up-to-date.\n')

        elif answer == 'load':
            storage.load_data(username)
            answer = input('Data was loaded.\n')

        elif answer == 'list':

            result = storage.get_elements_list(username)
            if result:
                print('Your storage:')
                i = 1
                for element in result:
                    print(f'{i}) {element}')
                    i += 1
                answer = input('')
            else:
                answer = input('There are no elements in your container.\n')


        else:
            answer = input('Wrong input!\n')

    elif status == 'switch_user':

        if answer == 'Y':
            storage.save_data(username)
            username = input('Changes was saved.\nEnter username: ')
            status = 'start'

        elif answer == 'n':
            username = input('Changes wasn`t saved.\nEnter username: ')
            status = 'start'

        else:
            answer = input('Do you want to save changes?(Y/n)\n')
