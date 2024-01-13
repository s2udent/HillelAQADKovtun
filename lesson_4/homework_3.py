notes_list = []
action = ''

while action != 'exit':
    action = input('Enter the key word: ').lower()
    if action == 'add':
        note = input('Введіть нотатку: ')
        notes_list.append(note)
        print('Note was saved')
    elif action == 'earliest':
        for note in sorted(notes_list, key=notes_list.index):
            print(note)
    elif action == 'latest':
        for note in sorted(notes_list, key=notes_list.index, reverse=True):
            print(note)
    elif action == 'longest':
        for note in sorted(notes_list, key=len, reverse=True):
            print(note)
    elif action == 'shortest':
        for note in sorted(notes_list, key=len):
            print(note)
    elif action == 'exit':
        print('Exiting...')
    else:
        print('incorrect command')


