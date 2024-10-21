import requests
import uuid

class ClientIF():
    """
    Client Interface: Interface between the client and the server.

    This class provides methods for the Authentication, Game Management,
    and Message Translator subsystems and interacting with the server for game-related functionalities.

    Attributes:
        base_url (str): The base URL of the server.
        session (requests.Session): The HTTP session used for making requests.
        is_logged_in (bool): A flag indicating whether the user is logged in.
    """

    def __init__(self, base_url: str) -> None:
        """
        Initialize the ClientIF with the base URL.

        Args:
            base_url (str): The base URL of the server.
        """
        self.base_url = base_url
        self.session = requests.Session()  # Create a session for persistent connections
        self.is_logged_in = False  # Track login status
        print(f"Client IF: base URL: {base_url}")

    def setCookies(self, args: str) -> None:
        """
        Set cookies for the session (to be implemented).
        """
        # TODO: Implement cookie handling
        pass

    def register(self, args: str) -> None:
        """
        Register a new account with the provided username and passwords.

        Args:
            args (str): A string containing username, password1, and password2.

        Raises:
            ValueError: If the input format is incorrect or registration fails.
        """
        try:
            username, password1, password2 = args.split()
            data = {
                'username': username,
                'password1': password1,
                'password2': password2,
            }

            response = self.session.post(f"{self.base_url}/register/", data=data)
            response.raise_for_status()  # Raise an error for bad responses
            print(response.json())

        except ValueError:
            print("Error: Please provide username, password1, and password2.")
        except requests.RequestException as e:
            print(f"Registration failed: {e}")

    def login(self, args: str) -> None:
        """
        Log in to the account using the provided username and password.

        Args:
            args (str): A string containing username and password.

        Raises:
            ValueError: If the input format is incorrect.
        """
        try:
            username, password = args.split()
            response = self.session.post(f"{self.base_url}/login/", data={'username': username, 'password': password})
            response.raise_for_status()  # Raise an error for bad responses

            self.is_logged_in = True
            print("Logged in successfully.")

        except ValueError:
            print("Error: Please provide both username and password.")
        except requests.RequestException as e:
            print(f"Login failed: {e}")

    def logout(self) -> None:
        """
        Log out of the current account.

        Raises:
            requests.RequestException: If the logout request fails.
        """
        response = self.session.post(f"{self.base_url}/logout/")
        try:
            response.raise_for_status()  # Raise an error for bad responses
            self.is_logged_in = False
            print("Logged out successfully.")
        except requests.RequestException as e:
            print(f"Logout failed: {e}")

    def send(self, args: str) -> None:
        """
        Send a message to another user.

        Args:
            args (str): A string containing the recipient's username and the message.

        Raises:
            ValueError: If the user is not logged in or input format is incorrect.
        """
        if not self.is_logged_in:
            print("You must be logged in to send messages.")
            return

        try:
            username, message = args.split(maxsplit=1)
            response = self.session.post(f"{self.base_url}/send-message/", data={'recipient': username, 'message': message})
            response.raise_for_status()  # Raise an error for bad responses
            print(response.json())
        except ValueError:
            print("Error: Please provide both username and message.")
        except requests.RequestException as e:
            print(f"Failed to send message: {e}")

    def createGame(self):
        """
        Create a game lobby.

        Raises:
            RequestException: If the create game lobby request fails.
        """
        try:
            response = self.session.post(f"{self.base_url}/create_game/")
            response.raise_for_status()  # Raise an error for bad responses
            print(response.json())

        except requests.RequestException as e:
            print(f"Create game lobby failed: {e}")

    def joinGame(self, arg):
        """
        Join a game lobby.

        Args:
            args (str): A string containing a UUID for the game to join.

        Raises:
            ValueError: If the input format is incorrect.
             RequestException: If the join game lobby fails.
        """
        try:
            uuid.UUID(arg) # validtes UUID string; throws ValueError on failed parsing

            data = {
                'key': arg,
            }

            response = self.session.post(f"{self.base_url}/join_game/", data=data)
            response.raise_for_status()  # Raise an error for bad responses
            print(response.json())

        except ValueError:
            print("Error: Please provide a valid UUID key.")
        except requests.RequestException as e:
            print(f"Join game lobby failed: {e}")

    def leaveGame(self):
        """
        Leave a game lobby.

        Raises:
            RequestException: If the leave game lobby request fails.
        """
        try:
            response = self.session.post(f"{self.base_url}/leave_game/")
            response.raise_for_status()  # Raise an error for bad responses
            print(response.json())

        except requests.RequestException as e:
            print(f"Leave game lobby failed: {e}")

    def startGame(self):
        """
        Starts a game.

        Raises:
            RequestException: If the start game request fails.
        """
        try:
            response = self.session.post(f"{self.base_url}/start_game/")
            response.raise_for_status()  # Raise an error for bad responses
            print(response.json())

        except requests.RequestException as e:
            print(f"Start game failed: {e}")

    def chooseCharacter(self, arg):
        """
        Chooses a character in the game lobby.

        Raises:
            RequestException: If the choose character request fails.
        """

        data = {
                'key': arg,
            }
        
        try:
            response = self.session.post(f"{self.base_url}/choose_character/", data=data)
            response.raise_for_status()  # Raise an error for bad responses
            print(response.json())

        except requests.RequestException as e:
            print(f"Choose character failed: {e}")

    def playerMove(self, arg):
        """
        Move a player token.

        Raises:
            RequestException: If the player move fails.
        """

        data = {
                'room': arg,
            }
        
        try:
            response = self.session.post(f"{self.base_url}/player_move/", data=data)
            response.raise_for_status()  # Raise an error for bad responses
            print(response.json())

        except requests.RequestException as e:
            print(f"Player move failed: {e}")

    def makeSuggestion(self, args):
        """
        Make a suggestion.

        Raises:
            RequestException: If the suggestion fails.
        """

        character, weapon, room = args.split()
        data = {
                'character': character,
                'weapon': weapon,
                'room': room,
            }
        
        try:
            response = self.session.post(f"{self.base_url}/make_suggestion/", data=data)
            response.raise_for_status()  # Raise an error for bad responses
            print(response.json())

        except requests.RequestException as e:
            print(f"Make suggestion failed: {e}")

    def makeAccusation(self, args):
        """
        Make an accusation.

        Raises:
            RequestException: If the accusation fails.
        """

        character, weapon, room = args.split()
        data = {
                'character': character,
                'weapon': weapon,
                'room': room,
            }
        
        try:
            response = self.session.post(f"{self.base_url}/make_accusation/", data=data)
            response.raise_for_status()  # Raise an error for bad responses
            print(response.json())

        except requests.RequestException as e:
            print(f"Make accusation failed: {e}")

    def EndTurn(self, ws):
        """
        Ends a player's turn.

        Raises:
            RequestException: If the end turn request fails.
        """
        try:
            response = self.session.post(f"{self.base_url}/end_turn/")
            response.raise_for_status()  # Raise an error for bad responses
            print(response.json())

        except requests.RequestException as e:
            print(f"End turn failed: {e}")

    def EndGameEarlyRequest(self, ws):
        """
        Ends game early request.

        Raises:
            RequestException: If the request to end the game early fails.
        """
        try:
            response = self.session.post(f"{self.base_url}/end_game_early_request/")
            response.raise_for_status()  # Raise an error for bad responses
            print(response.json())

        except requests.RequestException as e:
            print(f"End game early request failed: {e}")

    def EndGameEarlyRequest(self, arg):
        """
        Ends game early vote.

        Raises:
            RequestException: If the vote to end the game early fails.
        """
        try:
            response = self.session.post(f"{self.base_url}/end_game_early_vote/")
            response.raise_for_status()  # Raise an error for bad responses
            print(response.json())

        except requests.RequestException as e:
            print(f"End game early vote failed: {e}")

    def exit(self, arg):
        """
        Exit the CLI.

        Args:
            arg (str): Command to exit.

        Returns:
            bool: Always returns True to indicate exit.
        """
        print("Thank you. Goodbye!")
        return True