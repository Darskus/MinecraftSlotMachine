'''
Created on 2013-06-06

@author: Emilio Tunno
Version: 1.0 Gui only no functionality yet
'''
import pygame
import pygbutton

imgZomb = pygame.image.load('Zombie.png')
imgDia = pygame.image.load('Diamond.png')
imgGold = pygame.image.load('Gold.png')
imgIron = pygame.image.load('Iron.png')
imgRedstone = pygame.image.load('Redstone.png')
imgQuartz = pygame.image.load('Quartz.png')
imgWood = pygame.image.load('Wood.png')
imgEmerald = pygame.image.load('Emerald.png')


def main():
    pygame.init()
    
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
    
        #L - Set up main loop
    while keepGoing:
    
        #T - Timer to set frame rate
        clock.tick(30)
    
        #E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
    
        #R - Refresh display
        screen.blit(background, (0, 0))
        #Labels For input and output boxes
        screen.blit(Betlabel, (495, 440))
        screen.blit(Pocketlabel, (495, 475))
        screen.blit(Jackpotlabel, (495, 40))
        
        #Displaying the buttons on the screen
        Spinbutton.draw(screen)
        Resetbutton.draw(screen)
        Quitbutton.draw(screen)
        
        #First reel
        screen.blit(imgZomb, (60,170))
        #Second reel
        screen.blit(imgZomb, (245,170))
        #Third reel
        screen.blit(imgZomb, (435,170))
        
        
        pygame.display.flip()
if __name__ == "__main__": main()