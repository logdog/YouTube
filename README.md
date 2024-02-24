For installation guide, scoll to bottom of this page!

# About Me
Hi everyone! My name is Logan, and I am a PhD student in Electrical Engineering at Purdue University. I love teaching, so in my spare time, I like to put together videos that I wish existed when I was an undergraduate student! I hope these videos inspire you to try and simulate your own mechanical sysetms, and learn some fun mathematics!

## YouTube Channel
[Logan Dihel on YouTube.](https://youtube.com/@logandihel) Learn engineering, math, and computer science from a graduate student and (former) NASA engineer! My goal is to teach $10^6$ people something new with short, digestible content. I try to target more advanced topics that are not covered well on YouTube.

## Lagrangian Mechanics
Lagrangian mechanics is a beautiful way to model a mechanical system using energy. I have a series of videos teaching you how to use Lagrangian mechanics for a variety of systems. All of the code for these videos are compiled in this repo. More to come!
* [Full Playlist](https://www.youtube.com/watch?v=FZjRTbYPjgk&list=PLb1f9nCDJiAtMum_n9U3y3ktrBaIzeVmk)
* [Introduction](https://www.youtube.com/watch?v=FZjRTbYPjgk)
* [Simple Pendulum](https://www.youtube.com/watch?v=0PUrSlr6XCk&t=1s) (part 1, 2, 3)
* [Spring Mass](https://www.youtube.com/watch?v=HaQwLfKOvKI) (part 1, 2)
* [Elastic Pendulum](https://www.youtube.com/watch?v=K6FzJUDPE9M)
* [Kapitza Pendulum](https://www.youtube.com/watch?v=oeneVhFh4-o)
* [Double Pendulum](https://www.youtube.com/watch?v=sxL3KQgFLcI)

## Commonly Asked Questions
_Why do you use Python and not MATLAB in your videos?_

I believe that anyone who wants to learn engineering should be able to with free, publically available software. While MATLAB is a wonderful tool, but it is prohibitively expensive if you don't have access through an institution. Python is the world's most popular programming language, and it's free!

_How did you learn all this stuff?_

I learned Lagrangian mechanics from watching YouTube videos and reading free online lecture notes. I started with common systems (pendulum, spring mass) so that I could compare answers against online answers. When learning something new, I always start small.

_What is the best way to get started programming?_

The best way to learn anything is do jump into it and create. You don't need to spend hours and hours watching tutorials online. All you need is an understanding of variables and simple functions to do most tasks.

Pick a small project that excites you: the simpler, the better. For graphics, use print statements in your terminal. Print out a Christmas tree using \* characters in your terminal, or make a simple hangman game. With every project you complete, your confidence and ability to read documentation will grow. I particularly like making games, as they are really fun to make and will test your abilities as a programmer. 

# Installation Guide (Windows 10/11)
1. Install latest version of [Python](https://www.python.org/downloads/). Select checkboxes "Use admin privileges" and "Add python to PATH" if possible. Verify proper install by opening a new terminal and running `python -v`.
   
2. Install [FFMPEG](https://ffmpeg.org/download.html) (this is for creating MP4 and GIF files). I recommend using [Chocolately](https://chocolatey.org/install) to do this process. In a powershell window, install Chocolately with
```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
Once this is done, open a new powershell window and run
```
choco install ffmpeg
```
You may need to answer some questions by typing `y` or `a` in order to finish the installation process. Verify proper install by opening new terminal and running `ffmpeg` and checking the program runs.

3. Install [VSCode](https://code.visualstudio.com/download). I recommend checking the optional "Open with Code" boxes in the installation on page 5.

4. Install [git for windows](https://git-scm.com/download/win). I recommend changing the default editor to Visual Studio Code in the installatoin on page 5. Verify proper install by opening a new terminal and running `git -v`.
   
5. Copy the code in this repository. In the command line, navigate to suitable location. Then run
```
git clone https://github.com/logdog/YouTube.git
```
The folder YouTube will have been created. Type `cd YouTube` to change directory.

6. Open VSCode in the YouTube folder. You can type `code .` in the YouTube folder on the command line, or open VSCode and then open the YouTube folder.

7. Install extensions in VSCode. Open the extensions tab (`Ctrl+Shift+X`). I recommend the Python extension and the Jupyter extension.
   
8. Create a Python virtual environment. Type `Ctrl+Shift+P` and then type `Python: Create Environment`. Select `.venv` and then select the desired version of Python.
    
9. Source the virtual environment. Open a new command prompt (press `` Ctrl+` `` to open terminal and type `cmd` to open a command prompt). Then type `.venv\Scripts\activate`. When you run
```
python -c "import sys; print(sys.prefix)"
```
the printed path should end in `.venv`

10. `pip` install all Python modules. Here are a few which are needed, but feel free to install whatever you'd like.
```
pip install numpy scipy matplotlib moviepy
```

11. Open Jupyter Notebook file in VSCode. For example, open `Lagrangian Mechanics in Python/Elastic Pendulum/animate.ipynb`. Select In the top right corner, be sure to select the `.venv` kernel.

12. Run the notebook. A popup may appear asking you to install ipykernel package. Hit Install and wait a few moments for this install to finish. Then, run the notebook again by clicking the "Run All" button in the top left corner. The entire script should run and produce `.mp4` files when complete. Change the initial conditions for yourself to experiment and play around! For example, 
```
x0 = np.array([np.deg2rad(-30), 0, 0.25, 0])
```

## Issues:
If you find any issues with this code base, don't hesitate to bring them to my attention! Please open a new issue on this Github repository so we can address the problem.
