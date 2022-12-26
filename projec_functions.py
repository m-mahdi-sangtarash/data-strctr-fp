def sort_lst_func(num_array, index):
    for turn in range(0, index):
        for num_checker in range(0, index):
            if num_array[num_checker] > num_array[num_checker + 1]:
                num_array[num_checker + 1] += num_array[num_checker]
                num_array[num_checker] = num_array[num_checker + 1] - num_array[num_checker]
                num_array[num_checker + 1] -= num_array[num_checker]
            else:
                continue
    print('The list of numbers is sorted in ascending order.')
    return num_array, index


def numbers_receiver_func(num_array, index):

    while 0 < 1:
        if index == None:
            try:
                num_array[0] = int(input('enter your number (If you want to end this operation, you can enter a '
                                         'letter.): '))
                index = 0
            except ValueError:
                return num_array, index

        else:
            for i in range(index, 50):
                try:
                    num_array[index + 1] = int(input('enter your number (If you want to end this operation, you can '
                                                     'enter a letter.): '))
                    index += 1
                except ValueError:
                    break
            return num_array, index


def remove_num_func(num_array, index):
    while 0 < 1:
        try:
            remove_ind = int(input(f'please select number place (between 0 - {index}:'))
            break
        except ValueError:
            print('\ninvalid value! please try again.')
            continue
    turn = remove_ind
    while turn < index:
        num_array[turn] = num_array[turn + 1]
        turn += 1

    index -= 1
    print('\n number removed!')
    return num_array, index


def insert_num(num_array, index):
    while 0 < 1:
        try:
            add_index = int(input(f'Choose the place to add the number you want.(between 0 - {index + 1}: )'))
            if add_index > (index + 1) or add_index < 0:
                print('invalid index!. try again.')
                continue
            else:
                break
        except ValueError:
            print('invalid value! try again!')
            continue

    while 0 < 1:
        try:
            add_number = int(input('enter your number: '))
            break
        except ValueError:
            print('\ninvalid Value! Try again.\n')
            continue

    if add_index == index + 1:
        index += 1
        num_array[index] = add_number

    else:
        replacer = index
        index += 1
        while replacer >= add_index:
            num_array[replacer + 1] = num_array[replacer]
            replacer -= 1
        num_array[add_index] = add_number

    print(f'number {add_number} add to {add_index}th section.')
    return num_array, index


def find_biggest(num_array, index):
    big_index = 0
    big_number = num_array[big_index]
    while big_index < index:
        if big_number < num_array[big_index + 1]:
            big_number = num_array[big_index + 1]
            big_index += 1
        else:
            big_index += 1
            continue

    print(f'biggest number in list is: {big_number}')
