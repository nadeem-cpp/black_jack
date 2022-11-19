import random as rd

# constant limiting score
BURST_SCORE = 21
TERMINATE = -999

#display cards in more readable way
def display(player):

    def to_str(cards):
        string_cards = ""
        for card in cards:
            if type(card) is int:
                string_cards += str(card)
            else:
                string_cards += card
            string_cards += " , "

        return string_cards  

    print(f"{player['id']} got '{to_str(player['cards'])}' cards with total score of {player['actual_score']} ")

         

# return random card
def random_cards():
    """ select random card and return it"""
    cards = [2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 'jack' , 'king' , 'queen' , 'ace']
    return rd.choice(cards)
    
# return score according to cards
def scoring(cards , user):
    """ get cards and return the total score 
    give 2nd parameter True for user and false for dealer"""
    score = 0

    def decision(card):
        sc = 0
        if type(card) is int:
            sc += card
        else:
            if card == "ace":
                sc += 11
            else:
                sc += 10
        return sc
    
    if type(cards) is list:
        for card in cards:
            score += decision(card)
    # when card is not list  for dealer's shown_score
    else:
        return decision(cards)

    return score

# simple game ai 
def dealer_AI(dealer , user):

    dealer += scoring(random_cards() , False)
    # print("entering ai")
    if (dealer > BURST_SCORE):
        # user has won
        print(f"dealer score is {dealer} so dealer has bursted ")
        print("you win")
        return TERMINATE

    elif (user > dealer):
        dealer_AI(dealer=dealer , user=user)

    elif dealer > user:
        print(f"dealer score is {dealer}")
        print("you lose")
        return TERMINATE

## game function called by main function
def black_jack():

    user = {
        # id for interactive display 
        "id":"user",
        "actual_score": 0,
        "shown_score": 0,
        "cards": []
    }
    dealer = {
        "id":"dealer",
        "actual_score": 0,
        "shown_score": 0,
        "cards": []
    }

    # select 2 random cards for user and dealer random_cards() and save it in a list
    for i in range(2):
        user["cards"].append(random_cards())

    for i in range(2):
        dealer["cards"].append(random_cards())

    # calculate actual and shown score for each
    # shown score is shown to opponent rather than actual score
    user["actual_score"] = scoring(user["cards"] , True)
    user["shown_score"] = scoring(user["cards"][0] , True)
    
    dealer["actual_score"] = scoring(dealer["cards"] , False)
    dealer["shown_score"] = scoring(dealer["cards"][0] , False)
    

    # display score of the cards
    display(user)
    display(dealer)

    # user  can call hit() to get extra card
    choice = input("Enter your choice\n 1: hit\n 2: stand\n")
    terminate = 0
    while terminate != TERMINATE:
        if choice == "1":
            user["cards"].append(random_cards())
            user["actual_score"] += scoring(user["cards"][-1] , True)
            display(user)

            # burst cards
            if (user["actual_score"] > BURST_SCORE):
                print("you lose")
                terminate = TERMINATE
            else:
                choice = input("Enter your choice\n 1: hit\n 2: stand\n")
        # stand
        else:
            display(user)
            display(dealer)

            if (user["actual_score"] < dealer["actual_score"]):
                print("dealer has won")
                terminate = TERMINATE
            # elif (user["actual_score"] == dealer["actual_score"]):
            #     print("DRAW! equal score")
            #     terminate = TERMINATE
            else:
                terminate = dealer_AI(dealer["actual_score"] , user["actual_score"])

    # once user hit stand() , dealer can also hit() to get extra cards to increase its score
    # call is_win() to check if user has won the game or lose
    
def main():
    black_jack()

if __name__ == "__main__":
    main()