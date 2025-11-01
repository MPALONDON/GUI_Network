import json
import tkinter,socket,threading
from datetime import datetime

root = tkinter.Tk()
root.title("Chat Server")
root.geometry("800x800")
root.resizable(False,False)

my_font = ("SimSun",14)
cream = "#FDFBD4"
caramel = "#D89549"
black = "#000000"
root.iconbitmap("./favicon/Web_.ico")
root.config(bg=cream)

def date_format():
    today_date = datetime.today()
    format_date = today_date.strftime("%d-%m-%Y %I:%M%p")
    return format_date

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
    history_listbox.insert(0,f"{date_format()} Server started on port {connection.port}")
    end_button.config(state="normal")
    self_broadcast_button.config(state="normal")
    message_button.config(state="normal")
    kick_button.config(state="normal")
    ban_button.config(state="normal")
    start_button.config(state="disabled")

    threading.Thread(target=connect_client, args=(connection,)).start()


def end_server(connection):
    message_packet = create_message(flag = "DISCONNECT", name = "ADMIN (broadcast)",
                                    message = "Server is closing...", colour = caramel, date = date_format())
    message_json = json.dumps(message_packet)
    broadcast_message(connection,message_json.encode(connection.encoder))

    history_listbox.insert(0,f"Server started on port {connection.port}")
    end_button.config(state="disabled")
    self_broadcast_button.config(state="disabled")
    message_button.config(state="disabled")
    kick_button.config(state="disabled")
    ban_button.config(state="disabled")
    start_button.config(state="normal")

    connection.server_socket.close()


def connect_client(connection):
    while True:
        try:
            client_socket, client_address = connection.server_socket.accept()
            if client_address[0] in connection.banned_ips:
                message_packet = create_message(flag = "DISCONNECT", name = "ADMIN (private)",
                                                message = "You have been banned...", colour=caramel, date = date_format())
                message_json = json.dumps(message_packet)
                client_socket.send(message_json.encode(connection.encoder))
                client_socket.close()
            else:
                message_packet = create_message(flag = "INFO", name = "ADMIN (private)",
                                                message = "Please send your name...", colour=caramel, date = date_format())
                message_json = json.dumps(message_packet)
                client_socket.send(message_json.encode(connection.encoder))
                message_json = client_socket.recv(connection.byte_size)
                process_message(connection,message_json,client_socket,client_address)

        except:
            break


def create_message(flag,name,message,colour, date):
    message_packet = {
        "flag": flag,
        "name": name,
        "message": message,
        "colour": colour,
        "date" : date
    }
    return message_packet

def process_message(connection,message_json,client_socket,client_address=(0,0)):
    message_packet = json.loads(message_json)
    flag = message_packet["flag"]
    name = message_packet["name"]
    message = message_packet["message"]
    colour = message_packet["colour"]
    date = message_packet["date"]

    if flag == "INFO":
        connection.client_sockets.append(client_socket)
        connection.client_ips.append(client_address[0])
        message_packet = create_message(flag = "MESSAGE", name = "ADMIN (broadcast)",
                                        message = f"{name} has joined the server!!!", colour = caramel, date = date_format())
        message_json = json.dumps(message_packet)
        broadcast_message(connection,message_json.encode(connection.encoder))
        client_listbox.insert("end",f"{date} Name: {name}  IP ADDR: {client_address[0]}")
        threading.Thread(target = receive_message, args=(connection,client_socket,)).start()

    elif flag == "MESSAGE":
        broadcast_message(connection, message_json)

        history_listbox.insert(0, f"{date} {name}: {message}")
        history_listbox.itemconfig(0, fg=colour)

    elif flag == "DISCONNECT":
        index = connection.client_sockets.index(client_socket)
        connection.client_sockets.remove(client_socket)
        connection.client_ips.pop(index)
        client_listbox.delete(index,"end")
        client_socket.close()
        message_packet = create_message(
            flag = "MESSAGE",name = "ADMIN (broadcast)",message = f"{name}: has left the server...", colour = caramel, date = date_format())
        message_json = json.dumps(message_packet)
        broadcast_message(connection = connection,message_json = message_json.encode(connection.encoder))
        history_listbox.insert(0, f"{date} ADMIN (broadcast): {name} has left the server...")

    else:
        history_listbox.insert(0, "Error processing message...")

def broadcast_message(connection,message_json):
    for client_socket in connection.client_sockets:
        client_socket.send(message_json)

def receive_message(connection, client_socket):
    while True:
        try:
            message_json = client_socket.recv(connection.byte_size)
            process_message(
                connection = connection,message_json = message_json,client_socket = client_socket)
        except:
            break

