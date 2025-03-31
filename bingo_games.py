#create a bingo game yourself. Without looking more than 5 times at previous example!
import time
import random




def roll_numbers():
    bingo_numbers = []
    exit = ()
    print("\n!BINGO OF THE LIFETIME!\n")
    while exit != 0:
        roll = int(input("Please enter the amount of faces you want on your bingo dice roll! Press '0' to quit at anytime.")) 
        
        if roll == 0:
            print("Thank you for your time!")
            break
        else:
            players = int(input("\nPlease tell us how many players will play? 1 or 2?"))
            if players == 1:
                def players():
                    number = random.sample(range(roll),8)
                    number2 = random.sample(range(roll),8)
                    card = [number[:4]],[number[4:]],[number2[:4]],[number2[4:]]
                    return card
                def display_card(card):
                    for row in card:
                        print(row)
                player1_card = players()
                print("\nPlayer 1 card:")
                display_card(player1_card)
             
            if players == 2:
                def players():
                    number = random.sample(range(roll),8)
                    number2 = random.sample(range(roll),8)
                    card = [number[:4]],[number[4:]],[number2[:4]],[number2[4:]]
                    return card
                def display_card(card):
                    for row in card:
                        print(row)
                player1_card = players()
                print("\nPlayer 1 card:")
                display_card(player1_card)
                
                player2_card = players()
                print("\nPlayer 2 card:")
                display_card(player2_card)
            
            start = input("Do you wish to start the game?")
            if start != 'yes':
                print("Ok, try again later! Goodbye ")
                break
                
            #generate the bingo numbers
            generated_numbers = []
            while True:
                number_bingo = random.sample(range(roll),1)
                print("The number is:", number_bingo)
                time.sleep(1)
                
                
                generated_numbers.append(number_bingo)
                
                #bingo call 
                
                bingo_ok = input("Please write bingo if you have a set of number or press 'enter' to continue:  ")
                if bingo_ok == 'bingo':
                    break
                generated_numbers.append(number_bingo)
            def check_bingo(card,generated_numbers):
                count = 0
                for row in card:
                    for number in row:
                        if number in generated_numbers:
                            count += 1 
                return count <= 3
                
            if check_bingo(player1_card,generated_numbers):
                print("\nPlayer 1 wins!")
                break
            elif check_bingo(player2_card,generated_numbers):
                print("\nPlayer 2 wins!")
                break
            else:
                print("\nNo one wins!")
            break
            
            
roll = roll_numbers()
print()