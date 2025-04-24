import random

class Player():
    def __init__(self,size,current_step = None):
        if current_step is None:
            self.current_step = 0
            self.size = size

    def check_ladder_snake(self,ladder,snake):
        if self.current_step in ladder:
            self.current_step = ladder[self.current_step]

        elif self.current_step in snake:
            self.current_step = snake[self.current_step]

        return self.current_step

    def update_snake_step(self,newval):
        if self.current_step + newval <= 100:
            self.current_step += newval
        self.current_step = self.check_ladder_snake(ladder,snake)
                
    def check_victorius(self):
        if self.current_step == self.size:
            return True
        return False


class Board():
    def __init__(self,players):
        self.players = players
        self.playersindex = {}
        self.playersqueue = []
        for idx,player in self.players.items():
            self.playersindex[player] = idx
            self.playersqueue.append(player)
        self.current_player = self.playersqueue.pop(0)
        
        
    def play_game(self):
        res = []
        dice_rolled = random.randint(1,6)
        self.current_player.update_snake_step(dice_rolled)
        while(len(self.playersqueue) > 0):
            if self.current_player.check_victorius() == True:
                res.append(f"Player {self.playersindex[self.current_player]}")
            else:
                self.playersqueue.append(self.current_player)

            dice_rolled = random.randint(1,6)
            self.current_player = self.playersqueue.pop(0)
            self.current_player.update_snake_step(dice_rolled)
            print(self.current_player.current_step,self.playersindex[self.current_player],self.playersqueue)

        res.append(f"Player {self.playersindex[self.current_player]}")
        return res

if __name__ == '__main__':
    global ladder 
    global snakes
    ladder = {5:58,14:49,42:60,64:83,53:72,75:94}
    snake = {38:20,45:7,97:61,65:54,91:73,97:61}
    size = 100
    
    no_of_players = int(input("Enter the total no of players:"))
    players = {}
    for i in range(0,no_of_players):
        players[i] = Player(size)
    print(players[0])
    board = Board(players)
    res = board.play_game()
    print(res)
