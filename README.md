# Graded-Unit RFID Robotic Arm Project

This project was completed as part of my HND Mechatronics Graded Unit.  The client required a robotic arm to pick up, identify and sort items based on RFID codes.

Images of the completed system can be found [here](https://github.com/GRitchie1/RFIDRoboticArm-HNDGradedUnit/tree/main/Images).

All of the models used can be found [here](https://github.com/GRitchie1/Graded-Unit/tree/main/Models), and are 3D printable.

The code was written as part of the project and utilises CircuitPython due to the vast number of libraries.

This repository will be updated with parts lists and instructions.

## Parts List
This project requires access to a 3D printer to manufacture the robot arm.  All of the [models](https://github.com/GRitchie1/Graded-Unit/tree/main/Models) can be 3D printed using PLA.

The required quantities of 3D printed parts are shown in the table below.

| Model | QTY |
|-------|-----|
| Base Mount | 1 |
| Driver Gear | 1 |
| Geared Base Bottom | 1 |
| Geared Base Top | 1 |
| Item to Pickup | 3 |
| Linkage 1 & 2 | 2 |
| Linkage 3 | 1 |
| Motor Mount | 1 |

The required quantities of components and other parts are shown below.

| Part | QTY |
|------|-----|
| Pi Pico | 1 |
| Micro Servo (SG92R) | 5 |
| Momentary Push button | 2 |
| RFID Scanner (RC522) | 1 |
| Power supply (5V 3A) | 1 |
| Breadboard friendly power jack | 1 |
| Servo driver (PCA9685) | 1 |
| Skateboard bearing | 2 |
| M8 Bolt | 1 |
| M3 * 12 Countersunk screws | 9 |

## Wiring Diagrams
The wiring diagrams for this project were designed using Fritsing.

![Full Wiring Diagram_bb](https://user-images.githubusercontent.com/55364420/171039927-9715cc31-7c0a-4324-ab6b-2bb0fb3534cc.jpg)


## Assembly
To assemble the robotic arm, first ensure that you have got all of the required [parts](#Parts-List).

Next use the following steps to assemble the arm:
1. Insert the bearing into the Base (Top) piece. 
2. Insert the bearing into the Base (Bottom) piece.
3. Place the Top and Bottom pieces of the base together and insert the screws to keep them attached.
4. Insert the M8 bolt into the Mount piece.
5. Attach the mount piece to a piece of support material (such as a plank of wood)
6. Assemble the rest of the robot arm using servo motors and linkage pieces.
7. Place the Robot arm onto the M8 bolt.
8. Attach the driver gear to the servo motor.
9. Mount the servo motor to the support material using the motor mount piece at a suitable distance to allow the gears to interlink.
