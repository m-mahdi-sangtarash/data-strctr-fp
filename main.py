import numpy as np
import projec_functions as pf

index = None
num_array = np.array([0 for _ in range(50)])
loop_status = 'open'

while loop_status == 'open':
    print('''\t===========================================
    |  enter numbers :                     e  |
    |  remove a number:                    r  |
    |  insert a number in special index :  i  |
    |  sort number:                        s  |
    |  show numbers list:                  v  |
    |  show biggest number in list:        b  |
    |  exit:                               q  |
    ===========================================''')

    work = input('\n\tenter your task: ')

    if work == 'e':
        if index == None or index < 49:
            num_array, index = pf.numbers_receiver_func(num_array, index)
        else:
            print('Your list is currently full. To add a number, you must remove a number first.\nOur suggestion: '
                  'enter <r>')

    elif work == 'r':
        if index == None:
            print(
                'Number list is empty! You must first add one or more numbers to the list.\n\nSuggestion: Enter '
                'the letter <e>.')
        else:
            num_array, index = pf.remove_num_func(num_array, index)
            continue

    elif work == 'i':
        try:
            if index < 49:
                num_array, index = pf.insert_num(num_array, index)
                continue
            elif index == 49:
                print('Your list is currently full. To add a number, you must remove a number first.\nOur suggestion: '
                      'enter <r>')
                continue
        except TypeError:
            print('Your list is empty now! suggestion: enter <e>')
    elif work == 's':

        if index == None:
            print('Number list is empty! You must first add one or more numbers to the list.\n\nSuggestion: Enter '
                  'the letter <e>.')
            continue
        else:
            num_array, index = pf.sort_lst_func(num_array, index)
            continue

    elif work == 'v':
        if index == None:
            print('Number list is empty! You must first add one or more numbers to the list.\n\nSuggestion: Enter '
                  'the letter <e>.')
        else:
            print(num_array[0:index + 1])
            continue

    elif work == 'q':
        print('Goodbye...!')
        break
    elif work == 'b':
        if index == None:
            print('Number list is empty! You must first add one or more numbers to the list.\n\nSuggestion: Enter '
                  'the letter <e>.')
        else:
            pf.find_biggest(num_array, index)
            continue
    else:
        print('invalid value ! Pay attention to the list of operations.')
        continue
