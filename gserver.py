import socket

host = "localhost"
port = 7777

def play_game(s):
    while True:
        try:
            # received the banner
            data = s.recv(1024)
            # print banner
            print(data.decode().strip())

            # Ask the user to choose the difficulty level
            difficulty = input("Choose the difficulty level (a/b/c): ").strip()
            s.sendall(difficulty.encode())

            while True:
                # Get the user's guess input
                user_input = input("").strip()

                s.sendall(user_input.encode())
                reply = s.recv(1024).decode().strip()
                if "Correct" in reply:
                    print(reply)
                    break
                print(reply)
                continue
            
            play_again = input("Do you want to choose difficulty and play again? (yes/no): ").lower()
            if play_again != 'yes':
                break

        except ConnectionAbortedError:
            print("Connection closed by server.")
            break

# initialize the socket object
s = socket.socket()
s.connect((host, port))


while True:
    play_game(s)
    play_again = input("Ya sure? (yes/no): ").lower()
    if play_again == 'yes':
        break
    
s.close()
