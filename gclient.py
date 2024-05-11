import socket
import json

host = "127.0.0.1"
port = 7777

def play_game():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    data = s.recv(1024)
    print("\n== GuessingGameV2 ==\n")
    print(data.decode().strip())

    while True:
        user_input = input("Enter Here: ").strip()
        s.sendall(user_input.encode())
        
        print()
        reply = s.recv(1024).decode().strip()
        
        if "Correct" in reply:
            print(reply)
            s.close()  
            return
        
        print(reply)

def load_user_data():
    try:
        with open("users.json", 'r') as file:
            data = file.read()
            if data:
                return json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return {}

while True:
    play_game()
    repeat = input("\nWant to play another round? (y/n): ").strip().lower()
    if repeat != 'y':
        user_data = load_user_data()
        print("\n== Loaded User Data ==\n")
        sorted_user_data = sorted(user_data.items(), key=lambda x: (x[1]['difficulty'], x[1]['score']), reverse=True)
        for key, value in sorted_user_data:
            print(f"Player: {key}")
            print(f"Difficulty: {value['difficulty']}")
            print(f"Score: {value['score']}")
            print(f"tries: {value['tries']}\n")
        break
