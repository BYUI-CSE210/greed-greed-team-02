import os
import random

from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.rock import Rock
from game.casting.gem import Gem

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed - Team 02"
WHITE = Color(255, 255, 255)


def main():

    # create the cast
    cast = Cast()

    # create the banner
    banner = Actor()
    banner.set_text("The Score")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    score = 0


    #create the robot, this is copypasta from rfk
    x = int(MAX_X / 2)
    y = MAX_Y-(CELL_SIZE*2) #we will be changing this to the bottom of the screen
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)


    #maybe also start with a couple objects too.

    for n in range(random.randint(3,6)):

        #true for rock, false for gem
        is_rock = random.choice([Gem, Rock])

        x = random.randint(1, COLS - 1)
        y = 1 #we will be changing this to the top of the screen
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        #check for collision with another generated object and make sure there is no conflict

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        object = is_rock()

        object.set_font_size(FONT_SIZE)
        object.set_color(color)
        object.set_position(position)
        cast.add_actor("objects", object)


    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(
        CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
