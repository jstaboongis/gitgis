import os
from random import randint
global number
global cards
global cards2
global player1money
global player2money
global player3money
global player4money
global p1wins
global p2wins
global p3wins
global p4wins
global p1loses
global p2loses
global p3loses
global p4loses
p1wins = 0
p2wins = 0
p3wins = 0
p4wins = 0
p1loses = 0
p2loses = 0
p3loses = 0
p4loses = 0
player1money = 400
player2money = 400
player3money = 400
player4money = 400

cards = ['A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2']
cards2 = cards



numbers = range(0,208,1)
numbers2 = range(0,208,1)



for i in range(0,700,1):
    x = randint(0,207)
    index = numbers.index(x)
    numbers2[index] = 999


for i in numbers2:
    if i != 999:
        x = 0


   
def getcard():
    x = randint(0,207)
    card = cards[x]
    cards[x] = 999
    if card == 999:
        while card == 999:
            x = randint(0,207)
            card = cards[x]
        cards[x] = 999
        
def getcard2():
    global cards
    global cards2
    length = len(cards)
    run = "yes"
    
    if length == 0:
        cards = ['A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2','A','K','J','Q','10','9','8','7','6','5','4','3','2']
        run = "no"

    if run == "yes":
        x = randint(0,(length - 1))
        card = cards[x]
        del cards[x]
        return card






def roundbj():
    dealer = []
    player1 = []
    player2 = []
    player3 = []
    player4 = []
    player1score = 0
    player2score = 0
    player3score = 0
    player4score = 0
    #player1money = player1money - 20
    #player2money = player2money - 20
    #player3money = player3money - 20
    #player4money = player4money - 20
    global player1money
    global player2money
    global player3money
    global player4money

    
    player4.append(getcard2())
    player4.append(getcard2())
    player1.append(getcard2())
    player1.append(getcard2())
    player2.append(getcard2())
    player2.append(getcard2())
    player3.append(getcard2())
    player3.append(getcard2())

    dealer.append(getcard2())
    player1score = getscore(player1)
    player2score = getscore(player2)
    player3score = getscore(player3)
    player4score = getscore(player4)
    dealerscore = getscore(dealer)

    #player4
    if player4score < 16 and dealerscore == 10:
        player4.append(getcard2())
        player4score = getscore(player4)

    if dealerscore < 4 and player4score < 13:
        player4.append(getcard2())
    elif player4score < 13:
        player4.append(getcard2())
        player4score = getscore(player4)
        if player4score < 13:
            player4.append(getcard2())
            player4score = getscore(player4)
        if player4score < 13:
            player4.append(getcard2())
            player4score = getscore(player4)
        if player4score < 13:
            player4.append(getcard2())
            player4score = getscore(player4)
    else:
        nulll = 0

    #player1
    if player1score < 16 and dealerscore == 10:
        player1.append(getcard2())
        player1score = getscore(player1)
    else:
        if player1score < 13:
            player1.append(getcard2())
            player1score = getscore(player1)
    if player1score < 13:
        player1.append(getcard2())
        player1score = getscore(player1)
    if player1score < 13:
        player1.append(getcard2())
        player1score = getscore(player1)
    if player1score < 13:
        player1.append(getcard2())
        player1score = getscore(player1)
    if player1score < 13:
        player1.append(getcard2())
        player1score = getscore(player1)

    #player2
    if player2score < 16 and dealerscore == 10:
        player2.append(getcard2())
        player2score = getscore(player2)
    else:
        if player2score < 13:
            player2.append(getcard2())
            player2score = getscore(player2)
    if player2score < 13:
        player2.append(getcard2())
        player2score = getscore(player2)
    if player2score < 13:
        player2.append(getcard2())
        player2score = getscore(player2)
    if player2score < 13:
        player2.append(getcard2())
        player2score = getscore(player2)
    if player2score < 13:
        player2.append(getcard2())
        player2score = getscore(player2)


        
    #player3
    if player3score < 16 and dealerscore == 10:
        player3.append(getcard2())
        player3score = getscore(player3)
    else:
        if player3score < 13:
            player3.append(getcard2())
            player3score = getscore(player3)
    if player3score < 13:
        player3.append(getcard2())
        player3score = getscore(player3)
    if player3score < 13:
        player3.append(getcard2())
        player3score = getscore(player3)
    if player3score < 13:
        player3.append(getcard2())
        player3score = getscore(player3)
    if player3score < 13:
        player3.append(getcard2())
        player3score = getscore(player3)


    

    #dealer
    if dealerscore < 17:
        dealer.append(getcard2())
        dealerscore = getscore(dealer)

    if dealerscore < 17:
        dealer.append(getcard2())
        dealerscore = getscore(dealer)

    if dealerscore < 17:
        dealer.append(getcard2())
        dealerscore = getscore(dealer)
    
    if dealerscore < 17:
        dealer.append(getcard2())
        dealerscore = getscore(dealer)

    if dealerscore < 17:
        dealer.append(getcard2())
        dealerscore = getscore(dealer)

    if dealerscore < 17:
        dealer.append(getcard2())
        dealerscore = getscore(dealer)

    #p1
    if player1score > 21:
        player1money = player1money - 20
    elif player1score == 21 and dealerscore != 21:
        player1money = player1money + 25
    elif player1score > dealerscore and player1score < 22 and dealerscore < 22:
        player1money = player1money + 20
    elif player1score < 22 and dealerscore > 21:
        player1money = player1money + 20
    elif player1score == dealerscore:
        nulll = 0
    else:
        player1money = player1money - 20

    if player4score > 21:
        player4money = player4money - 20
    elif player4score == 21 and dealerscore != 21:
        player4money = player4money + 25
    elif player4score > dealerscore and player4score < 22 and dealerscore < 22:
        player4money = player4money + 20
    elif player4score < 22 and dealerscore > 21:
        player4money = player4money + 20
    elif player4score == dealerscore:
        nulll = 0
    else:
        player4money = player4money - 20

        
    if player2score > 21:
        player2money = player2money - 20
    elif player2score == 21 and dealerscore != 21:
        player2money = player2money + 25
    elif player2score > dealerscore and player2score < 22 and dealerscore < 22:
        player2money = player2money + 20
    elif player2score < 22 and dealerscore > 21:
        player2money = player2money + 20
    elif player2score == dealerscore:
        nulll = 0
    else:
        player2money = player2money - 20


    if player3score > 21:
        player3money = player3money - 20
    elif player3score == 21 and dealerscore != 21:
        player3money = player3money + 25
    elif player3score > dealerscore and player3score < 22 and dealerscore < 22:
        player3money = player3money + 20
    elif player3score < 22 and dealerscore > 21:
        player3money = player3money + 20
    elif player3score == dealerscore:
        nulll = 0
    else:
        player3money = player3money - 20



