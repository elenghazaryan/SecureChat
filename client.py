from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import rle
import caesar

is_name: bool = True
msg_count: int = 0


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZE).decode("utf8")
            global msg_count
            last_index: int = msg.find(":") + 2
            name = msg[:last_index]
            message = msg[last_index:]
            if msg_count >= 2:
                message = rle.decompress(message)
                print(message)
                message = caesar.decode(message, 3)
                print(message)
            else:
                msg_count += 1
            msg_list.insert(tkinter.END, name + message)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    quit_msg = msg
    global is_name

    if not is_name:
        msg = caesar.encode(msg, 3)
        print(msg)
        msg = rle.compress(msg)
        print(msg)
    else:
        is_name = False
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if quit_msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()


top = tkinter.Tk()
top.title("Chat")

messages_frame = tkinter.Frame(top)  # create a frame for holding the list of messages
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("You can type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=70, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
''' The fill option tells the manager that the widget wants fill the entire space assigned to it. 
The value controls how to fill the space; BOTH means that the widget should expand both horisontally and vertically, 
X means that it should expand only horisontally, and Y means that it should expand only vertically.'''
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)  # create the input field for the user to input their message,
# and bind it to the string variable defined above
entry_field.bind("<Return>", send)  # also bind it to the send() function
# so that whenever the user presses return, the message is sent to the server
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)  # create the send button
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

# ----Now comes the sockets part----
HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33010
else:
    PORT = int(PORT)

BUFSIZE = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # Starts GUI execution.
