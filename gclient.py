import socket
import random 

host = "0.0.0.0"
port = 7777
banner = """
== Guessing Game v1.0 ==
Choose the difficulty level:
a. Easy (1-50)
b. Medium (1-100)
c. Hard (1-500)
Enter your choice:"""

def generate_random_int(difficulty):
    if difficulty == 'a':
        return random.randint(1, 50)
    elif difficulty == 'b':
        return random.randint(1, 100)
    elif difficulty == 'c':
        return random.randint(1, 500)

# Initialize the socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

print(f"server is listening in port {port}")

while True:
    guessme = 0
    conn = None
    while True:
        if conn is None:
            print("waiting for connection..")
            conn, addr = s.accept()
            print(f"new client: {addr[0]}")
        conn.sendall(banner.encode())
        client_input = conn.recv(1024)
        difficulty = client_input.decode().strip()
        guessme = generate_random_int(difficulty)
        print(f"Selected difficulty: {difficulty}")
        conn.sendall(b"Let's start guessing!\nEnter your guess: ")

        while True:
            client_input = conn.recv(1024)
            guess = int(client_input.decode().strip())
            print(f"User guess attempt: {guess}")
            if guess == guessme:
                conn.sendall(b"Correct Answer!")
                break
            elif guess > guessme:
                conn.sendall(b"Guess Lower!\nEnter guess: ")
            elif guess < guessme:
                conn.sendall(b"Guess Higher!\nEnter guess:")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

s.close()
