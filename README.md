# CSE4360-Projects

This repository contains the directories for the projects done by Michael Bonnet, Allison Gardiner, and Noah Walker for CSE 4360 Autonomous Robots, taught by Dr. Mangred Huber in the Fall 2021 semester at the University of Texas at Arlington.

`Project_1`
---

**Project_1** is the directory for our first project. We were tasked to design and program a LEGO EV3 robot to navigate a maze where the starting position, goal position, and obstacle (aka wall) positions were known. We were allowed to choose our orientation. However, once programming in these positions, the robot had to plan a path and execute it autonomously. See the specification document, `Project_1/proj1.pdf`, for more information.

We used A* search with a Manhattan Distance heuristic to build this path, then used the ordered position list to generate movement commands. See our report, `Project_1/CSE 4360 Team 6 Project 1 Report.pdf`, for more information.

`Project_2`
---

**Project_2** is the directory for our second project. We were tasked to design and program a LEGO EV3 robot to navigate a maze with the goal of finding an upright object somewhere in the maze, then moving that object 12 inches away from the position it was found in. However, unlike in our first project, none of the starting position, starting orientation, goal position, or obstacle positions were known, and our robot's actions were to be purely behavior-based, and again had to execute all its movements and actions autonomously. See the specification document, `Project_2/proj2.pdf`, for more information.

Our robot possessed two sensors: a color sensor, and an ultrasonic sensor. 

* The color sensor was mounted to the forward left corner of the robot, and was used to detect whether a wall, marked with blue painter's tape, had been encountered.
* The ultrasonic sensor was mounted to the lower front of the robot pointing directly forward, and was used to detect whether an object was within 13 inches of the sensor.
  * We set 13 inches as the detection range because the ultrasonic sensor was imprecise. Adding the extra inch of range ensured we would detect the object if it were within 12 inches.

We implemented three main behaviors:

* `wander()`, which led the robot in an expanding clockwise spiral centered on its initial position.
  * If a wall was encountered while within `wander()`, the robot would enter `follow_wall()` mode.
  * If an object was detected while within `wander()`, the robot would enter `clear()` mode.
  * If the spiral got too large, it would move straight forward for two seconds before beginning another spiral, in the hopes of either detecting an object or hitting a wall.
* `follow_wall()`, which had the robot follow blue-painter's-tape-on-the-ground "walls" for 80 seconds before ree
  * If an object was detected while within follow_wall(), the robot would enter clear() mode.
  * If an instance of `follow_wall()` behavior lasts 80 seconds, the robot would reenter `wander()` mode.
* `clear()`, which is entered upon object detection within 13 inches, and causes the robot to charge forward for 2 feet or until it encounters a wall, whichever happens first.
  * If the robot encounters a wall within clear(), it enters follow_wall() mode in an effort to get around the wall and at the goal.

For further information, see our report, `Project_2/CSE 4360 Team 6 Project 2 Report.pdf`, for more information.
