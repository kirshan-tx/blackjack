#pyuic5 -x view.ui -o view.py

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from view import *
import random
from strat import *
#import time

class Blackjack(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        #set window icon and name
        self.setWindowTitle("Black Jack!")
        self.setWindowIcon(QtGui.QIcon('images/icon.png'))

        #main menu start button
        self.button_start.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.game))

        #instructions button 
        self.button_instructions.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.instructions))
        self.button_instructions_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.instructions))

        #game buttons
        self.button_shuffle.clicked.connect(lambda: self.shuffle())
        self.button_hit.clicked.connect(lambda: self.player_hit())
        self.button_stand.clicked.connect(lambda: self.stand())
        self.button_bet.clicked.connect(lambda: self.bet())

        #bet slider and button 
        self.horizontalSlider.setMinimum(10)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(10)
        self.horizontalSlider.setSingleStep(10)
        self.horizontalSlider.valueChanged.connect(self.bet_value)
        #self.horizontalSlider.valueChanged.connect(self.bet)

        #bankroll 
        self.bankroll = 200

        #disable buttons
        self.button_hit.setEnabled(False)
        self.button_stand.setEnabled(False)
        self.button_shuffle.setEnabled(False)

    def bet(self):
        #stop slider and get bet value
        self.bet = self.horizontalSlider.value()
        self.horizontalSlider.setEnabled(False)

        #open shuffle button
        self.button_shuffle.setEnabled(True)
        #close bet button
        self.button_bet.setEnabled(False)

    #show bet value from slider
    def bet_value(self, value):
        self.label_bet.setText(f'${value}')

    #stand
    def stand(self):
        self.label_dealer1.setPixmap(self.pos_2_pixmap)

        self.button_hit.setEnabled(False)
        self.button_stand.setEnabled(False)

        self.player_total = sum(self.player_score)
        self.dealer_total = sum(self.dealer_score)

        #logic
        if self.dealer_total >= 17:
            #dealer stops hitting
            if self.dealer_total > 21:
                self.label_result.setText(f'Player Wins with {self.player_total}!!')   
                self.label_dealer_total.setText(f'Total: {self.dealer_total}')         
            elif self.dealer_total == self.player_total:
                self.label_result.setText(f'It\'s a Tie.')   
                self.label_dealer_total.setText(f'Total: {self.dealer_total}')
            elif self.dealer_total > self.player_total:
                self.label_result.setText(f'Dealer Wins with {self.dealer_total}.')             
                self.label_dealer_total.setText(f'Total: {self.dealer_total}')
            else:
                self.label_result.setText(f'Player Wins with {self.player_total}!!')  
                self.label_dealer_total.setText(f'Total: {self.dealer_total}')          

        #dealer needs another card
        else:
            self.dealer_hit()
            self.stand()
            #time here??

    #check for blackjack
    def blackjack_check(self, party): 
        self.player_total = 0
        self.dealer_total = 0

        if party == 'dealer':
            if len(self.dealer_score) == 2:
                if self.dealer_score[0] + self.dealer_score[1] == 21:
                    self.blackjack_status['dealer'] = 'yes'
            
            #dealer ace conversion
            self.dealer_total = sum(self.dealer_score)
            if self.dealer_total > 21:
                for card_num, card in enumerate(self.dealer_score):
                        if card == 11:
                            self.dealer_score[card_num] = 1 #change 11 to 1

                            #update dealer total
                            self.dealer_total = sum(self.dealer_score)

        if party == 'player':
            if len(self.player_score) == 2:
                if self.player_score[0] + self.player_score[1] == 21:
                    self.blackjack_status['player'] = 'yes'
            else:
                self.player_total = sum(self.player_score)
                if self.player_total == 21:
                    self.blackjack_status["player"] = "yes"
                elif self.player_total > 21:
                    #check for ace
                    for card_num, card in enumerate(self.player_score):
                        if card == 11:
                            self.player_score[card_num] = 1 #change 11 to 1
                            self.player_total = sum(self.player_score) #update player total
                            self.label_player_total.setText(f'Total: {self.player_total}')
                            break # do once

                    if self.player_total == 21:
                        self.blackjack_status["player"] = "yes"
                    if self.player_total > 21:
                        self.blackjack_status["player"] = "bust"

        #wait for player to get both cards to check for tie
        if len(self.player_score) < 2:
            return

        #check for initial blackjack 
        if len(self.player_score) == 2 and len(self.dealer_score) == 2:
            #both blackjack
            if self.blackjack_status['player'] == 'yes' and self.blackjack_status['dealer'] == 'yes':
                self.label_dealer1.setPixmap(self.pos_2_pixmap)
                self.label_result.setText(f'Push!...It\'s a tie.')   
                self.label_dealer_total.setText(f'Total: {self.dealer_total}')
                self.button_hit.setEnabled(False)
                self.button_stand.setEnabled(False)

                self.blackjack_status["player"] = "no"
                self.blackjack_status["dealer"] = "no"


            #player blackjack
            if self.blackjack_status['player'] == 'yes':
                self.label_result.setText(f'Blackjack! Player Wins!!')   
                self.button_hit.setEnabled(False)
                self.button_stand.setEnabled(False)

                self.blackjack_status["player"] = "no"

            #dealer blackjack
            elif self.blackjack_status['dealer'] == 'yes':
                self.label_dealer1.setPixmap(self.pos_2_pixmap)
                self.label_result.setText(f'Dealer Blackjack.') 
                self.label_dealer_total.setText(f'Total: 21')
                self.button_hit.setEnabled(False)
                self.button_stand.setEnabled(False)

                self.blackjack_status["dealer"] = "no"

        else:
            #tie
            if self.blackjack_status['player'] == 'yes' and self.blackjack_status['dealer'] == 'yes':
                self.label_result.setText(f'Push!...It\'s a tie.')   
                self.label_dealer_total.setText(f'Total: {self.dealer_total}')
                self.button_hit.setEnabled(False)
                self.button_stand.setEnabled(False)

                self.blackjack_status["player"] = "no"
                self.blackjack_status["dealer"] = "no"

            #player win
            elif self.blackjack_status['player'] == 'yes':
                self.label_result.setText(f'21!! You got it!')   
                self.label_dealer_total.setText(f'Total: {self.dealer_total}')
                self.button_hit.setEnabled(False)
                self.button_stand.setEnabled(False)

                self.blackjack_status["player"] = "no"

            #dealer win
            elif self.blackjack_status['dealer'] == 'yes':
                self.label_result.setText(f'21! Dealer wins.')   
                self.label_dealer_total.setText(f'Total: {self.dealer_total}')
                self.button_hit.setEnabled(False)
                self.button_stand.setEnabled(False)

                self.blackjack_status["dealer"] = "no"

        #player bust
        if self.blackjack_status['player'] == 'bust':
            self.label_dealer1.setPixmap(self.pos_2_pixmap)
            self.label_result.setText(f'BUST!!! Dealer Win.')   
            self.button_hit.setEnabled(False)
            self.button_stand.setEnabled(False)
    
    def shuffle(self): 
        #clear textboxes
        self.label_result.setText("")
        self.label_dealer_total.setText("")

        #score totals
        self.player_total = 0
        self.dealer_total = 0

        #blackjack status dict 
        self.blackjack_status = {'dealer': 'no', 'player':'no'}

        #enable buttons
        self.button_hit.setEnabled(True)
        self.button_stand.setEnabled(True)

        #set blank card slots
        pixmap = QPixmap('images/blank.png')
        self.label_player2.setPixmap(pixmap)
        self.label_player3.setPixmap(pixmap)
        self.label_player4.setPixmap(pixmap)
        self.label_dealer2.setPixmap(pixmap)
        self.label_dealer3.setPixmap(pixmap)
        self.label_dealer4.setPixmap(pixmap)


        #define deck
        suits = ['diamonds', 'clubs', 'hearts', 'spades']
        values = range(2,15)
        # jack=11, queen=12, king=13, ace=14

        #create deck
        self.deck = []

        for suit in suits:
            for value in values:
                self.deck.append(f"{value}_of_{suit}")
        

        self.dealer = []
        self.player = []
        self.dealer_score = []
        self.player_score = []

        #card slot position
        self.player_pos = 0 
        self.dealer_pos = 0

        #first 2 dealer and player cards 
        self.dealer_hit()
        self.dealer_hit()

        self.player_hit()
        self.player_hit()



    def player_hit(self):
        if self.player_pos <= 5:
            try:
                card = random.choice(self.deck) #random card
                self.deck.remove(card) #remove that card

                #add to score
                self.player_card = int(card.split("_",1)[0])
                if self.player_card == 14:
                    self.player_score.append(11)
                elif self.player_card in [11,12,13]:
                    self.player_score.append(10)
                else:
                    self.player_score.append(self.player_card)

                self.player.append(card) #add card to player

                #output card 
                pixmap = QPixmap(f'images/{card}.png')

                if self.player_pos == 0:
                    self.label_player0.setPixmap(pixmap)
                    self.player_pos += 1

                elif self.player_pos == 1:
                    self.label_player1.setPixmap(pixmap)
                    self.player_pos += 1
                
                elif self.player_pos == 2:
                    self.label_player2.setPixmap(pixmap)
                    self.player_pos += 1

                elif self.player_pos == 3:
                    self.label_player3.setPixmap(pixmap)
                    self.player_pos += 1

                elif self.player_pos == 4:
                    self.label_player4.setPixmap(pixmap)
                    self.player_pos += 1

                    # 5 card
                    self.player_total = sum(self.player_score)
                    
                    if self.player_total <= 21:
                        self.button_hit.setEnabled(False)
                        self.button_stand.setEnabled(False)
                        self.label_result.setText(f'5-Card!!! That\'s a lotta cards!')   
                        self.label_dealer_total.setText(f'Total: {self.dealer_total}')
                
            except Exception as e:
                print(e)


            #show sum, taking into consideration of aces
            self.player_total = sum(self.player_score)

            if 11 in self.player_score and self.player_total > 21:
                self.player_total = 0
                for i in self.player_score:
                    if i == 11:
                        i = 1
                    self.player_total += i

            self.label_player_total.setText(f'Total: {self.player_total}') #display player total
            self.label_strat.setText(f'{strat(self.player_score, self.dealer_score)}')

            #check for blackjack
            self.blackjack_check("player")

    def dealer_hit(self):
        if self.dealer_pos <= 5:
            try:
                card = random.choice(self.deck) #random card
                self.deck.remove(card) #remove that card

                #add to score
                self.dealer_card = int(card.split("_",1)[0])
                if self.dealer_card == 14:
                    self.dealer_score.append(11)
                elif self.dealer_card in [11,12,13]:
                    self.dealer_score.append(10)
                else:
                    self.dealer_score.append(self.dealer_card)

                self.dealer.append(card) #add card to player
    
                #output card 
                pixmap = QPixmap(f'images/{card}.png')

                if self.dealer_pos == 0:
                    self.label_dealer0.setPixmap(pixmap)
                    self.dealer_pos += 1

                elif self.dealer_pos == 1:
                    self.pos_2_pixmap = pixmap
                    self.label_dealer1.setPixmap(QPixmap(f'images/back.png'))
                    self.dealer_pos += 1
                
                elif self.dealer_pos == 2:
                    self.label_dealer2.setPixmap(pixmap)
                    self.dealer_pos += 1

                elif self.dealer_pos == 3:
                    self.label_dealer3.setPixmap(pixmap)
                    self.dealer_pos += 1

                elif self.dealer_pos == 4:
                    self.label_dealer4.setPixmap(pixmap)
                    self.dealer_pos += 1

                # 5 card
                    self.dealer_total = sum(self.dealer_score)
                    
                    if self.dealer_total <= 21:
                        self.button_hit.setEnabled(False)
                        self.button_stand.setEnabled(False)
                        self.label_result.setText(f'5 Card! Dealer Wins.')   
                        self.label_dealer_total.setText(f'Total: {self.dealer_total}')

            except Exception as e:
                print(e)

            #check for blackjack
            self.blackjack_check("dealer")


    
