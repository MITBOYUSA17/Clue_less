import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from GameManagement.models import GameRoom

class NotificationConsumer(AsyncWebsocketConsumer):
    """
    A WebSocket consumer for handling real-time notifications.

    This class manages WebSocket connections for sending notifications to clients.
    It allows clients to connect to a notification group and receive messages in real-time.

    Methods:
        connect(): Accepts the WebSocket connection and joins the notifications group.
        disconnect(close_code): Leaves the notifications group upon disconnection.
        notify(event): Sends a notification message to the WebSocket client.
    """
    async def connect(self):
        """
        Handle WebSocket connection requests.

        This method is called when a client connects to the WebSocket.
        It adds the client to the 'notifications' group and accepts the connection.
        """
        try:
            self.channel_layer = get_channel_layer()  # Get the channel layer
            await self.channel_layer.group_add("notifications", self.channel_name)  # Join the notifications group
            await self.accept()  # Accept the WebSocket connection
        except Exception as e:
            # Log the error or handle it appropriately
            print(f"Error while connecting to notifications group: {e}")

    async def disconnect(self, close_code: int) -> None:
        """
        Handle WebSocket disconnection requests.

        This method is called when a client disconnects from the WebSocket.
        It removes the client from the 'notifications' group.

        Args:
            close_code (int): The code indicating why the WebSocket connection was closed.
        """
        try:
            await self.channel_layer.group_discard("notifications", self.channel_name)  # Leave the notifications group
        except Exception as e:
            # Log the error or handle it appropriately
            print(f"Error while disconnecting from notifications group: {e}")

    async def notify(self, event: dict) -> None:
        """
        Send a notification message to the WebSocket client.

        This method is called when a notification event occurs. It sends the message
        contained in the event to the connected WebSocket client.

        Args:
            event (dict): The event dictionary containing the notification message.
        """
        try:
            message = event['message']  # Extract the message from the event
            await self.send(text_data=json.dumps({'message': message}))  # Send the notification message to WebSocket
        except KeyError:
            print("Notification event does not contain 'message' key.")
        except Exception as e:
            # Log the error or handle it appropriately
            print(f"Error while sending notification: {e}")


class GameRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        # retrieves the user associated with the request
        self.game_id = self.scope["url_route"]["kwargs"]["game_id"]
        # retrieves the game_id provided with the request
        if self.user.is_authenticated:
            # verifies that the user sending the request is authenticated 
            # via Django back-end authentication mechanisms
            self.game_room = await self.get_room()
            # attempts to get the game room id associates with users request
            if self.game_room is not None:
            # ASSERT: The game room id provided is in the db.
                if self.can_join():
                    self.channel_layer = get_channel_layer()  # Get the channel layer
                    await self.channel_layer.group_add("gamerooms", self.game_id)  # Join the notifications group
                    await self.accept()  # Accept the WebSocket connection
                    await self.send(f"Connected to game room {self.game_id}\nStatus {self.game_room.status}\nPlayer Count: {self.game_room.player_count}")
                else:
                    await self.close()
            else:
                await self.send(f"Game room '{self.game_id} could not be found.")
                # executes custom function that sends the error message to the Client and Server.
                await self.close()
                # closes the connection due to failure
        else:
            await self.send("User authentication failed")
            await self.close()
            # closes the connection due to failure
    async def can_join(self) -> bool:
        can_join = False
        if self.is_space():
            if self.is_room_available():
                if self.is_valid_passcode():
                    can_join = True
                else:
                    await self.send(f"Invalid room passcode for {self.game_room.game_id}")
            
            else:
                await self.send(f"The Room is {self.game_room.status}, and cannot be joined.")
        
        else:
            await self.send(f"The Room is full, players: {self.game_room.player_count}/{self.game_room.max_players}")
        return can_join

    async def is_valid_passcode(self) -> bool:
        is_valid = True
        if self.game_room.is_private:
            passcode = self.scope.get("query_string").get("passcode")
            is_valid = passcode == self.game_room.passcode
        return is_valid
            
    async def is_room_available(self) -> bool:
        return self.game_room.status == "Open"

    async def is_space(self) -> bool:
        return self.game_room.player_count < self.game_room.max_players
    
    async def send_welcome_msg(self):
        data = json.dumps({
            "message": f"Welcome to game room {self.game_id}.",
            "status": self.game_room.status,
            "player_count": self.game_room.player_count
        })
        await self.send(text_data=data)

    async def add_to_groups(self):
        await self.channel_layer.group_add(f"gameroom_{self.game_id}", self.channel_name)


    async def get_room(self) -> GameRoom | None:
        try:
            return GameRoom.objects.get(game_id=self.game_id)
        except GameRoom.DoesNotExist:
            return None
        
    async def disconnect(self):
        await self.remove_from_groups()

class GameRoomChat(AsyncWebsocketConsumer):
    pass
