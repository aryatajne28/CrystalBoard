# My experience with making of the CrystalBoard.

## Assembly
First let's go through the assembly and making of CrystalBoard
- I had cut the acrylic sheets from my school's laser cutter.
- So, I layed out some of the switches onto the acrylic plate to check whether it cutouts match with the PCB or not.

| ![First try on switches](take-two/images/1.jpeg) | ![Second pic of switches](take-two/images/2.jpeg) | ![Second try on switches](take-two/images/3.jpeg)|
| - | - | -| 

- Since they were matching, I went ahead and soldered the Pi Pico to my PCB and screwed in the stablizers.

|![Soldering pi](take-two/images/5.jpeg) | ![Soldering pi](take-two/images/4.jpeg) |
| - | - |

- Thus, the next step I did was to solder all the switches and rest of the components in the back of the PCB!

|![](take-two/images/6.jpeg) | ![](take-two/images/7.jpeg) |
| - | - |

- After this, I was about to solder my Neopixels, then I noticed that the pins are not matching. I quickly opened my Kicad file and checked and whoosh! I used the wrong footprint :)
- Thus, I was left with no choice but to assemble without them! And after assembling all the rest of the sheets and keycaps, we have our Crystalboard:

|![](take-two/images/8.jpeg) |![](take-two/images/9.jpeg) |
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
