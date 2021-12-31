# CSE4360-Projects

This repository contains the directories for the projects done by Michael Bonnet, Allison Gardiner, and Noah Walker for CSE 4360 Autonomous Robots, taught by Dr. Mangred Huber in the Fall 2021 semester at the University of Texas at Arlington.

`Project_1`
---

**Project_1** is the directory for our first project. We were tasked to design and program a LEGO EV3 robot to navigate a maze where the starting position, goal position, and obstacle (aka wall) positions were known. We were allowed to choose our orientation. However, once programming in these positions, the robot had to plan a path and execute it autonomously. See the specification document, `Project_1/proj1.pdf`, for more information.

We used A* search with a Manhattan Distance heuristic to build this path, then used the ordered position list to generate movement commands, pseudo-integrating it once for position change and again for heading change. 

See our report, `Project_1/CSE 4360 Team 6 Project 1 Report.pdf`, for more information.

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

For more information, see our report, `Project_2/CSE 4360 Team 6 Project 2 Report.pdf`.

`Project_3`
---

**Project_3** is the directory for our second project. When our team received the specification document for Project 3 including several suggested projects, we did not find any of them to be quite to our liking, and so began brainstorming what we’d propose instead. Eventually, we settled on proposing that we design and implement Braitenberg vehicles, simple robots that directly map sensor readings to actuators in ways that create different behaviors based on whether the robots accelerate or decelerate towards signals, and turn towards or away from signals. Combinations of these two criterions’ two variations result in four behaviors:

* **“Fear”**, where the robot will turn away from signal and accelerate the closer it is to the
signal, aiming to come to a stop when it has turned fully away from the signal and no
longer detects it, as if it “fears” the signal.
* **“Aggression”**, where the robot will turn toward the signal and accelerate the closer it is to
the signal, as if it were trying to “attack” the signal.
* **“Love”**, where the robot will turn toward the signal and decelerate the closer it is to the
signal, as if it “loved” the signal and wished to be peacefully near to it and face it.
* **“Explore”**, where the robot will turn away from the signal and decelerate the closer it is to
the signal, as if it were “exploring” the world and wished to observe signals then seek
new ones.

Our proposal was approved, and we got to work. Challenges included:

* Creating a signal source that would give both our distance (ultrasonic) and direction (infrared seeker) sensors actionable data, given that no sensor available to us could sense both distance and direction
* Fusing the data from the two sensors to inform heading and velocity changes
* Solving a problem where the infrared seekers that were included in our EV3 kits could not be automatically detected and used by the EV3, requiring us to implement a direct, bare-metal I2C solution to be able to use them
* Signal source development having to be done blindly in parallel to infrared seeker solution engineering, resulting in limited time to make the needed design adjustments made apparent once the infrared seeker was functioning  

For more information, see our report, `Project_3/CSE 4360 Team 6 Project 3 Report.pdf`.
