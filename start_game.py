from main import start, choose_starting_five, main_menu1
start()
choose_starting_five()
print("--------------------------------------------------------------")
user_choice = input('Press Enter to continue...')
if user_choice == '':
    main_menu1()