def self_broadcast(connection):
    message_packet = create_message(
            flag = "MESSAGE",name = "ADMIN (broadcast)",message = input_entry.get(), colour = caramel, date = date_format())
    message_json = json.dumps(message_packet)
    broadcast_message(connection = connection,message_json = message_json.encode(connection.encoder))
    input_entry.delete(0,"end")

def private_message(connection):
    index = client_listbox.curselection()[0]
    client_socket = connection.client_sockets[index]
    message_packet = create_message(
            flag = "MESSAGE",name = "ADMIN (private)",message = input_entry.get(), colour = caramel, date = date_format())
    message_json = json.dumps(message_packet)
    client_socket.send(message_json.encode(connection.encoder))
    input_entry.delete(0,"end")

def kick_client(connection):
    index = client_listbox.curselection()[0]
    client_socket = connection.client_sockets[index]
    message_packet = create_message(
            flag = "DISCONNECT",name = "ADMIN (private)",message = "You have been kicked...", colour = caramel, date = date_format())
    message_json = json.dumps(message_packet)
    client_socket.send(message_json.encode(connection.encoder))

def ban_client(connection):
    index = client_listbox.curselection()[0]
    client_socket = connection.client_sockets[index]
    message_packet = create_message(
            flag = "DISCONNECT",name = "ADMIN (private)",message = "You have been banned...", colour = caramel, date = date_format())
    message_json = json.dumps(message_packet)
    client_socket.send(message_json.encode(connection.encoder))
    connection.banned_ips.append(connection.client_ips[index])


connection_frame = tkinter.Frame(root, bg=cream)
history_frame = tkinter.Frame(root, bg=cream)
client_frame = tkinter.Frame(root, bg=cream)
message_frame = tkinter.Frame(root, bg=cream)
admin_frame = tkinter.Frame(root, bg=cream)

connection_frame.pack(pady=5)
history_frame.pack()
client_frame.pack(pady=5)
message_frame.pack()
admin_frame.pack()

post_label = tkinter.Label(
    connection_frame, text="Port Number:",font=my_font, bg=cream, fg=black)
port_entry = tkinter.Entry(
    connection_frame,width=10, borderwidth=3, font=my_font)
start_button = tkinter.Button(
    connection_frame,text="Start Server", borderwidth=5, width=15,font=my_font, bg=caramel, command=lambda:start_server(my_connection))
end_button = tkinter.Button(
    connection_frame, text="End Server", borderwidth=5, width=15,font=my_font, bg=caramel, state="disabled", command=lambda:end_server(my_connection))

post_label.grid(row=0, column=0,padx=2, pady=10)
port_entry.grid(row=0, column=1,padx=2, pady=10)
start_button.grid(row=0, column=2,padx=5, pady=10)
end_button.grid(row=0, column=3,padx=5, pady=10)

history_scrollbar = tkinter.Scrollbar(history_frame,orient="vertical")
history_listbox = tkinter.Listbox(history_frame, height=10, width=55, borderwidth=3,
                                  font=my_font, bg=black, fg=caramel, yscrollcommand=history_scrollbar.set, )
history_scrollbar.config(command=history_listbox.yview)

history_listbox.grid(row=0, column=0)
history_scrollbar.grid(row=0, column=0, sticky="ns")


client_scrollbar = tkinter.Scrollbar(client_frame,orient="vertical")
client_listbox = tkinter.Listbox(client_frame, height=10, width=55, borderwidth=3,
                                 font=my_font, bg=black, fg=caramel, yscrollcommand=client_scrollbar.set)
client_scrollbar.config(command=client_listbox.yview)


client_listbox.grid(row=0, column=0)
client_scrollbar.grid(row=0, column=0, sticky="ns")


input_entry = tkinter.Entry(message_frame, width=40, borderwidth=3, font=my_font)

self_broadcast_button = tkinter.Button(
    message_frame, text="Broadcast", width=13, borderwidth=5, font=my_font,bg=caramel,state="disabled", command=lambda:self_broadcast(my_connection))

input_entry.grid(row=0,column=0, padx=5, pady=5)
self_broadcast_button.grid(row=0,column=1, padx=5, pady=5)

message_button = tkinter.Button(
    admin_frame, text="PM", borderwidth=5, width=15, font=my_font, bg=caramel, state="disabled", command=lambda:private_message(my_connection))
kick_button = tkinter.Button(
    admin_frame, text="Kick", borderwidth=5, width=15, font=my_font, bg=caramel, state="disabled", command = lambda: kick_client(my_connection))
ban_button = tkinter.Button(
    admin_frame, text="Ban", borderwidth=5, width=15, font=my_font, bg=caramel, state="disabled", command = lambda: ban_client(my_connection))

message_button.grid(row=0, column=0, padx=5, pady=5)
kick_button.grid(row=0, column=1, padx=5, pady=5)
ban_button.grid(row=0, column=2, padx=5, pady=5)

my_connection = Connection()
root.mainloop()