import cmd
import ClientIF
import websocket
import threading
import json

# Disable specific pylint warnings for the entire file
# pylint: disable=missing-function-docstring, invalid-name

SERVER_IP = "127.0.0.1:8000"
SERVER_URL = f"http://{SERVER_IP}"
WS_URL = f"ws://{SERVER_IP}/ws/notifications/"

class cmdClientIF(cmd.Cmd):

    intro = """
      ####### ##        ##      ##  ########
     ##       ##        ##      ##  ##
    ##        ##        ##      ##  ##
    ##        ##        ##      ##  #####
    ##        ##        ##      ##  ##
     ##       ##        ##      ##  ##
      ####### ######### ##########  ########

    Welcome to team Elemnt Edge's Clueless - CLI
        Type help or ? to list commands"""
    prompt = "(cli-Clueless) "

    def __init__(self, base_url):
        super().__init__()
        self.client = ClientIF.ClientIF(base_url)
        self.websocket_thread = threading.Thread(target=self.start_websocket, daemon=True)
        self.websocket_thread.start()  # Start the WebSocket listener in a separate thread

    def start_websocket(self):
        websocket_url = WS_URL
        ws = websocket.WebSocketApp(websocket_url,
                                    on_open=self.on_open,
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        ws.run_forever()

    def on_message(self, ws, message):
        data = json.loads(message)
        print(f"\nNotification: {data['message']}")  # Print the notification message
        print(self.prompt, end='')  # Reprint the prompt after displaying the notification

    def on_error(self, ws, error):
        print(f"Error: connection error being called...{error}")

    def on_close(self, ws):
        print("Connection closed")

    def on_open(self, ws):
        print("Connected to WebSocket")

    def do_register(self, args):
        """Register a new account: register <username> <password> <re-enter Password>"""
        self.client.register(args)

    def do_login(self, args):
        """Login to your account: login <username> <password>"""
        self.client.login(args)

    def do_logout(self, arg):
        """Log out of your account: logout"""
        self.client.logout(arg)

    def do_send(self, message):
        """Send a message to another user: send <username> <message>"""
        self.client.send(message)

    def do_sendToAll(self, message):
        """Send a message to all connected users: sendToAll <message>"""
        self.client.senToAll(message)

    def do_receive(self, arg):
        """Receive messages from the server: receive"""
        self.client.receive(arg)

    def do_createGame(self, ws):
        """Create a game lobby: createGame"""
        self.client.createGame()

    def do_joinGame(self, arg):
        """Join a game lobby: joinGame <key>"""
        self.client.joinGame(arg)

    def do_leaveGame(self, ws):
        """Leave a game lobby: leaveGame"""
        self.client.leaveGame()

    def do_startGame(self, ws):
        """Start a game: leaveGame"""
        self.client.startGame()

    def do_chooseCharacter(self, arg):
        """Choose a character: chooseCharacter <character_name>"""
        self.client.chooseCharacter(arg)
        
    def do_playerMove(self, arg):
        """Move your piece: playerMove <room>"""
        self.client.chooseCharacter(arg)

    def do_makeSuggestion(self, arg):
        """Make a suggestion: makeSuggestion <perpetrator> <weapon> <room>"""
        self.client.makeSuggestion(arg)

    def do_makeAccusation(self, arg):
        """Make an accusation: makeAccusation <perpetrator> <weapon> <room>"""
        self.client.makeAccusation(arg)

    def do_EndTurn(self, ws):
        """End your turn: endTurn"""
        self.client.endTurn()

    def do_EndGameEarlyRequest(self):
        """End game early request: endGameEarly"""
        self.client.EndGameEarlyRequest()

    def do_EndGameEarlyVote(self):
        """Vote to end the game early: endGameEarlyVote"""
        self.client.EndGameEarlyVote()

    def do_exit(self, arg):
        "Exit the CLI: exit"
        print("Thank you. Goodbye!")
        return True

if __name__ == "__main__":
    cli = cmdClientIF(SERVER_URL)  # Adjust the base URL as needed
    cli.cmdloop()