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
        pass

def start_server(connection):
    pass

def end_server(connection):
    pass

def connect_client(connection):
    pass

def create_message(flag,name,message,colour):
    pass

def process_message(connection,message_json,client_socket,client_address=(0,0)):
    pass

def broadcast_message(connection,message_json):
    pass

def receive_message(connection, client_socket):
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
    connection_frame,text="Start Server", borderwidth=5, width=15,font=my_font, bg=red)
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


root.mainloop()