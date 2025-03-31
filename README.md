# Bingo Game  

### In this project, the main skills required are:
- import time
- import random
- using functions within functions.
- using count

The import time.sleep(1) is used to delay the time ( one second) between the rolls so that a little bit of tension is applied. Like below:

    '''
   
    generated_numbers = []
            while True:
                number_bingo = random.sample(range(roll),1)
                print("The number is:", number_bingo)
                time.sleep(1)
                generated_numbers.append(number_bingo)
               
    '''

The import random is used to generate the random numbers. The (roll) is the number the user has inputed regarding the maximum amount of faces that they want :

    '''

    def players():
                    number = random.sample(range(roll),8)
                    number2 = random.sample(range(roll),8)



    '''


The count has been used to count how many values that have been rolled exist in the current bingo sheet:


    '''

    def check_bingo(card,generated_numbers):
                count = 0
                for row in card:
                    for number in row:
                        if number in generated_numbers:
                            count += 1
                return count <= 3

    '''

The video below showcases how the project turned out. I have showcased the game with for one person. There is also an option for two people:



https://github.com/user-attachments/assets/f883699a-4230-43f7-8fac-1daa2794f260






This is how I have added the bingo sheet. I have made the board 4x4 so that it can be 'bingo' horizontally or vertically. As below:


    '''

    card = [number[:4]],[number[4:]],[number2[:4]],[number2[4:]]
                    return card
                def display_card(card):
                    for row in card:
                        print(row)
                player1_card = players()
                print("\nPlayer 1 card:")
                display_card(player1_card)

    '''

##### The game can be adjusted to more than 2 players but it needs to be adjusted. 
