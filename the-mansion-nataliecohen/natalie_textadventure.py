#start point
print("You enter a seemingly empty mansion. The door closes behind you with a quiet click.")
while True:
    while True:
        try:
            ans1 = int(input("You can: (1)Jiggle the front doorknob (2)Take the door directly to your right (3)Move forward down the hallway"))
            break
        except ValueError:
            print("Error. Enter one of the number choices provided.")
            continue
            break
    #branch 1 - end
    if ans1 == 1:
        print("The knob doesn't give when you try it. You look up in frustration, your eyes widening as you realize the chandelier has somehow come loose from the ceiling. You feel blinding pain, and then nothing.")
        exitonclick()
    #branch 2
    elif ans1 == 2:
        print("You are now in a very small hallway. The dust that has gathered suggests no one has been there in a very long time.")
        while True:
            while True:
                try:
                    ans2 = int(input("You can: (1)Take the door slightly to the left, just up ahead (2)Move up the stairs"))
                    break
                except ValueError:
                    print("Error. Enter one of the number choices provided.")
                    continue
                    break
                    #branch 2-1 - end
                    if ans2 == 1:
                        print("You move through the doorway, and see steps directly in front of you. You clumsily navigate the dark stairway. The door swings shut behind you. You bang on it, but there is no way out. The precious few days you have left to live are painful and delirious due to hunger and dehydration.")
                        exitonclick()
                        #branch 2-2 - end
                    elif ans2 == 2:
                        print("As you walk up the stairs, you hear a sharp crack, and the floorboard collapses beneath you. The splinters of the wood pierce your skin and you see a wooden block hit your chest.")
                        exitonclick()
                    else:
                        print("Error. Enter one of the number choices provided.")
                        continue
    #branch 3
    elif ans1 == 3:
        print("You enter a hallway filled with paintings. There's just something not quite right about the faces in them though.")
        while True:
            try:
                ans3 = int(input("You can: (1)Enter the larger hall up ahead (2)Climb the steep stairwell (3)Take the door on your right"))
                break
            except ValueError:
                print("Error. Enter one of the number choices provided.")
                continue
                break
        #branch 3-1
        if ans3 == 1:
            print("The hall is blank, with no life or color.")
            while True:
                while True:
                    try:
                        ans4 = int(input("You can: (1)Enter the open doorway just ahead (2)Enter the slightly ajar doorway to your left"))
                        break
                    except ValueError:
                        print("Error. Enter one of the number choices provided.")
                        continue
                        break
                        #branch 3-1-1 - end
                if ans4 == 1:
                    print("You flick the lightswitch as you walk slowly into the room. It seems to be a small kitchen with fresh food despite what layers of dust might suggest. Suddenly, you feel a sharp pain, and feel warm liquid rise to your mouth. You cast your eyes downward, unable to move your head. The tip of a sharp knife sticks out of your chest.")
                    exitonclick()
                #branch 3-1-2 - end
                elif ans4 == 2:
                    print("The door creaks open to show a beautiful, lush garden full of huge plants that you do not recognize. You feel something by your feet, but when you attempt to kick out you find your feet are bound by something. You look down and see vines curled around your legs, trapping you like a fly in a spider's web. You look forward again, and are met by the gaping maw of what looked to be an enormous venus flytrap.")
                    exitonclick()
                else:
                    print("Error. Enter one of the number choices provided.")
                    continue
        #branch 3-2
        elif ans3 == 2:
            print("You walk up the stairs, wondering just how many stories there were in this place.")
            while True:
                while True:
                    try:
                        ans5 = int(input("You can: (1)Take the door on your right (2)Take the door on your left"))
                        break
                    except ValueError:
                        print("Error. Enter one of the number choices provided.")
                        continue
                        break
                #branch 3-2-1 - end
                if ans5 == 1:
                    print("The door leads to a room empty of anything except an elaborate window. You open the window and cautiously climb out in an attempt to scale the wall. It appears to be going well, until your foot slips. You feel a moment of pure panic, and then pain.")
                    exitonclick()
                #branch 3-2-2 - end
                elif ans5 == 2:
                    print("The door closes behind you, revealing a well-stocked bathroom. You admire the beautiful tiling for a moment, before you hear the distinctive sound of glass shattering. You look toward the noise, only to be met with a huge wave of water.")
                    exitonclick()
                else:
                    print("Error. Enter one of the number choices provided.")
                    continue
        #branch 3-3 - end
        elif ans3 == 3:
            print("A sharp, acrid scent reaches your nose as the door closes behind you. You squint up ahead, wondering what the flickering light is. Walking forward, you quickly realize fire is eating through the hall you're in at an incredible rate. You run towards the door you came from, pounding on it and trying to force it open as the fire comes up behind you and consumes your existence.")
            exitonclick()
        else:
            print("Error. Enter one of the number choices provided.")
            continue
    else:
        print("Error. Enter one of the number choices provided.")
        continue
