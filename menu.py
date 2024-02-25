# display

# author: Colin Maggard

import pygame, sys

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Initializations
multiplier = 2 # controls size of windows
pygame.init() # initialize pygame
screen = pygame.display.set_mode((480 * multiplier, 270 * multiplier))
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 24 * multiplier)
hudfont = pygame.font.SysFont(None, 18 * multiplier)

# Game state variables
gamerun = True
activity = "Menu"
selection = 0
infoprompts = ["Please enter your full name:", "Please enter your city:",
               "Please enter your state abbreviation (e.g. WI):",
               "Please enter your email:","Please enter your phone number"]
infoanswers = []
gatherLinks = False
links = ""
linkprompts = ["How many links would you like to include any links in your resume header?", "Please enter an integer."]
link_index = 1
objective_statement = ""
i = 0
inputstring = ""
character_amount = 0

def render_menu(selection):
    screen.fill(BLACK)  # clear screen
    title = font.render("Resume Enhancer", True, WHITE)
    screen.blit(title, (180 * multiplier, 5 * multiplier))

    # Menu options
    menu0_color = RED if selection == 0 else WHITE
    menu1_color = RED if selection == 1 else WHITE

    menu0 = hudfont.render("Create Resume", True, menu0_color)
    menu1 = hudfont.render("Quit", True, menu1_color)

    screen.blit(menu0, (50 * multiplier, 50 * multiplier))
    screen.blit(menu1, (50 * multiplier, 100 * multiplier))

def render_information(prompt, inputstring, character_amount):
    screen.fill(BLACK)  # clear screen
    prompt_text = font.render(prompt, True, WHITE)
    screen.blit(prompt_text, (20, 20))

    inputfont = pygame.font.SysFont(None, 24 * multiplier)
    inputDisp = inputfont.render(inputstring, True, WHITE)
    screen.blit(inputDisp, (20, 60))

while gamerun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if activity == "Menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selection = max(0, selection - 1)
                elif event.key == pygame.K_DOWN:
                    selection = min(1, selection + 1)
                elif event.key == pygame.K_SPACE:
                    if selection == 0:
                        activity = "Information"
                        i = 0
                    else:
                        pygame.quit()
                        sys.exit()

        elif activity == "Information":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and character_amount > 0:
                    inputstring = inputstring[:-1]
                    character_amount -= 1
                elif event.key == pygame.K_RETURN:
                    infoanswers.append(inputstring)
                    inputstring = ""
                    character_amount = 0
                    i += 1
                    if i >= len(infoprompts):
                        activity = "Menu"
                    else:
                        activity = "LinkMenu"
                elif character_amount < 24 and event.unicode.isprintable():
                    inputstring += event.unicode
                    character_amount += 1

        elif activity == "LinkMenu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and character_amount > 0:
                    inputstring = inputstring[:-1]
                    character_amount -= 1
                elif event.key == pygame.K_RETURN:
                    # count number of links
                    if (not int(inputstring)):
                        i = 1
                        break
                    if int(inputstring) > 0:
                       gatherLinks == True
                       linkCount = inputstring
                       activity = "GatherLinks"
                    else:
                        activity = "ObjectiveMenu"
                elif character_amount < 24 and event.unicode.isprintable():
                    inputstring += event.unicode
                    character_amount += 1
        
        elif activity == "GatherLinks":
            while (link_index < linkCount)
                links = links + link
                if (i != linkscnt):
                    links += ","

        elif activity == "ObjectiveMenu":
            pass

        elif activity == "GatherObjective":
            pass

    if activity == "Menu":
        render_menu(selection)
    elif activity == "Information" and i < len(infoprompts):
        render_information(infoprompts[i], inputstring, character_amount)
    elif activity == "LinkMenu":
        render_information(linkprompts[i], inputstring, character_amount)
    elif activity == "GatherLinks":
        render_information("Please provide link #{link_index}: ", inputstring, character_amount)

    pygame.display.update()
    clock.tick(60)