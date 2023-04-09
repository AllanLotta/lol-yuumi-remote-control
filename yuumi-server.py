import configparser
import keyboard
import pyautogui
import time
from flask import Flask, request

app = Flask(__name__)

# Read the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Get values from the config file
yuumi_server_ip = config.get('General', 'yuumi_server_ip')
yuumi_server_port = config.getint('General', 'yuumi_server_port')
yuumi_game_resolution = tuple(map(int, config.get('General', 'yuumi_game_resolution').split(', ')))
client_game_resolution = tuple(map(int, config.get('General', 'client_game_resolution').split(', ')))
yuumi_controls_key_press_duration = config.getfloat('General', 'yuumi_controls_key_press_duration')

# Duration for key presses
key_press_duration = yuumi_controls_key_press_duration

@app.route('/spell', methods=['POST'])
def handle_spell():
    global key_press_duration

    spell_action = request.json['action']
    valid_keys = [
        config.get('Keys', key) 
        for key in ['spell_q', 'spell_w', 'spell_e', 'spell_r', 'spell_d', 'spell_f', 'open_shop', 'tab_info', 'go_to_base', 'level_up_q', 'level_up_w', 'level_up_e', 'level_up_r']
    ]

    if spell_action in valid_keys:
        keyboard.press(spell_action)
        time.sleep(key_press_duration)
        keyboard.release(spell_action)
    else:
        return {'error': 'Invalid spell action'}, 400

    return {'success': True}

@app.route('/click', methods=['POST'])
def handle_click():
    global yuumi_game_resolution, client_game_resolution

    # Get the mouse coordinates from the request
    mouse_x = request.json['mouse_x']
    mouse_y = request.json['mouse_y']
    button = request.json['button']

    # Convert the mouse coordinates from main PC screen resolution to League of Legends game resolution
    game_x = int((mouse_x / client_game_resolution[0]) * yuumi_game_resolution[0])
    game_y = int((mouse_y / client_game_resolution[1]) * yuumi_game_resolution[1])

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
    if ability in [config.get('Keys', key) for key in ['level_up_q', 'level_up_w', 'level_up_e', 'level_up_r']]:
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
    app.run(host=yuumi_server_ip, port=yuumi_server_port, threaded=True)