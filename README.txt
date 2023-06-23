Hey, it's Kieran
Just wanted to give you a quick summary of what I've done

Colour Adjuster Tool (CAT):

This tool modifies the colour of each icon in a folder (and all subfolders)

To use it, call it on the command line as follows

ColourAdjusterTool.exe folder colour

Where 'folder' is the filepath to the top level directory containing all the icons you want to edit
and 'colour' is the new colour you want the icons to be, in hex code

For example, if you want to change all the icons in the folder 'ios' to green, you would do:

ColourAdjusterTool.exe ios 00ff00

This will create a new folder at the same level as the target folder with the hex code appended to it's name
This folder will contain a copy of the target folder but with all icons changed to match the target colour


This tools works by cutting the icon image into 4, and solely operating on the first and third images, counting from the top
It sets the colour of these parts of the image to the desired colour and then puts the full image back together and saves it in the new folder
This works because (most of) your icons use transparency for anti-aliasing, which allows me to just set the entire image as a single colour

There were a couple icons that did not use transparency for anti-aliasing, they used colours that faded to white instead
This is fine as long as they are always on a white background, but meant that my program would make them look terrible
So I wrote a short script to change them to use transparency instead, I ended up editing three of your icons to work this way so that they would work with the colour changing program
And as a bonus, they will now look good on any background colour as well. I have put the icons in the ios folder here, but also put the images at the top level.
Also, with Joe's permission, I redid the setpop icon to make it simpler, as that was an easier option than editing the current icon to work with my program.

Finally, I have bundled the python script into an executable that should include anything needed to run it, but I've also included the python script should you want to look at it for any reason