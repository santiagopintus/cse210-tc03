from pintus import pintus_presentation
from Chamorro import chamorro_presentation
from Quarshie import quarshie_greetings

def main(): 
    print('\nWelcome to our collaborative program.\n')
    #Everybody's functions
    while True:
        try:
            presentation_chosen = int(input('\nYou have to choose what number of presentation to see:\n'
                                    '1 - Pintus\n'
                                    '2 - Chamorro\n'
                                    '3 - Quarshie\n'
                                    '4 - All of them\n'
                                    '5 - Quit\n'
                                    'Choice: '
            ))
            if presentation_chosen > 5 or presentation_chosen < 1:
                print('\nSorry, you need to choose between 1 and 5')
            else:
                break
        except ValueError:
            print('\nSorry, you need to type a number between 1 and 5 without any symbols')
    if presentation_chosen == 1:
        print()
        pintus_presentation()
    elif presentation_chosen == 2:
        print()
        chamorro_presentation()
    elif presentation_chosen == 3:
        print()
        quarshie_greetings()
    elif presentation_chosen == 4:
        print()
        pintus_presentation()
        chamorro_presentation()
        quarshie_greetings()
    else:
        print()
        print('Ok! Goodbye!\n')

if __name__ == '__main__':
    main()