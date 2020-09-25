import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"] * 4
answer = True
games_won = 0
total_games = 0
hitstay = "hit"
response = True


def horiz():
    print("***************")


def ace():
    horiz()
    for i in range(1, 2):
        print("*             *")
    for i in range(2, 3):
        print("*      *      *")
    for i in range(3, 4):
        print("*     * *     *")
    for i in range(4, 5):
        print("*    *   *    *")
    for i in range(5, 6):
        print("*   *     *   *")
    for i in range(6, 7):
        print("*   *******   *")
    for i in range(7, 9):
        print("*   *     *   *")
    for i in range(10, 11):
        print("*             *")
    horiz()


def two():
    horiz()
    for i in range(1, 2):
        print("*             *")
    for i in range(3, 4):
        print("*   *******   *")
    for i in range(5, 7):
        print("*         *   *")
    for i in range(8, 9):
        print("*   *******   *")
    for i in range(10, 12):
        print("*   *         *")
    for i in range(13, 14):
        print("*   *******   *")
    for i in range(15, 16):
        print("*             *")
    horiz()


def three():
    horiz()
    for i in range(1, 2):
        print("*             *")
    for i in range(3, 4):
        print("*   *******   *")
    for i in range(5, 7):
        print("*         *   *")
    for i in range(8, 9):
        print("*   *******   *")
    for i in range(10, 12):
        print("*         *   *")
    for i in range(13, 14):
        print("*   *******   *")
    for i in range(15, 16):
        print("*             *")
    horiz()


def four():
    horiz()
    for i in range(1, 2):
        print("*             *")
    for i in range(3, 6):
        print("*   *     *   *")
    for i in range(7, 8):
        print("*   *******   *")
    for i in range(9, 12):
        print("*         *   *")
    for i in range(13, 14):
        print("*             *")
    horiz()


def five():
    horiz()
    for i in range(1, 2):
        print("*             *")
    for i in range(3, 4):
        print("*   *******   *")
    for i in range(5, 7):
        print("*   *         *")
    for i in range(8, 9):
        print("*   *******   *")
    for i in range(10, 12):
        print("*         *   *")
    for i in range(13, 14):
        print("*   *******   *")
    for i in range(15, 16):
        print("*             *")
    horiz()


def six():
    horiz()
    for i in range(1, 2):
        print("*             *")
    for i in range(3, 4):
        print("*   *******   *")
    for i in range(5, 7):
        print("*   *         *")
    for i in range(8, 9):
        print("*   *******   *")
    for i in range(10, 12):
        print("*   *     *   *")
    for i in range(13, 14):
        print("*   *******   *")
    for i in range(15, 16):
        print("*             *")
    horiz()


def seven():
    horiz()
    for i in range(1, 2):
        print("*             *")
    for i in range(3, 4):
        print("*   *******   *")
    for i in range(5, 11):
        print("*         *   *")
    for i in range(11, 12):
        print("*             *")
    horiz()


def eight():
    horiz()
    for i in range(1, 2):
        print("*             *")
    for i in range(3, 4):
        print("*   *******   *")
    for i in range(5, 7):
        print("*   *     *   *")
    for i in range(8, 9):
        print("*   *******   *")
    for i in range(10, 12):
        print("*   *     *   *")
    for i in range(13, 14):
        print("*   *******   *")
    for i in range(15, 16):
        print("*             *")
    horiz()


def nine():
    horiz()
    for i in range(1, 2):
        print("*             *")
    for i in range(3, 4):
        print("*   *******   *")
    for i in range(5, 7):
        print("*   *     *   *")
    for i in range(8, 9):
        print("*   *******   *")
    for i in range(10, 12):
        print("*         *   *")
    for i in range(13, 14):
        print("*         *   *")
    for i in range(15, 16):
        print("*             *")
    horiz()


def ten():
    horiz()
    for i in range(1, 2):
        print("*             *")
    for i in range(3, 4):
        print("*   *  *****  *")
    for i in range(5, 6):
        print("*  **  *   *  *")
    for i in range(6, 10):
        print("*   *  *   *  *")
    for i in range(11, 12):
        print("*   *  *****  *")
    for i in range(13, 14):
        print("*             *")
    horiz()


def jack():
    horiz()
    for i in range(1, 2):
        print("*             *")
    for i in range(3, 4):
        print("*   *******   *")
    for i in range(5, 9):
        print("*       *     *")
    for i in range(9, 10):
        print("*  *   *      *")
    for i in range(11, 12):
        print("*   ***       *")
    for i in range(13, 14):
        print("*             *")
    horiz()


def queen():
    horiz()
    for i in range(1, 2):
        print("*             *")
    for i in range(3, 4):
        print("*    *****    *")
    for i in range(5, 9):
        print("*   *     *   *")
    for i in range(9, 10):
        print("*   *    **   *")
    for i in range(10, 11):
        print("*     *****   *")
    for i in range(12, 13):
        print("*          *  *")
    horiz()


