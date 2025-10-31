import tkinter, socket, threading, json
from tkinter import StringVar

root = tkinter.Tk()
root.title("Chat Client")
root.geometry("800x800")
root.resizable(False,False)

my_font = ("SimSun",14)
black = "#010101"
light_green = "#1fc742"
white = "#ffffff"
red = "#ff3855"
orange = "#ffaa1d"
yellow = "#fff700"
green = "#1fc742"
blue = "#5dadec"
purple = "#9c51b6"
root.config(bg=black)

class Connection:
    def __init__(self):
        self.encoder = "utf-8"
        self.byte_size = 1024

def connect(connection):
    my_listbox.delete(0,"end")
    connection.name = name_entry.get()
    connection.target_ip = ip_entry.get()
    connection.port = port_entry.get()
    connection.colour = colour.get()

    try:
        connection.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connection.client_socket.connect((connection.target_ip, int(connection.port)))

        message_json = connection.client_socket.recv(connection.byte_size)
        process_message(connection, message_json)

    except:
        my_listbox.insert(0,"Connection not established...")

def disconnect(connection):
    pass

def gui_start():
    pass

def gui_end():
    pass

def create_message(flag, name, message, colour):
    pass

def process_message(connection, message_json):
    pass

def send_message(connection):
    pass

def receive_message(connection):
    pass



info_frame = tkinter.Frame(root, bg=black)
colour_frame = tkinter.Frame(root, bg=black)
output_frame = tkinter.Frame(root, bg=black)
input_frame = tkinter.Frame(root,bg=black)

info_frame.pack()
colour_frame.pack()
output_frame.pack(pady=10)
input_frame.pack()

name_label = tkinter.Label(info_frame, text="Client Name: ", font=my_font, fg=light_green,bg=black)
name_entry = tkinter.Entry(info_frame,borderwidth=3, font=my_font)
ip_label = tkinter.Label(info_frame,text="Host IP:", font=my_font,fg=light_green,bg=black)
ip_entry = tkinter.Entry(info_frame,borderwidth=3,font=my_font)
port_label = tkinter.Label(info_frame, text="Port Num:", font=my_font, fg=light_green,bg=black)
port_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font, width=10)

connect_button = tkinter.Button(info_frame, text="Connect", font=my_font,bg=light_green, borderwidth=5, width=10,
                                command=lambda:connect(my_connection))
disconnect_button = tkinter.Button(info_frame, text="Disconnect", font=my_font,bg=light_green, borderwidth=5, width=10,
                                   state="disabled",command=disconnect)


colour = StringVar()
colour.set(white)

white_button = tkinter.Radiobutton(colour_frame,width=5, text="white",variable=colour, value=white,
                                   bg=black, fg=light_green,font=my_font)

red_button = tkinter.Radiobutton(colour_frame,width=5, text="red",variable=colour, value=red,
                                   bg=black, fg=light_green,font=my_font)

orange_button = tkinter.Radiobutton(colour_frame,width=5, text="orange",variable=colour, value=orange,
                                   bg=black, fg=light_green,font=my_font)

yellow_button = tkinter.Radiobutton(colour_frame,width=5, text="yellow",variable=colour, value=yellow,
                                   bg=black, fg=light_green,font=my_font)

green_button = tkinter.Radiobutton(colour_frame,width=5, text="green",variable=colour, value=green,
                                   bg=black, fg=light_green,font=my_font)

blue_button = tkinter.Radiobutton(colour_frame,width=5, text="blue",variable=colour, value=blue,
                                   bg=black, fg=light_green,font=my_font)

purple_button = tkinter.Radiobutton(colour_frame,width=5, text="purple",variable=colour, value=purple,
                                   bg=black, fg=light_green,font=my_font)

colour_buttons = [white_button,red_button,orange_button,yellow_button,green_button,blue_button,purple_button]

white_button.grid(row=1, column=0, padx=2, pady=2)
red_button.grid(row=1, column=1, padx=2, pady=2)
orange_button.grid(row=1, column=2, padx=2, pady=2)
yellow_button.grid(row=1, column=3, padx=2, pady=2)
green_button.grid(row=1, column=4, padx=2, pady=2)
blue_button.grid(row=1, column=5, padx=2, pady=2)
purple_button.grid(row=1, column=6, padx=2, pady=2)

name_label.grid(row=0, column=0, padx=2, pady=10)
name_entry.grid(row=0, column=1, padx=2, pady=10)
port_label.grid(row=0, column=2, padx=2, pady=10)
port_entry.grid(row=0, column=3, padx=2, pady=10)
ip_label.grid(row=1, column=0, padx=2, pady=5)
ip_entry.grid(row=1, column=1, padx=2, pady=5)
connect_button.grid(row=1, column=2, padx=4, pady=5)
disconnect_button.grid(row=1, column=3, padx=4, pady=5)

my_scrollbar = tkinter.Scrollbar(output_frame,orient="vertical")
my_listbox = tkinter.Listbox(output_frame,height=20, width=55,borderwidth=3,bg=black,fg=light_green,font=my_font,yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_listbox.yview)

my_listbox.grid(row=0,column=0)
my_scrollbar.grid(row=0, column=1,sticky="ns")

input_entry = tkinter.Entry(input_frame, width=45, borderwidth=3, font=my_font)
send_button = tkinter.Button(input_frame,text="send",borderwidth=5, width=10, font=my_font, bg=light_green, state="disabled")

input_entry.grid(row=0, column=0, padx=5, pady=5)
send_button.grid(row=0, column=1, padx=5, pady=5)

my_connection = Connection()

root.mainloop()