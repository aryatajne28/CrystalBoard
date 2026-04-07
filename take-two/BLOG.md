# My experience with making of the CrystalBoard.

## Assembly
First let's go through the assembly and making of CrystalBoard
- I had cut the acrylic sheets from my school's laser cutter.
- So, I layed out some of the switches onto the acrylic plate to check whether it cutouts match with the PCB or not.

| ![1](https://github.com/user-attachments/assets/63749808-b1a0-4506-89df-9f679dc84c96)  | ![2](https://github.com/user-attachments/assets/52622937-f10e-45d7-9a5e-17b42ef4cf46) | ![3](https://github.com/user-attachments/assets/8b1b3185-37f8-4817-93d8-492f8cab5b33)|
| - | - | -| 

- Since they were matching, I went ahead and soldered the Pi Pico to my PCB and screwed in the stablizers.

|![5](https://github.com/user-attachments/assets/538a2af9-13b0-42f7-b0dc-68827fb76d3d)  | ![4](https://github.com/user-attachments/assets/fdd7876e-ab11-4ae2-81ed-b740223be389)  |
| - | - |

- Thus, the next step I did was to solder all the switches and rest of the components in the back of the PCB!

|![6](https://github.com/user-attachments/assets/7a75ab59-9fc1-4524-a753-cc20f5eae6cb)| ![7](https://github.com/user-attachments/assets/33941d69-6d51-46ab-82ac-5b94d75395a0) |
| - | - |

- After this, I was about to solder my Neopixels, then I noticed that the pins are not matching. I quickly opened my Kicad file and checked and whoosh! I used the wrong footprint :)
- Thus, I was left with no choice but to assemble without them! And after assembling all the rest of the sheets and keycaps, we have our Crystalboard:

|![8](https://github.com/user-attachments/assets/42766c2d-90a2-4a38-aeb8-f04625ae2521)  |![9](https://github.com/user-attachments/assets/32be2cf8-91de-4820-a564-e9cb713e86ae)  |
| -|-|

## Firmware
I used QMK for this, since I consider it to be a very standard firmware for it's features like: the keyboard isn't detected as a new USB device everytime we plug it in
and direct build loading onto our MCU!

## Why this project didn't work?
- Used wrong footprint for Neopixels (sk6812mini instead of sk6812mini-e).
- I didn't calculate the placement of Micro-USB port of Pico, and due to which, the USB-port broke-off from the pico after short usage while flashing the firmware!
- I didn't have tolerances for screws holes I made in acrylic sheet, due to which the screws didn't go through, I had to use glue temporarily.

## My two cents for anyone designing a keyboard!
- Maybe try to design a hotswappable design. Because for soldering the switches, you have to first insert the switches through the plate that you will design. So if you want to desolder even one switch, that will become a nightmare!
- Focus very much on the CAD of case design, cause even a slight mis-alignment won't let your PCB fit in!

Demo link: https://youtu.be/TqwXyUNoaCY
P.S. there's nothing much in there cause currently the keyboard is not working!
