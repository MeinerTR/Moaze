import pygame;
from typing import Tuple;

class Object:
    wall    :int = 0;
    lspin   :int = 1; # later maybe
    rspin   :int = 2; # later maybe
    finish  :int = 3;

class Game:
    def __init__(self, width:int, height:int, title:str):
        
        #-# window #-#
        self.win_size   :Tuple[int, int] = (width, height);
        pygame.display.set_caption(title);
        self.window = pygame.display.set_mode(self.win_size);

        #-# statuses #-#
        self.running    :bool = True;
        self.level      :int = 0;

        #-# map[[type, size, [startx, starty, endx, endy]]...]
        map:Tuple[Tuple[int, int, Tuple[int, int, int, int]]];

    def main_loop(self, FPS:int):
        self.init_level(self.level);
        
        while self.running:
            
            #-# inputs #-#
            self.handle_events();

            #-# outputs #-#
            self.window.fill([0, 0, 0]);
            self.draw_level();
            pygame.display.flip();

    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit(); exit();
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); exit();

            #-# mouse collisions #-#
            elif event.type == pygame.MOUSEMOTION:

                #-# window left | top #-#
                if event.pos[0] == 0 or event.pos[1] == 0:
                    print("you lost!");
                    pygame.quit(); exit();
                
                #-# window right #-#
                if event.pos[0] == self.win_size[0] - 1:
                    print("you lost!");
                    pygame.quit(); exit();

                #-# window bottom #-#
                if event.pos[1] == self.win_size[1] - 1:
                    print("you lost!");
                    pygame.quit(); exit();

                color = self.window.get_at(pygame.mouse.get_pos())[:3];
            
                #-# wall collision #-#
                if color == (255, 255, 255):
                    print("you lost!");
                    pygame.quit(); exit();

                #-# finish collision #-#
                elif color == (0, 255, 0):
                    print("you won!");
                    pygame.quit(); exit();

    def draw_level(self):
        for map in self.map:
            if map[0] == Object.wall:
                pygame.draw.line(self.window, (255, 255, 255),
                    (map[2][0], map[2][1]),
                    (map[2][2], map[2][3]), map[1]);
            
            elif map[0] == Object.finish:
                pygame.draw.line(self.window, (0, 255, 0),
                    (map[2][0], map[2][1]),
                    (map[2][2], map[2][3]), map[1]);

    def init_level(self, level:int):
        width:int; height:int;
        width, height = self.win_size;
        hwidth  :int = int(width / 2);
        hheight :int = int(height / 2);

        #-# example level #-#
        if level == 0: self.map = (   
                (Object.wall,   20, (0, int(hheight / 2), width - int(width / 3), int(hheight / 2))),
                (Object.wall,   20, (int(hwidth / 3), hheight, width, hheight)),
                (Object.wall,   20, (0, int(hheight * 1.5), width - int(width / 3), int(hheight * 1.5))),
                (Object.finish, 20, (int(hwidth / 4), int(hheight * 1.5), int(hwidth / 4), height))
            ); pygame.mouse.set_pos([int(hwidth / 2), int(hheight / 3)]);

if __name__ == "__main__":
    pygame.init();

    game:Game = Game(640, 480, "Moaze");
    game.main_loop(60);
