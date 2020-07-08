
# OCR Statistics Recorder
This project is intended for people who play Riot Games' tactical shooter, Valorant. The program records the user's score when practicing in the "Shooting Range" to keep track of the user's overall improvement in the Range.
## Background
![Valorant Shooting Range](https://i.ytimg.com/vi/Wee8N6sOlWQ/maxresdefault.jpg)

As the user shoots more robots in the Shooting Range, the score in the center-top of the screen increases. The score is recorded and saved into a file to track the user's overall improvement. <
## Installation
WIP; program only works for the developer.
## Concepts Used
* optical character recognition ([OCR](https://en.wikipedia.org/wiki/Optical_character_recognition))
* HSV color detection
## Version History
The project went through different versions based on the how accurate the program would read the user's score in the Practice Range.
### v1

![Screenshot of Scoreboard](images/scoreboard.png)

Initially took a screenshot of the region where the scoreboard _should_ be. This method was unreliable since the region might depend on the size of the user's screen. Also, the user would have to aim at a specific point in order for the image to be detected.
### v2

Used HSV color detection to find the largest contour of a certain color. In this case, the HSV algorithms were tuned to search for a color similar to the scoreboard (brownish-gray), and the largest contour that appeared was the scoreboard. 

![Scoreboard with HSV](images/hsv_color_detection_example.PNG)

Using the color detection to create a bounding box, a more specific screenshot of the scoreboard could be captured. This method proved to be much more reliable than depending on a screenshot of a region. However, the user would have to use the same (or similar) display settings as the developer. For example, using a colorblind mode might change the shade or intensity of the scoreboard's color, which would lead to an inaccurate screenshot of the scoreboard.
## Future Plans
* Improve accuracy of reading the scoreboard. 
* Add customized options for the program to work with the user's display settings (i.e. colorblind options).
* Track overshooting/undershooting when aiming at the bots; could help users improve their aim.
* Webpage to create a leaderboard among the Valorant community.




