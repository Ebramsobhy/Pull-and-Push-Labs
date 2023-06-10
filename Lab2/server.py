import json
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class ChatApp(WebSocket):
    """Implement three basic functions"""
    clients = []
    def handleConnected(self):   
        ChatApp.clients.append(self)
        print(f"nummber of connected users till now {len(self.__class__.clients)}")    

    def handleClose(self):
        print(f"--- client disconnected {self.address}")
        self.__class__.clients.remove(self)
        print(f"nummber of connected users till now {len(self.__class__.clients)}")

        for client in self.__class__.clients:
            client.sendMessage(self.address[0] + U' - disconnected')
    
    def handleMessage(self):
        msg_to_send = self.prepare_message(self.data)
        print("in handle", msg_to_send)
        for client in self.__class__.clients:
            if client != self:
                client.sendMessage(msg_to_send)

    def prepare_message(self, data):
        data = json.loads(data)
        msg = {}
        if data["type"] == 'login':
            msg = {"message": f"{data['name']} has been joined\n"}
            self.name = data["name"]

        elif data["type"] == "chat":
            msg = {"message": f"{self.name}:{data['body']}\n"} 

        return json.dumps(msg)    
                     
if __name__ == "__main__":
    server = SimpleWebSocketServer('', 8080, ChatApp)
    print("--- Server started ---")
    server.serveforever()