##    print "================================"
##    print "Dealer Score: " + str(dealerscore)
##    print str(player1money) + "$ P1, score" + str(player1score)
##    print str(player2money) + "$ P2, score" + str(player2score)
##    print str(player3money) + "$ P3, score" + str(player3score)
##    print str(player4money) + "$ P4, score" + str(player4score)
##    print "================================"
    
        
def getscore(list):
    score = 0
    for item in list:
        if item == '2':
            score += 2
        elif item == '3':
            score += 3
        elif item == '4':
            score += 4
        elif item == '5':
            score += 5
        elif item == '6':
            score += 6
        elif item == '7':
            score += 7
        elif item == '8':
            score += 8
        elif item == '9':
            score += 9
        elif item == '10':
            score += 10
        elif item == 'J':
            score += 10
        elif item == 'Q':
            score += 10
        elif item == 'K':
            score += 10
        else:
            if score <= 10:
                score += 11
            else:
                score += 1
    return score


countf = 0
avgp1 = 0
avgp2 = 0
avgp3 = 0
avgp4 = 0 
for i in range(1,5):
    countf += 1
    
    
    for i in range(1,40):
        for i in range(1,400):
            roundbj()
    ##    print "==================================================="
    ##    print "P1$ = " + str(player1money)
    ##    print "P2$ = " + str(player2money)
    ##    print "P3$ = " + str(player3money)
    ##    print "P4$ = " + str(player4money)
    ##    print "==================================================="
        if player1money >= 400:
            p1wins += 1
        else:
            p1loses += 1
        if player2money >= 400:
            p2wins += 1
        else:
            p2loses += 1
        if player3money >= 400:
            p3wins += 1
        else:
            p3loses += 1
        if player4money >= 400:
            p4wins += 1
        else:
            p4loses += 1
        player1money = 400
        player2money = 400
        player3money = 400
        player4money = 400
        

    print "RESULTS"
    avgp1 += (float(p1wins)/p1loses)
    avgp2 += (float(p2wins)/p2loses)
    avgp3 += (float(p3wins)/p3loses)
    avgp4 += (float(p4wins)/p4loses)
    print "player 1 had %s wins and %s losses. %s percent were wins." % (p1wins,p1loses,(float(p1wins)/p1loses)*100)
    print "player 2 had %s wins and %s losses. %s percent were wins." % (p2wins,p2loses,(float(p2wins)/p2loses)*100)
    print "player 3 had %s wins and %s losses. %s percent were wins." % (p3wins,p3loses,(float(p3wins)/p3loses)*100)
    print "player 4 had %s wins and %s losses. %s percent were wins." % (p4wins,p4loses,(float(p4wins)/p4loses)*100)
    p1wins = 0
    p2wins = 0
    p3wins = 0
    p4wins = 0
    p1loses = 0
    p2loses = 0
    p3loses = 0
    p4loses = 0
avgp1 = avgp1/countf
avgp2 = avgp2/countf
avgp3 = avgp3/countf
avgp4 = avgp4/countf
print "FINAL AVERAGES"
print "player 1 had an average win percentage of %s." % (avgp1)
print "player 2 had an average win percentage of %s." % (avgp2)
print "player 3 had an average win percentage of %s." % (avgp3)
print "player 4 had an average win percentage of %s." % (avgp4)
