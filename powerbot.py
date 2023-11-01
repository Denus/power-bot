import subprocess
import pyttsx3
import time

def run_powershell_command(command):
    powershell_command = f'''
    $response = Invoke-Expression -Command "{command}"
    $response
    '''

    result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)
    return result.stdout

def chat_with_bot():
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Adjust the speech rate if needed

    print("Hello! I'm your friendly chatbot. You can ask me questions or have a conversation.")
    engine.say("Hello! I'm your friendly chatbot. You can ask me questions or have a conversation.")
    engine.runAndWait()

    while True:
        user_input = input("You: ")
        response = run_powershell_command(user_input)

        print("Bot:", response)
        engine.say(response)
        engine.runAndWait()

if __name__ == "__main__":
    chat_with_bot()
