'''
Created on 2013-06-06

@author: Emilio Tunno
Version: 1.2 Gui with hopes of full functionality minus the bet inputs==
'''
import pygame
import pygbutton
import sys
import slotmachine_0_1
import random

imgZomb = pygame.image.load('Zombie.png')
imgDia = pygame.image.load('Diamond.png')
imgGold = pygame.image.load('Gold.png')
imgIron = pygame.image.load('Iron.png')
imgRedstone = pygame.image.load('Redstone.png')
imgQuartz = pygame.image.load('Quartz.png')
imgWood = pygame.image.load('Wood.png')
imgEmerald = pygame.image.load('Emerald.png')

def Reels():
    """ When this function is called it determines the Bet_Line results.
        e.g. Bar - Orange - Banana """
        
    # [0]Fruit, [1]Fruit, [2]Fruit
    Bet_Line = [" "," "," "]
    Outcome = [0,0,0]
    
    # Spin those reels
    for spin in range(3):
        Outcome[spin] = random.randrange(1,65,1)
        # Spin those Reels!
        if Outcome[spin] >= 1 and Outcome[spin] <=26:   # 40.10% Chance
            Bet_Line[spin] = "Zombie"
        if Outcome[spin] >= 27 and Outcome[spin] <=36:  # 16.15% Chance
            Bet_Line[spin] = "Wood"
        if Outcome[spin] >= 37 and Outcome[spin] <=45:  # 13.54% Chance
            Bet_Line[spin] = "Redstone"
        if Outcome[spin] >= 46 and Outcome[spin] <=53:  # 11.98% Chance
            Bet_Line[spin] = "Quartz"
        if Outcome[spin] >= 54 and Outcome[spin] <=58:  # 7.29%  Chance
            Bet_Line[spin] = "Iron"
        if Outcome[spin] >= 59 and Outcome[spin] <=61:  # 5.73%  Chance
            Bet_Line[spin] = "Gold"
        if Outcome[spin] >= 62 and Outcome[spin] <=63:  # 3.65%  Chance
            Bet_Line[spin] = "Emerald"  
        if Outcome[spin] == 64:                         # 1.56%  Chance
            Bet_Line[spin] = "Diamond"    

    
    return Bet_Line


