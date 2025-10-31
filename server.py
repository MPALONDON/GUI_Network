import json
import tkinter,socket,threading

root = tkinter.Tk()
root.title("Chat Server")
root.geometry("800x800")
root.resizable(False,False)

my_font = ("SimSun",14)
black = "#010101"
red = "#FF0000"
root.config(bg=black)

class Connection:
    def __init__(self):
        self.host_ip = socket.gethostbyname(socket.gethostname())
        self.encoder = "utf-8"
        self.byte_size = 1024
        self.client_sockets = []
        self.client_ips = []
        self.banned_ips = []


def start_server(connection):
    connection.port = int(port_entry.get())
    connection.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connection.server_socket.bind((connection.host_ip,connection.port))
    connection.server_socket.listen()

    history_listbox.delete(0,"end")
    history_listbox.insert(0,f"Server started on port {connection.port}")
    end_button.config(state="normal")
    self_broadcast_button.config(state="normal")
    message_button.config(state="normal")
    kick_button.config(state="normal")
    ban_button.config(state="normal")
    start_button.config(state="disabled")

    threading.Thread(target=connect_client, args=(connection,)).start()


def end_server(connection):
    pass

def connect_client(connection):
    while True:
        try:
            client_socket, client_address = connection.server_socket.accept()
            if client_address[0] in connection.banned_ips:
                message_packet = create_message(flag = "DISCONNECT",name = "Admin (private)",
                                                message = "You have been banned...",colour=red)
                message_json = json.dumps(message_packet)
                client_socket.send(message_json.encode(connection.encoder))
                client_socket.close()
            else:
                message_packet = create_message(flag = "INFO",name = "Admin (private)",
                                                message = "Please send your name...",colour=red)
                message_json = json.dumps(message_packet)
                client_socket.send(message_json.encode(connection.encoder))
                message_json = client_socket.recv(connection.byte_size)
                process_message(connection,message_json,client_socket,client_address)

        except:
            break


def create_message(flag,name,message,colour):
    message_packet = {
        "flag": flag,
        "name": name,
        "message": message,
        "colour": colour
    }
    return message_packet

def process_message(connection,message_json,client_socket,client_address=(0,0)):
    message_packet = json.loads(message_json)
    flag = message_packet["flag"]
    name = message_packet["name"]
    message = message_packet["message"]
    colour = message_packet["colour"]

    if flag == "INFO":
        connection.client_sockets.append(client_socket)
        connection.client_ips.append(client_address[0])
        message_packet = create_message(flag = "MESSAGE", name = "ADMIN (broadcast)",
                                        message = f"{name} has joined the server!!!", colour = red)
        message_json = json.dumps(message_packet)
        broadcast_message(connection,message_json.encode(connection.encoder))
        client_listbox.insert("end",f"Name: {name}         IP ADDR: {client_address[0]}")
        receive_thread = threading.Thread(target = receive_message, args=(connection,client_socket,))
        receive_thread.start()

    elif flag == "MESSAGE":
        pass

    elif flag == "DISCONNECT":
        pass

    else:
        history_listbox.insert(0, "Error processing message...")

def broadcast_message(connection,message_json):
    for client_socket in connection.client_sockets:
        client_socket.send(message_json)

def receive_message(connection, client_socket):
    pass

def self_broadcast(connection):
    pass

def private_message(connection):
    pass

def kick_client(connection):
    pass

def ban_client(connection):
    pass


connection_frame = tkinter.Frame(root,bg=black)
history_frame = tkinter.Frame(root,bg=black)
client_frame = tkinter.Frame(root,bg=black)
message_frame = tkinter.Frame(root,bg=black)
admin_frame = tkinter.Frame(root,bg=black)

connection_frame.pack(pady=5)
history_frame.pack()
client_frame.pack(pady=5)
message_frame.pack()
admin_frame.pack()

post_label = tkinter.Label(
    connection_frame, text="Port Number:",font=my_font, bg=black, fg=red)
port_entry = tkinter.Entry(
    connection_frame,width=10, borderwidth=3, font=my_font)
start_button = tkinter.Button(
    connection_frame,text="Start Server", borderwidth=5, width=15,font=my_font, bg=red, command=lambda:start_server(my_connection))
end_button = tkinter.Button(
    connection_frame, text="End Server", borderwidth=5, width=15,font=my_font, bg=red, state="disabled")

post_label.grid(row=0, column=0,padx=2, pady=10)
port_entry.grid(row=0, column=1,padx=2, pady=10)
start_button.grid(row=0, column=2,padx=5, pady=10)
end_button.grid(row=0, column=3,padx=5, pady=10)

history_scrollbar = tkinter.Scrollbar(history_frame,orient="vertical")
history_listbox = tkinter.Listbox(history_frame, height=10, width=55, borderwidth=3,
                                  font=my_font,bg=black,fg=red, yscrollcommand=history_scrollbar.set)
history_scrollbar.config(command=history_listbox.yview)

history_listbox.grid(row=0, column=0)
history_scrollbar.grid(row=0, column=0, sticky="ns")


client_scrollbar = tkinter.Scrollbar(client_frame,orient="vertical")
client_listbox = tkinter.Listbox(client_frame, height=10, width=55, borderwidth=3,
                                  font=my_font,bg=black,fg=red, yscrollcommand=client_scrollbar.set)
client_scrollbar.config(command=client_listbox.yview)


client_listbox.grid(row=0, column=0)
client_scrollbar.grid(row=0, column=0, sticky="ns")


input_entry = tkinter.Entry(message_frame, width=40, borderwidth=3, font=my_font)

self_broadcast_button = tkinter.Button(
    message_frame, text="Broadcast", width=13, borderwidth=5, font=my_font,bg=red,state="disabled")

input_entry.grid(row=0,column=0, padx=5, pady=5)
self_broadcast_button.grid(row=0,column=1, padx=5, pady=5)

message_button = tkinter.Button(
    admin_frame, text="PM", borderwidth=5, width=15, font=my_font, bg=red, state="disabled")
kick_button = tkinter.Button(
    admin_frame, text="Kick", borderwidth=5, width=15, font=my_font, bg=red, state="disabled")
ban_button = tkinter.Button(
    admin_frame, text="Ban", borderwidth=5, width=15, font=my_font, bg=red, state="disabled")

message_button.grid(row=0, column=0, padx=5, pady=5)
kick_button.grid(row=0, column=1, padx=5, pady=5)
ban_button.grid(row=0, column=2, padx=5, pady=5)

my_connection = Connection()
root.mainloop()