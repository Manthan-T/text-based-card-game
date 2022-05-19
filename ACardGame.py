def a_card_game():
    import random
    import sys

    def generate_deck(deck):
        for suit in ["hearts", "diamonds", "clubs", "spades"]:
            for card in range(1, 14):
                if card == 1:
                    deck.append("Ace of " + suit)
                elif card == 11:
                    deck.append("Jack of " + suit)
                elif card == 12:
                    deck.append("Queen of " + suit)
                elif card == 13:
                    deck.append("King of " + suit)
                else:
                    deck.append(str(card) + " of " + suit)
                    
        random.shuffle(deck)

    def menu():
        valid_response = False

        while not valid_response:
            mode = input("Would you like to play manually or automatically? (Type x to quit): ")

            if mode == "manually":
                valid_response = True
                print("You completed the game in " + str(game()) + " draws!")                
            elif mode == "automatically":
                valid_response = True
                print("You completed the game in " + str(game()) + " draws!")
            elif mode == "x":
                print("Goodbye")
                sys.exit()
            else:
                print("That is not a valid response. Please try again: ")

    def game():
        deck = []
        hand = []
        generate_deck(deck)

        hearts_pile = "No cards yet"
        diamonds_pile = "No cards yet"
        clubs_pile = "No cards yet"
        spades_pile = "No cards yet"

        ace_present = False
        game_running = True
        prev_invalid = False
        cannot_play_card = False
        cards_drawn = 0
        
        while not ace_present:
            for card in range(0, 5):
                hand.append(deck.pop(0))
            for card in hand:
                if card.find("Ace") != -1:
                    ace_present = True
            if not ace_present:
                deck += hand
                hand.clear()
                random.shuffle(deck)
            cards_drawn += 5

        while game_running:
            print("\n##########################################################################################\n")
            print("                                         Your hand:")
            for card in hand:
                print("                                         " + str(hand.index(card) + 1) + ") " + card)

            print("\n                          Top card on the pile of hearts: " + hearts_pile)
            print("                          Top card on the pile of diamonds: " + diamonds_pile)
            print("                          Top card on the pile of clubs: " + clubs_pile)
            print("                          Top card on the pile of spades: " + spades_pile)
            print("\n##########################################################################################")
            
            if prev_invalid == True:
                choice = input("\nThat is not a valid reponse. Please try again: Would you like to draw (\"n\"), quit (\"q\"), or play a card (\"p\"): ")
                prev_invalid = False
            elif cannot_play_card == True:
                choice = input("\nYou cannot play that card. Please try again: Would you like to draw (\"n\"), quit (\"q\"), or play a card (\"p\"): ")
                cannot_play_card = False
            else:
                choice = input("\nWould you like to draw (\"n\"), quit (\"q\"), or play a card (\"p\"): ")

            if choice == "n":
                if len(deck) != 0:
                    hand.append(deck.pop(0))
                    cards_drawn += 1
                else:
                    print("The deck is empty")
                    prev_invalid = True

            elif choice == "p":
                play = input("Which card number would you like to play? (Enter the number or enter \"q\" to quit): ")
                if play == "q":
                    print("Cards drawn: " + cards_drawn)
                    print("Goodbye")
                    sys.exit()

                else:
                    try:
                        play = int(play) - 1
                        if play in range(0, len(hand)):
                            match hand[play][hand[play].rfind(" ") + 1:]:
                                case "hearts":
                                    if hand[play][0:hand[play].find(" ")] == "Ace" and hearts_pile == "No cards yet":
                                        hearts_pile = "Ace"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == "2" and hearts_pile == "Ace":
                                        hearts_pile = "2"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == "Jack" and hearts_pile == "10":
                                        hearts_pile = "Jack"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == "Queen" and hearts_pile == "Jack":
                                        hearts_pile = "Queen"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == "King" and hearts_pile == "Queen":
                                        hearts_pile = "King (Completed pile)"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == str(int(hearts_pile) + 1):
                                        hearts_pile = hand[play][0:hand[play].find(" ")]
                                        hand.pop(play)
                                    else:
                                        cannot_play_card = True
                                case "diamonds":
                                    if hand[play][0:hand[play].find(" ")] == "Ace" and diamonds_pile == "No cards yet":
                                        diamonds_pile = "Ace"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == "2" and diamonds_pile == "Ace":
                                        diamonds_pile = "2"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == "Jack" and diamonds_pile == "10":
                                        diamonds_pile = "Jack"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == "Queen" and diamonds_pile == "Jack":
                                        diamonds_pile = "Queen"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == "King" and diamonds_pile == "Queen":
                                        diamonds_pile = "King (Completed pile)"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == str(int(diamonds_pile) + 1):
                                        diamonds_pile = hand[play][0:hand[play].find(" ")]
                                        hand.pop(play)
                                    else:
                                        cannot_play_card = True
                                case "clubs":
                                    if hand[play][0:hand[play].find(" ")] == "Ace" and clubs_pile == "No cards yet":
                                        clubs_pile = "Ace"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == "2" and clubs_pile == "Ace":
                                        clubs_pile = "2"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == "Jack" and clubs_pile == "10":
                                        clubs_pile = "Jack"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == "Queen" and clubs_pile == "Jack":
                                        clubs_pile = "Queen"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == "King" and clubs_pile == "Queen":
                                        clubs_pile = "King (Completed pile)"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == str(int(clubs_pile) + 1):
                                        clubs_pile = hand[play][0:hand[play].find(" ")]
                                        hand.pop(play)
                                    else:
                                        cannot_play_card = True
                                case "spades":
                                    if hand[play][0:hand[play].find(" ")] == "Ace" and spades_pile == "No cards yet":
                                        spades_pile = "Ace"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == "2" and spades_pile == "Ace":
                                        spades_pile = "2"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == "Jack" and spades_pile == "10":
                                        spades_pile = "Jack"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == "Queen" and spades_pile == "Jack":
                                        spades_pile = "Queen"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == "King" and spades_pile == "Queen":
                                        spades_pile = "King (Completed pile)"
                                        hand.pop(play)
                                    elif hand[play][0:hand[play].find(" ")] == str(int(spades_pile) + 1):
                                        spades_pile = hand[play][0:hand[play].find(" ")]
                                        hand.pop(play)
                                    else:
                                        cannot_play_card = True
                            
                        else:
                            prev_invalid = True

                    except:
                        prev_invalid = True

            elif choice == "q":
                print("Cards drawn: " + str(cards_drawn))
                print("Goodbye")
                sys.exit()

            else:
                prev_invalid = True
            
            if len(hand) == 0 and len(deck) == 0:
                game_running = False
        
        return cards_drawn

    menu()

a_card_game()