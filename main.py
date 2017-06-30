
from spy_details import spy, user, Chat_message, friends_detail# import spy,user,chat_meaasge,friends_details from spy_details
from steganography.steganography import Steganography #import steganography for send secrect image message and read secrect message
from datetime import datetime#import  datetime for display a date and time

status_message = ['hellow every one', 'how do you do ', 'always happy']#predefine status message


print ("welcome to spy chat")

menu_choices = ("Do you want to continue as " + spy.salutation + " " + spy.name + " "+spy.age+" "+spy.rating+" (Y/N)? ")
menu_choice = raw_input(menu_choices )


def add_status():# define function to add status

    updated_status_message = None

    if spy.current_status_message != None:

        print ('Your current status message is %s \n' % (spy.current_status_message))
    else:
        print ('You don\'t have any status message currently \n')

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")


        if len(new_status_message) > 0:
            status_message.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in status_message:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))


        if len(status_message) >= message_selection:
            updated_status_message = status_message[message_selection - 1]

    else:
        print ('The option you chose is not valid! Press either y or n.')

    if updated_status_message:
        print ('Your updated status message is: %s' % (updated_status_message))
    else:
        print ('You current don\'t have a status update')

    return updated_status_message


def add_friend():#define function for add friend

    new_friend = user('','',0,0.0)#call user from spy_details

    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends_detail.append(new_friend)#append new_friend to friend_details
        print ('Friend Added!')
    else:
        print ('Sorry! Invalid entry. We can\'t add spy with the details you provided')

    return len(friends_detail)# return the value to friends_detalis


def select_a_friend():# define select_a_friend function
    item_number = 0

    for friend in friends_detail:
        print ('%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating))
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def send_message():# define function for send message

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)#steganography for encode the message

    new_chat = Chat_message(text,True)#call chat_message

    friends_detail[friend_choice].chats.append(new_chat)

    print ("Your secret message image is ready!")


def read_message():# define function for read message

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)# steanography use for decode the message

    new_chat = Chat_message(secret_text,False)# call chat_message

    friends_detail[sender].chats.append(new_chat)

    print ("Your secret message has been saved!")


def read_chat_history():# define function for read chat history

    read_for = select_a_friend()


    for chat in friends_detail[read_for].chats:
        if chat.sent_by_me:
            print ('[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message))
        else:
            print ('[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends_detail[read_for].name, chat.message))


def start_chat(spy):# define start chat function

    spy.name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 50:


        print ("Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard")

        show_menu = True

        while show_menu:
            menu_choices =("What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n")
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()# call add_status function
                elif menu_choice == 2:
                    number_of_friends = add_friend()# call add function
                    print ('You have %d friends' % (number_of_friends))
                elif menu_choice == 3:
                    send_message()# call send_message
                elif menu_choice == 4:
                    read_message()# call read_message function
                elif menu_choice == 5:
                    read_chat_history()# call read _chat_history function
                else:
                    show_menu = False
    else:
        print ('Sorry you are not of the correct age to be a spy')

if menu_choice == "Y":
    start_chat(spy)# call start chat
else:

    spy = user('','',0,0.0)


    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)

        if spy.rating>4.5:
            print (" great one keep it on")
        elif spy.rating>3.4 and spy.rating<=4.5:
            print (" you are the good one")
        elif spy.rating>=2.4 and spy.rating<3.5:
            print ("you can alwayes do better")
        else:
            print ("you can use sameone in office")

        start_chat(spy)# call start chat function
    else:
        print ('Please add a valid spy name')


#spy chat application complete




