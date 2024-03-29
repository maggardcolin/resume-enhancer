# author: Colin Maggard

import pygame, sys
from resume import Resume

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
               "Please enter your email:", "Please enter your phone number"]
infoanswers = []
gatherLinks = False
links = []
linkprompts = ["Number of links in resume header? (Enter an integer)"]
link_index = 0
linkCount = 0
objective_statement = ""
i = 0
inputstring = ""
character_amount = 0

def render_menu(selection):
    if activity == "Menu":
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
    elif activity == "MainMenu":
        screen.fill(BLACK)  # clear screen
        title = font.render("Add Resume Fields", True, WHITE)
        screen.blit(title, (180 * multiplier, 5 * multiplier))

        # Menu options
        menu1_color = RED if selection == 1 else WHITE
        menu2_color = RED if selection == 2 else WHITE
        menu3_color = RED if selection == 3 else WHITE
        menu4_color = RED if selection == 4 else WHITE
        menu5_color = RED if selection == 5 else WHITE
        menu6_color = RED if selection == 6 else WHITE
        menu7_color = RED if selection == 7 else WHITE

        menu1 = hudfont.render("Add Education", True, menu1_color)
        menu2 = hudfont.render("Add Experience", True, menu2_color)
        menu3 = hudfont.render("Add Activity", True, menu3_color)
        menu4 = hudfont.render("Add Project", True, menu4_color)
        menu5 = hudfont.render("Add Skills", True, menu5_color)
        menu6 = hudfont.render("Finish and Export Resume", True, menu6_color)
        menu7 = hudfont.render("Quit App", True, menu7_color)

        screen.blit(menu1, (50 * multiplier, 1 * 25 * multiplier))
        screen.blit(menu2, (50 * multiplier, 2 * 25 * multiplier))
        screen.blit(menu3, (50 * multiplier, 3 * 25 * multiplier))
        screen.blit(menu4, (50 * multiplier, 4 * 25 * multiplier))
        screen.blit(menu5, (50 * multiplier, 5 * 25 * multiplier))
        screen.blit(menu6, (50 * multiplier, 6 * 25 * multiplier))
        screen.blit(menu7, (50 * multiplier, 7 * 25 * multiplier))

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
                        activity = "LinkMenu"
                        i = 0
                    else:
                        activity = "Information"
                elif character_amount < 24 and event.unicode.isprintable():
                    inputstring += event.unicode
                    character_amount += 1

        elif activity == "LinkMenu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and character_amount > 0:
                    inputstring = inputstring[:-1]
                    character_amount -= 1
                elif event.key == pygame.K_RETURN:
                    if inputstring.isdigit():
                        linkCount = int(inputstring)
                        if linkCount > 0:
                            gatherLinks = True
                            activity = "GatherLinks"
                            inputstring = ""
                            character_amount = 0
                        else:
                            inputstring = ""
                            activity = "ObjectiveMenu"
                    else:
                        print("Please enter a valid integer.")
                elif character_amount < 24 and event.unicode.isprintable():
                    inputstring += event.unicode
                    character_amount += 1

        elif activity == "GatherLinks":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and character_amount > 0:
                    inputstring = inputstring[:-1]
                    character_amount -= 1
                elif event.key == pygame.K_RETURN:
                    links.append(inputstring)
                    inputstring = "" 
                    character_amount = 0
                    link_index += 1
                    if link_index >= linkCount:
                        activity = "ObjectiveMenu"
                elif character_amount < 24 and event.unicode.isprintable():
                    inputstring += event.unicode
                    character_amount += 1

        elif activity == "ObjectiveMenu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and character_amount > 0:
                    inputstring = inputstring[:-1]
                    character_amount -= 1
                elif event.key == pygame.K_RETURN:
                    linkCount = inputstring
                    if inputstring == 'y':
                        inputstring = ""
                        activity = "GatherObjective"
                    else:
                        inputstring = ""
                        activity = "ObjectiveMenu"
                elif character_amount < 24 and event.unicode.isprintable():
                    inputstring += event.unicode
                    character_amount += 1

        elif activity == "GatherObjective":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and character_amount > 0:
                    inputstring = inputstring[:-1]
                    character_amount -= 1
                elif event.key == pygame.K_RETURN:
                    my_resume = Resume(infoanswers[0], infoanswers[1], infoanswers[2], 
                               infoanswers[3], infoanswers[4], objective_statement, links)
                    selection = 1
                    inputstring = ""
                    activity = "MainMenu"
                elif character_amount < 24 and event.unicode.isprintable():
                    inputstring += event.unicode
                    character_amount += 1

        elif activity == "MainMenu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selection = max(1, selection - 1)
                elif event.key == pygame.K_DOWN:
                    selection = min(7, selection + 1)
                elif event.key == pygame.K_SPACE:
                    if selection == 1:
                        activity = "Education"
                        i = 0
                    if selection == 2:
                        activity = "Information"
                        i = 0
                    if selection == 3:
                        activity = "Information"
                        i = 0
                    if selection == 4:
                        activity = "Information"
                        i = 0
                    if selection == 5:
                        activity = "Information"
                        i = 0
                    if selection == 6:
                        activity = "Information"
                        i = 0
                    else:
                        pygame.quit()
                        sys.exit()

    if activity == "Menu":
        render_menu(selection)
    elif activity == "Information":
        render_information(infoprompts[i], inputstring, character_amount)
    elif activity == "LinkMenu":
        render_information(linkprompts[0], inputstring, character_amount)
    elif activity == "GatherLinks":
        render_information(f"Please provide link #{link_index + 1}: ", inputstring, character_amount)
    elif activity == "ObjectiveMenu":
        render_information("Include an objective statement? (y/n)", inputstring, character_amount)
    elif activity == "GatherObjective":
        render_information("Please input your objective statement.", inputstring, character_amount)
    elif activity == "MainMenu":
        render_menu(selection)

    pygame.display.update()
    clock.tick(60)