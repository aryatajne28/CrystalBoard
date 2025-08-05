# Journal for CrystalBoard


- Date 26/07/25 - Total Time Spent: 0.5 hours
    - Idea: Make a custom mechanical keyboard with case made up of clear acrylic sheets stacked on top of each other, thus the name crystal board!
    - Work done - Finalised the layout, took it from keyboard-layout-editor.com and drawn all the rows and columns on that layout!
    ![Keyboard Layout](<./images/keyboard layout.png>)
    - Setup Kicad with all the libraries and footprints.
    - Time Spent - 30 mins
    
- Date 27/07/25 - Total Time Spent: 4.5 hours
    - I made the complete schematic made the PCB layout but then I noticed that there is no space for Pi Pico. So I deleted the top right 3 keys, thus I had to do changes in the Kicad Schematic and PCB. Thus took some time but I am done with PCB routing. Now I am thinking to add some neopixels and some silkscreen to the PCB.
    - The updated keyboard layout looks like this now:
    ![Keyboard Layout Updated](<./images/Keyboard Layout Updated.png>)
    - Kicad Schematic and PCB:
    ![Kicad Schematic](./images/kicad-schematic-1.png)
    ![Kicad PCB](./images/kicad-pcb-1.png)
    - Things to do next - Put some Neopixels, Stabilizers, Plate, Silkscreen
    - Time Spent today till now - 3 hours

- Date 27/07/25 (Update 2)
    - Done with the Neopixels, I did not add per key LED but a bar on top and on WASD keys (not for gaming obviously :O)
    ![alt text](./images/kicad-pcb-2.png)
    - Time Spent - 1.5 hours

- Date 28/07/25 - Total Time Spent: 1.5 hours
    - Done with Silkscreen and Stablizers.
    - It was pain to convert the images into B&W vectors.
    - PCB Looks like this now:
    ![alt text](./images/silkscreen.png)
    - Time spent - 1.5 hours

- Date 31/07/25 - Total Time Spent: 5 hours
    - Speedrunning the Case and Code File!
    - Case I have designed as layers since I will be laser cutting the acrylic sheets.
    - For illustration purposes I have just reduced the opacity of the components in Autocad to make it look like Acrylic, but in real life it will look really good!
    ![alt text](<./images/Full-Keyboard v1.png>)
    - Time spent - 3 hours

    - Finalized the repo and collected resources for all the BOM.
    - Time Spent - 2 hours

- Date 03/08/25 - Total Time Spent: 2 hours
    - According to the changes suggested by @Kai Pereira(Slack) I have now added per key RGB Neopixel!
    - So I deleted all the tracks because it was a lot of hassle to shift everything and again route.
    - Added 83x Neopixels and 83x 0805 Capacitors in the schematic and now searching for good site to order from, because ordering to India is a hassle
    - New Schematic and PCB photo:
    ![alt text](./images/kicad-schematic-neopixel.png)
    ![alt text](./images/kicad-pcb-neopixel.png)
    - Todo: Code change and Update BOM
    - Time Spent - 2 hours

- Date 06/08/25 - Total Time Spent: 0.5 hours
    - I have added the updated items in my BOM and updated the code a bit.
    - Refinded the README.md file.
    - Another Update, I uploaded the new Kicad Project files and the production .zip folder for the same.
    - Time Spent - 0.5 hours