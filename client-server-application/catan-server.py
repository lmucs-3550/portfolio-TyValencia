# catan-server.py
# Ty Valencia
# LMU CMSI3550

import socketserver
import threading
import random

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

class Tile:
    def __init__(self, column, row, tile_type, value, player_associated=None):
        self.column = column
        self.row = row
        self.tile_type = tile_type
        self.value = value
        self.player_associated = player_associated

def create_board():
    columns = [
        [None] * 3,
        [None] * 4,
        [None] * 5,
        [None] * 4,
        [None] * 3
    ]
    tile_types = ["wood", "brick", "stone", "wheat", "sheep"]

    for col in range(len(columns)):
        for row in range(len(columns[col])):
            tile_type = random.choice(tile_types)
            value = random.randint(1, 6) + random.randint(1, 6)
            columns[col][row] = Tile(col, row, tile_type, value)
    return columns

class PlayerHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.opponent = None
        client = f'{self.client_address} on {threading.currentThread().getName()}'
        print(f'Connected: {client}')
        try:
            self.initialize()
            self.process_commands()
        except Exception as e:
            print(e)
        finally:
            try:
                self.opponent.send('OTHER_PLAYER_LEFT')
            except:
                # Hack for when the game ends, not happy about this
                pass
        print(f'Closed: {client}')

        def roll_dice(self):
        	return random.randint(1, 6) + random.randint(1, 6)

    def initialize(self):
        Game.join(self)
        self.send('WELCOME ' + self.mark)
        if self.mark == 'X':
            self.game.current_player = self
            self.send('MESSAGE Rolling dice...')
            self.dice_roll = self.roll_dice()
            self.send(f'MESSAGE You rolled {self.dice_roll}')
            self.send('MESSAGE Waiting for opponent to connect')
        else:
            self.opponent = self.game.current_player
            self.opponent.opponent = self
            self.dice_roll = self.roll_dice()
            self.send(f'MESSAGE You rolled {self.dice_roll}')
            self.opponent.send(f'OPPONENT_ROLLED {self.dice_roll}')

            if self.dice_roll > self.opponent.dice_roll:
                self.game.current_player = self
                self.send('MESSAGE Your move')
                self.opponent.send('MESSAGE Opponent has a higher roll. Their move')
            else:
                self.game.current_player = self.opponent
                self.opponent.send('MESSAGE Your move')
                self.send('MESSAGE Opponent has a higher roll. Their move')

    def process_commands(self):
        while True:
            command = self.rfile.readline()
            if not command:
                break
            command = command.decode('utf-8')
            if command.startswith('QUIT'):
                return
            elif command.startswith('MOVE'):
                self.process_move_command(int(command[5:]))
            elif command.startswith('ASSOCIATE'):
                col, row = map(int, command[10:].split())
                self.process_associate_command(col, row)

    def process_associate_command(self, col, row):
        if self.game.current_player != self:
            self.send('MESSAGE Not your turn')
            return
        try:
            tile = self.game.board[col][row]
            if tile.player_associated is not None:
                self.send('MESSAGE Tile already associated')
            else:
                tile.player_associated = self
                self.send('VALID_ASSOCIATE')
                self.opponent.send(f'OPPONENT_ASSOCIATED {col} {row}')
                self.game.current_player = self.opponent
        except IndexError:
            self.send('MESSAGE Invalid tile')

    def send(self, message):
        self.wfile.write(f'{message}\n'.encode('utf-8'))

    def initialize(self):
        Game.join(self)
        self.send('WELCOME ' + self.mark)
        if self.mark == 'X':
            self.game.current_player = self
            self.send('MESSAGE Waiting for opponent to connect')
        else:
            self.opponent = self.game.current_player
            self.opponent.opponent = self
            self.opponent.send('MESSAGE Your move')

    def process_commands(self):
        while True:
            command = self.rfile.readline()
            if not command:
                break
            command = command.decode('utf-8')
            if command.startswith('QUIT'):
                return
            elif command.startswith('MOVE'):
                self.process_move_command(int(command[5:]))
                
    def process_move_command(self, location):
        # Implement any game moves or actions here.
        pass

class Game:
    next_game = None
    game_selection_lock = threading.Lock()

    def __init__(self):
        self.board = create_board()
        self.current_player = None
        self.lock = threading.Lock()

    @classmethod
    def join(cls, player):
        with cls.game_selection_lock:
            if cls.next_game is None:
                cls.next_game = Game()
                player.game = cls.next_game
                player.mark = 'X'
            else:
                player.mark = 'O'
                player.game = cls.next_game
                cls.next_game = None

with ThreadedTCPServer(('', 50000), PlayerHandler) as server:
    print(f'The Catan server is running...')
    server.serve_forever()