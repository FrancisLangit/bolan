![banner](https://i.imgur.com/hrYppaa.png)

Bolan.py is a clone of Google Chrome's well-known [Dinosaur Game](https://en.wikipedia.org/wiki/Dinosaur_Game) written on Python 3 using the [Pygame](https://www.pygame.org/wiki/about) game development framework. 

## Background

### Gameplay

The player takes control of a T-Rex running across an infinite desert. The main objective is for the player to keep themselves alive as long as possible by pressing the space key to avoid the Cacti and Pterodactyls that come their way. Points are continually scored until the player collides with an obstacle, upon which the game ends and they may restart the game to attain a higher score. 

**Note**: *Pterodactyls only start spawning at 350 points.*

![readme_gif.gif](https://i.imgur.com/rXhqaCg.gif)

### Controls

| Key          | Usage                                        |
| ------------ | -------------------------------------------- |
| Enter        | Starts the gameplay once the program is run. |
| Q and ESC    | Either can be pressed to close the program.  |
| Space and UP | Either makes the player jump.                |
| DOWN         | Makes the player duck.                       |

### Why did you name it "Bolan.py?"

Inspiration was taken from Google's development of the original Chrome game. Before the browser game was released, [Google gave the project the codename "Project Bolan,"](https://thenextweb.com/dd/2018/09/07/4-years-later-google-finally-explains-the-origins-of-its-chrome-dinosaur-game/), naming it after [Marc Bolan](https://en.wikipedia.org/wiki/Marc_Bolan), the lead singer of the 1970's band, [T-Rex](https://en.wikipedia.org/wiki/T._Rex_(band)). As such, while the game is more often referenced today as the "Dinosaur Game," "T-Rex Game," or "Dino Runner," this project's name, "Bolan.py," was chosen to honor its parent's past pseudonym.

## Specifications

### Content Limitations

While the game was made to best mirror that of the original's, it does have its shortcomings. Specifically, it has yet to support a proper **day/night cycle**. As of now, the author does not have any intentions of adding such a feature to the game but it would make for a great contribution to the repository.

### Spritesheet Utilization

The project makes use of a single sprite sheet to blit its 2D assets onto the screen. This was done in order to increase performance instead of using multiple differently blitted image files. In doing so, the author made use of a borrowed version of [Eric Matthes's  ```SpriteSheet```  class](https://ehmatthes.github.io/pcc_2e/beyond_pcc/pygame_sprite_sheets/) in order to effectively manipulate the images in the sheet. 

For reference, the ```SpriteSheet``` class used by the repository can be found in ```spritesheet.py```.

## Installation and Usage

**Note**: Skip the first step if Python 3 is already installed on your computer. You may also skip step two if you already have Pygame installed.

1. [Install Python](https://www.python.org/downloads/). Version 3.8.3 and above is recommended.

2. [Install Pygame](https://www.pygame.org/wiki/GettingStarted). Version 2.0.0 and above is recommended. 

3. Clone the repository (or download it as a .zip file and extract it).

4. Navigate to the repository's `/bolan` directory and run `main.py`. One may do so by double-clicking `main.py` or by using a command line interface and entering the following:

   ```
   $ python3 main.py
   ```

   If that doesn't work, one may also try entering `python main.py` instead of the above.

## Contributing

Pull requests are welcome for those that would like to make a contribution. On that note, for those that would like to apply major changes to the repository, we'd like to request that you open up an issue first and discuss the changes you'd like to make.

## License

[MIT License](LICENSE.txt)

