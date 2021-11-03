# Authors : Michael Bonnet
#           Allison Gardiner
#           Noah Walker
# Class   : CSE 4360-001 Autonomous Robots @ UT Arlington
#           Taught by Dr. Manfred Huber in Fall 2021
# Project : Project 1

# Due Date           : 11/3/2021 @ 11:59 PM
# Submission Date    : TBD
# Demonstration Date : 11/3/2021 @ 7:15 PM
# Grade Received     : TBD

#############################################
### OPTIONAL PRINTING/DEBUGGING FUNCTIONS ###
#############################################

# prints to console each instruction in list of instructions
# does not return anything
def print_instructions(instructions):
    for i in range(len(instructions)):
        if instructions[i] == 1:
            instruction_text = "go    forward"
        elif instructions[i] == 2:
            instruction_text = "go    backward"
        elif instructions[i] == 3:
            instruction_text = "turn  left"
        elif instructions[i] == 4:
            instruction_text = "turn  right"

        print("Instruction " + str(i) + ":\t" + str(instructions[i]) + " ("+str(instruction_text)+")")


# prints out where heading changes are found in the step transitions list
# does not return anything
def heading_change_detection(step_transitions, found_path, robot_heading):
    # for n steps there are n-1 step transitions, so only iterate that far
    for i in range(len(found_path)-1):
        x_change  = step_transitions[i][0] - step_transitions[i-1][0] # get change in X between steps
        y_change  = step_transitions[i][1] - step_transitions[i-1][1] # get change in Y between steps

        # if there is indeed a heading change, 
        if x_change != step_transitions[i-1][0] and y_change != step_transitions[i-1][1] and i>0:
            print("changing heading between step "+str(i-1)+"and "+str(i))
            # change heading accordingly, and
            if y_change == 1:
                if robot_heading != 4:
                    robot_heading -= 1
                else:
                    robot_heading = 1
            elif y_change == -1:
                if robot_heading != 1:
                    robot_heading += 1
                else:
                    robot_heading = 4
            elif x_change == 1:
                if robot_heading != 1:
                    robot_heading -= 1
                else:
                    robot_heading = 4
            elif x_change == -1:
                if robot_heading != 4:
                    robot_heading += 1
                else:
                    robot_heading = 1
            
            # print a notification of the detected heading change
            orientation = 0
            if robot_heading == 1:
                orientation = "North"
            elif robot_heading == 2:
                orientation = "East"
            elif robot_heading == 3:
                orientation = "South"
            elif robot_heading == 4:
                orientation = "West"
            print("heading change detected for step "+str(i)+"\t->\tstep "+str(i+1)+"! \theading "+orientation)