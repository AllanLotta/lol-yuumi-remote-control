import keyboard
import pyautogui
import time
from flask import Flask, request

app = Flask(__name__)

# Set the resolutions of the League of Legends on the Yuumi PC and the main PC
game_resolution = (3840, 2160)
main_pc_resolution = (5120, 2880)

# Duration for key presses
key_press_duration = 0.15

@app.route('/spell', methods=['POST'])
def handle_spell():
    global key_press_duration

    spell_action = request.json['action']

    if spell_action in ['q', 'w', 'e', 'r', 'd', 'f']:
        keyboard.press(spell_action)
        time.sleep(key_press_duration)
        keyboard.release(spell_action)
    else:
        return {'error': 'Invalid spell action'}, 400

    return {'success': True}

@app.route('/click', methods=['POST'])
def handle_click():
    global game_resolution, main_pc_resolution

    # Get the mouse coordinates from the request
    mouse_x = request.json['mouse_x']
    mouse_y = request.json['mouse_y']
    button = request.json['button']

    # Convert the mouse coordinates from main PC screen resolution to League of Legends game resolution
    game_x = int((mouse_x / main_pc_resolution[0]) * game_resolution[0])
    game_y = int((mouse_y / main_pc_resolution[1]) * game_resolution[1])

    # Move the mouse to the specified position and click
    pyautogui.moveTo(game_x, game_y)
    if button == 'left':
        pyautogui.click()
    elif button == 'right':
        pyautogui.rightClick()
    else:
        return {'error': 'Invalid mouse button'}, 400
    return {'success': True}

@app.route('/level', methods=['POST'])
def handle_level():
    global key_press_duration

    ability = request.json['ability']
    print('Leveling up ability')
    print(ability)
    if ability in ['h', 'j', 'k', 'l']:
        print(f'Leveling up {ability.upper()}')
        keyboard.press(ability)
        time.sleep(key_press_duration)
        keyboard.release(ability)
    else:
        return {'error': 'Invalid ability'}, 400

    return {'success': True}

@app.route('/connect', methods=['GET'])
def handle_connect():
    return {'success': True}

if __name__ == '__main__':
    app.run(host='192.168.0.4', port=8000, threaded=True)