def main():
    pygame.init()
    
    Player_Money = 1000
    Jack_Pot = 500
    Turn = 1
    Bet = 0
    Prev_Bet=0
    win_number = 0
    loss_number = 0
    
    #D - Display configuration
    screen = pygame.display.set_mode((615, 540))
    pygame.display.set_caption("Minecraft Slots")
    
    #E - Entities (just background for now)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background = pygame.image.load("Blankreels.png")
    
    #A - Action (broken into ALTER steps)
    
    myFont = pygame.font.SysFont("Times New Roman", 30)
    Betlabel = myFont.render("Bet", 1, (255, 255, 255))
    
    myFont = pygame.font.SysFont("Times New Roman", 30)
    Pocketlabel = myFont.render("Pocket", 1, (255, 255, 255))
    
    myFont = pygame.font.SysFont("Times New Roman", 30)
    Jackpotlabel = myFont.render("Jackpot", 1, (255, 255, 255))
    
    #intializing my buttons
    Spinbutton = pygbutton.PygButton((30,400,150,30), "Spin!")
    Resetbutton = pygbutton.PygButton((30,440,150,30), "Reset?")
    Quitbutton = pygbutton.PygButton((30,480,150,30), "Rage-Quit?")
        #A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
    
    screen.blit(background, (0, 0))
        #Labels For input and output boxes
    screen.blit(Betlabel, (495, 440))
    screen.blit(Pocketlabel, (495, 475))
    screen.blit(Jackpotlabel, (495, 40))
        
        #Displaying the buttons on the screen
    Spinbutton.draw(screen)
    Resetbutton.draw(screen)
    Quitbutton.draw(screen)
        
    screen.blit(imgZomb, (60,170))
        #Second reel
    screen.blit(imgZomb, (245,170))
        #Third reel
    screen.blit(imgZomb, (435,170))
    
    pygame.display.update()
    
        #L - Set up main loop
    while keepGoing:
    
        #T - Timer to set frame rate
        clock.tick(30)
    
        #E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
    
        #R - Refresh display
        
        if 'click' in Resetbutton.handleEvent(event):
            screen.blit(imgZomb, (60,170))
            #Second reel
            screen.blit(imgZomb, (245,170))
            #Third reel
            screen.blit(imgZomb, (435,170))
            pygame.display.update()
        if 'click' in Quitbutton.handleEvent(event):
            pygame.quit()
            sys.exit()
        
        if 'click' in Spinbutton.handleEvent(event):
            
            Player_Money -= Bet
            Jack_Pot += (int(Bet*.15)) # 15% of the player's bet goes to the jackpot
            win = False
            Fruit_Reel = Reels()
            Fruits = Fruit_Reel[0] + " - " + Fruit_Reel[1] + " - " + Fruit_Reel[2]
            reel1 = pygame.image.load(Fruit_Reel[0] + '.png')
            reel2 = pygame.image.load(Fruit_Reel[1] + '.png')
            reel3 = pygame.image.load(Fruit_Reel[2] + '.png')
            
            screen.blit(reel1, (60,170))
        #Second reel
            screen.blit(reel2, (245,170))
        #Third reel
            screen.blit(reel3, (435,170))
            
            pygame.display.update()
            
    
    # Match 3
            if Fruit_Reel.count("Wood") == 3:
                winnings,win = Bet*20,True
            elif Fruit_Reel.count("Redstone") == 3:
                winnings,win = Bet*30,True
            elif Fruit_Reel.count("Quartz") == 3:
                winnings,win = Bet*40,True
            elif Fruit_Reel.count("Iron") == 3:
                winnings,win = Bet*100,True
            elif Fruit_Reel.count("Gold") == 3:
                winnings,win = Bet*200,True
            elif Fruit_Reel.count("Emerald") == 3:
                winnings,win = Bet*300,True
            elif Fruit_Reel.count("Diamond") == 3:
                    print("Lucky Diamonds!!!")
                    winnings,win = Bet*1000,True
    # Match 2
            elif Fruit_Reel.count("Zombie") == 0:
                if Fruit_Reel.count("Wood") == 2:
                    winnings,win = Bet*2,True
                if Fruit_Reel.count("Redstone") == 2:
                    winnings,win = Bet*2,True
                elif Fruit_Reel.count("Quartz") == 2:
                    winnings,win = Bet*3,True
                elif Fruit_Reel.count("Iron") == 2:
                    winnings,win = Bet*4,True
                elif Fruit_Reel.count("Gold") == 2:
                    winnings,win = Bet*5,True
                elif Fruit_Reel.count("Emerald") == 2:
                    winnings,win = Bet*10,True
                elif Fruit_Reel.count("Diamond") == 2:
                    winnings,win = Bet*20,True
    
        # Match Lucky Seven
            elif Fruit_Reel.count("Diamond") == 1:
                winnings, win = Bet*10,True
            
            else:
                winnings, win = Bet*2,True
            if win:    
                print(Fruits + "\n" + "You Won $ " + str(int(winnings)) + " !!! \n")
                Player_Money += int(winnings)
    
        # Jackpot 1 in 450 chance of winning
            jackpot_try = random.randrange(1,51,1)
            jackpot_win = random.randrange(1,51,1)
            if  jackpot_try  == jackpot_win:
                print ("You Won The Jackpot !!!\nHere is your $ " + str(Jack_Pot) + "prize! \n")
                Jack_Pot = 500
            elif jackpot_try != jackpot_win:
                print ("You did not win the Jackpot this time. \nPlease try again ! \n")
    # No win
            else:
                print(Fruits + "\nPlease try again. \n")

        

        
    pygame.display.flip()

if __name__ == "__main__": main()