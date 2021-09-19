import time

program_running = True
clean = True
pantsup = True
hasshat = False
shitdownlegs = False
shituplegs = False


def countdown(timer):
    while timer:
        time.sleep(1)
        timer -= 1

welcome_message = str('''
Welcome to "Do a Shit."
**********************
The aim of the game is to do a shit.
For commands, type "help"
Enjoy.
''')
timer = 5
help_command = str("help")
hasshat_mesage = str("You don't have any shit left.")
pantsaredown = str("Your pants are already down.")
shitallover_message = str("You've got shit all up and down your legs. Your pants are filled with shit. You trip over "
                          "trying to sustain your grip on the shit-covered hem. Your head hits a rock, and you are "
                          "dead, and all covered in shit. Great job, loser.")
pantsareup = str("Your pants are already up.")
pants_down_command = str("pull pants down")
pants_down_msg_clean = str("You pull your pants down, and stand tall, bare arse in the wind...")
pants_down_msg_dirty = str("You pull your shit-covered pants down, and feel the warm, wet excrement rub against your "
                           "legs.")
pants_up_command = str("pull pants up")
pants_up_message_clean = str("You pull your pants back up, and fasten your belt.")
pants_up_msg_dirty = str("You slowly drag your now heavy with shit pants up, and feel that familiar sliminess once "
                         "again.")
shit_command = str("shit")
shit_clean_message = str("You tense your abs, and squeeze. A single, solid piece of shit fires out of your arsehole, "
                         "and lands in the grass. A small, squeak of a fart follows, and you are hyper aware of the "
                         "dry cleanliness around your sphincter.")
shit_dirty_message = str("You tense your abs, and squeeze. A mixture of wet farts, and sputtering diarrhea follows. "
                         "Shit fills your undies quickly, and begins oozing out the sides. You feel ill.")
quit_command = str("quit")
quit_clean_message = str("After having expelled a clean, and powerful shit in a beautiful meadow, you deserve a rest. "
                         "Farewell, King.")
quit_dirty_message = str("Might as well end it all huh? Shat your pants in a field. Bye.")
incorrect_command_message = str("I don't understand... type 'help' for command options.")
shitting_imminent_message = str("Huh. Quitting without shitting. Poetic.")
help_msg = str(f'''{pants_down_command} = pull your pants down
{pants_up_command} = pull your pants up
{shit_command} = do a shit
{quit_command} = quit the program''')
print(welcome_message)
while program_running:
    command = str(input("> "))
    if command.lower() == help_command:
        print(help_msg)
    elif command.lower() == pants_down_command:
        if not (shituplegs and shitdownlegs):
            if pantsup:
                pantsup = False
                if clean:
                    print(pants_down_msg_clean)
                else:
                    shitdownlegs = True
                    print(pants_down_msg_dirty)
            else:
                print(pantsaredown)
        else:
            print(shitallover_message)
            countdown(timer)
            break
    elif command.lower() == pants_up_command:
        if not (shituplegs and shitdownlegs):
            if not pantsup:
                pantsup = True
                if clean:
                    print(pants_up_message_clean)
                else:
                    shituplegs = True
                    print(pants_up_msg_dirty)
            else:
                print(pantsareup)
        else:
            print(shitallover_message)
            countdown(timer)
            break
    elif command.lower() == shit_command:
        if not hasshat:
            hasshat = True
            if pantsup:
                clean = False
                print(shit_dirty_message)
            else:
                print(shit_clean_message)
        else:
            print(hasshat_mesage)
    elif command.lower() == quit_command:
        if not hasshat:
            print(shitting_imminent_message)
            countdown(timer)
            break
        else:
            if clean:
                print(quit_clean_message)
                countdown(timer)
                break
            else:
                print(quit_dirty_message)
                countdown(timer)
                break
    else:
        print(incorrect_command_message)