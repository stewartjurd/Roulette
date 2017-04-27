import random
import time


def roulette(startbet, startbankbalance):
    bet = startbet
    bankbalance = startbankbalance
    while bet <= bankbalance:
        result = random.choice([True, False])
        if result:
            bankbalance += bet
            print "You bet $%d. You won. Total winnings $%d.\n" % (bet, bankbalance - startbankbalance)
            bet = startbet
        else:
            bankbalance -= bet
            print "You bet $%d. You lost. Total winnings $%d.\n" % (bet, bankbalance - startbankbalance)
            bet = bet*2
        time.sleep(0.1)
    print "The next bet would have cost $%d but you only had $%d left. Your final total was $%d.\n" % (bet, bankbalance, bankbalance - startbankbalance)
            
betinp = input("Enter starting bet:\n")
bankinp = input("Enter bank balance:\n")

roulette(betinp, bankinp)