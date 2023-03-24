import keyboard
import pyautogui
from flask import Flask, request

app = Flask(__name__)

# Set the resolution of the League of Legends game on Windows PC
game_resolution = (1920, 1080)

@app.route('/spell', methods=['POST'])
def handle_spell():
    global game_resolution

    # Get the spell action from the request
    spell_action = request.json['action']

    # Press the corresponding spell key on the keyboard
    if spell_action == 'q':
        keyboard.press('q')
    elif spell_action == 'w':
        keyboard.press('w')
    elif spell_action == 'e':
        keyboard.press('e')
    elif spell_action == 'r':
        keyboard.press('r')
    elif spell_action == 'd':
        keyboard.press('d')
    elif spell_action == 'f':
        keyboard.press('f')
    else:
        return {'error': 'Invalid spell action'}, 400

    return {'success': True}


@app.route('/click', methods=['POST'])
def handle_click():
    global game_resolution

    # Get the mouse coordinates from the request
    mouse_x = request.json['mouse_x']
    mouse_y = request.json['mouse_y']

    # Convert the mouse coordinates from Mac screen resolution to Windows game resolution
    game_x = int((mouse_x / 1440) * game_resolution[0])
    game_y = int((mouse_y / 900) * game_resolution[1])

    # Move the mouse to the specified position and click
    pyautogui.moveTo(game_x, game_y)
    pyautogui.click()

    return {'success': True}


if __name__ == '__main__':
    app.run(port=8000)