def king():
    horiz()
    for i in range(1, 2):
        print("*             *")
    for i in range(2, 3):
        print("*   *     *   *")
    for i in range(3, 4):
        print("*   *    *    *")
    for i in range(4, 5):
        print("*   *  *      *")
    for i in range(5, 6):
        print("*   **        *")
    for i in range(6, 7):
        print("*   *  *      *")
    for i in range(7, 8):
        print("*   *    *    *")
    for i in range(8, 9):
        print("*   *     *   *")
    for i in range(9, 10):
        print("*             *")
    horiz()


while answer == True:
    while cards:
        total_games += 1
        total = 0
        house_total = 0
        # computer generates two cards, the first one will be shown,
        # the second will be hidden
        if not cards:
            print("...")
            print("The deck is empty, RESHUFFLING")
            print("...")
            cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"] * 4
        computer_card1 = random.choice(cards)

        if computer_card1 == "Jack":
            jack()
            house_total += 10
        elif computer_card1 == "Queen":
            queen()
            house_total += 10
        elif computer_card1 == "King":
            king()
            house_total += 10
        elif computer_card1 == "Ace":
            ace()
            house_total += 11
            if house_total >= 21:
                house_total -= 10
        elif computer_card1 == 2:
            two()
            house_total += computer_card1
        elif computer_card1 == 3:
            three()
            house_total += computer_card1
        elif computer_card1 == 4:
            four()
            house_total += computer_card1
        elif computer_card1 == 5:
            five()
            house_total += computer_card1
        elif computer_card1 == 6:
            six()
            house_total += computer_card1
        elif computer_card1 == 7:
            seven()
            house_total += computer_card1
        elif computer_card1 == 8:
            eight()
            house_total += computer_card1
        elif computer_card1 == 9:
            nine()
            house_total += computer_card1
        elif computer_card1 == 10:
            ten()
            house_total += computer_card1
        cards.remove(computer_card1)
        if not cards:
            print("...")
            print("The deck is empty, RESHUFFLING")
            print("...")
            cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"] * 4
        computer_card2 = random.choice(cards)

        if computer_card2 == "Jack":
            house_total += 10
        elif computer_card2 == "Queen":
            house_total += 10
        elif computer_card2 == "King":
            house_total += 10
        elif computer_card2 == "Ace":
            house_total += 11
            if house_total >= 21:
                house_total -= 10
        else:
            house_total += computer_card2
        cards.remove(computer_card2)
        print("My second card is hidden. Your turn.")
        print()

        while response == True:
            total = 0
            if not cards:
                print("...")
                print("The deck is empty, RESHUFFLING")
                print("...")
                cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"] * 4
            # now it is your turn to choose a card
            my_card1 = random.choice(cards)

            # add to the total to first card
            if my_card1 == "Jack":
                jack()
                total += 10
            elif my_card1 == "Queen":
                queen()
                total += 10
            elif my_card1 == "King":
                king()
                total += 10
            elif my_card1 == "Ace":
                ace()
                total += 11

            elif my_card1 == 2:
                two()
                total += my_card1
            elif my_card1 == 3:
                three()
                total += my_card1
            elif my_card1 == 4:
                four()
                total += my_card1
            elif my_card1 == 5:
                five()
                total += my_card1
            elif my_card1 == 6:
                six()
                total += my_card1
            elif my_card1 == 7:
                seven()
                total += my_card1
            elif my_card1 == 8:
                eight()
                total += my_card1
            elif my_card1 == 9:
                nine()
                total += my_card1
            elif my_card1 == 10:
                ten()
                total += my_card1
            cards.remove(my_card1)
            if not cards:
                print(...)
                print("The deck is empty, RESHUFFLING")
                print(...)
                cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"] * 4
            # add to total for second card
            my_card2 = random.choice(cards)
            if my_card2 == "Jack":
                jack()
                total += 10
            elif my_card2 == "Queen":
                queen()
                total += 10
            elif my_card2 == "King":
                king()
                total += 10
            elif my_card2 == "Ace":
                ace()
                answer1 = int(input("You got ace. Would you like to use 1 or 11? "))
                total += answer1
            elif my_card2 == 2:
                two()
                total += my_card2
            elif my_card2 == 3:
                three()
                total += my_card2
            elif my_card2 == 4:
                four()
                total += my_card2
            elif my_card2 == 5:
                five()
                total += my_card2
            elif my_card2 == 6:
                six()
                total += my_card2
            elif my_card2 == 7:
                seven()
                total += my_card2
            elif my_card2 == 8:
                eight()
                total += my_card2
            elif my_card2 == 9:
                nine()
                total += my_card2
            elif my_card2 == 10:
                ten()
                total += my_card2
            print()
            print(total, "is your total.")
            if total == 21:
                print("You got blackjack!")
                games_won += 1
                print()
                continue

            while True:
                hitstay = input("hit or stay: ")
                if hitstay == "hit":
                    break
                elif hitstay == "stay":
                    break
                else:
                    print("Invalid entry, try again")
                    continue

            while hitstay == "hit":

                if not cards:
                    print("...")
                    print("The deck is empty, RESHUFFLING")
                    print("...")
                    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"] * 4
                my_newcard = random.choice(cards)
                if my_newcard == "Jack":
                    jack()
                    total += 10
                elif my_newcard == "Queen":
                    queen()
                    total += 10
                elif my_newcard == "King":
                    king()
                    total += 10
                elif my_newcard == "Ace":
                    ace()
                    answer1 = int(input("You got ace. Would you like to use 1 or 11? "))
                    total += answer1
                elif my_newcard == 2:
                    two()
                    total += my_newcard
                elif my_newcard == 3:
                    three()
                    total += my_newcard
                elif my_newcard == 4:
                    four()
                    total += my_newcard
                elif my_newcard == 5:
                    five()
                    total += my_newcard
                elif my_newcard == 6:
                    six()
                    total += my_newcard
                elif my_newcard == 7:
                    seven()
                    total += my_newcard
                elif my_newcard == 8:
                    eight()
                    total += my_newcard
                elif my_newcard == 9:
                    nine()
                    total += my_newcard
                elif my_newcard == 10:
                    ten()
                    total += my_newcard
                else:
                    total += my_newcard
                cards.remove(my_newcard)
                if total > 21:
                    total = 0
                    print("Bust!")
                    break

                elif total == 21:
                    print("You got 21!")
                    games_won += 1
                    break
                else:
                    print(total, "is your new total")
                    print()
                while True:
                    hitstay = input("hit or stay: ")
                    if hitstay == "hit":
                        break
                    elif hitstay == "stay":
                        break
                    else:
                        print("Invalid entry, try again")
                        continue
            break

        print()
        print("It is the house's turn")
        print()
        print("2ND CARD")
        print()
        # Print computer_card2
        if computer_card2 == "Jack":
            jack()
        elif computer_card2 == "Queen":
            queen()
        elif computer_card2 == "King":
            king()
        elif computer_card2 == "Ace":
            ace()
        elif computer_card2 == 2:
            two()
        elif computer_card2 == 3:
            three()
        elif computer_card2 == 4:
            four()
        elif computer_card2 == 5:
            five()
        elif computer_card2 == 6:
            six()
        elif computer_card2 == 7:
            seven()
        elif computer_card2 == 8:
            eight()
        elif computer_card2 == 9:
            nine()
        elif computer_card2 == 10:
            ten()
        print("for a total of", house_total)
        print()
        while house_total <= 16:
            if not cards:
                print("...")
                print("The deck is empty, RESHUFFLING")
                print("...")
                cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"] * 4
            new_card = random.choice(cards)
            if new_card == "Jack":
                jack()
                house_total += 10
            elif new_card == "Queen":
                queen()
                house_total += 10
            elif my_card2 == "King":
                king()
                house_total += 10
            elif new_card == "Ace":
                ace()
                house_total += 11
                if house_total >= 21:
                    house_total -= 10
            elif new_card == 2:
                two()
                house_total += new_card
            elif new_card == 3:
                three()
                house_total += new_card
            elif new_card == 4:
                four()
                house_total += new_card
            elif new_card == 5:
                five()
                house_total += new_card
            elif new_card == 6:
                six()
                house_total += new_card
            elif new_card == 7:
                seven()
                house_total += new_card
            elif new_card == 8:
                eight()
                house_total += new_card
            elif new_card == 9:
                nine()
                house_total += new_card
            elif new_card == 10:
                ten()
                house_total += new_card

            if house_total > 21:
                house_total = 0
                print("BUST")
                break
            elif house_total == 21:
                print("I got 21")
                break
            else:
                print(house_total, "is my new total")
                print()

        if total > house_total:
            print("You win!")
            games_won += 1
        elif house_total > total:
            print("You lose.")
        elif house_total == total:
            print("Push")
        elif total > 21 and house_total > 21:
            print("Push")

        if not cards:
            print("...")
            print()
            print("The deck is empty, RESHUFFLING")
            print()
            print("...")
            cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"] * 4
        print()
        while True:
            answer = input("Would you like to play again (yes or no)? ")
            if answer == "yes":
                break
            elif answer == "no":
                break
            else:
                print("Invalid entry, try again")
                continue
        if answer == "no":
            break
    break

print("You won", games_won, "out of", total_games, "games.")


