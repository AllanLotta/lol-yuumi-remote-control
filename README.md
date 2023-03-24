# League of Legends Yuumi Controller - In development...

This is a tool that allows you to control Yuumi, a champion from the game League of Legends, from a separate computer while you control your main champion on your primary computer. Yuumi is a unique champion that can attach herself to other champions, making her an ideal candidate for this type of control.

## Requirements

- Python 3.x
- Flask
- keyboard
- pyautogui

## Installation

1. Install Python 3.x on both your primary computer and your Yuumi controller computer.
2. Install the required Python packages by running the following command in your terminal:
pip install flask keyboard pyautogui


3. Download the files from this repository onto both computers.
4. On your Yuumi controller computer, navigate to the `yuumi_server` folder and run the following command in your terminal:

    $python yuumi_server.py

5. On your primary computer, navigate to the `main_pc` folder and run the following command in your terminal:

    $python yuumi_controller.py


6. Follow the instructions in the terminal to set up the connection between the two computers.

## How to Use

1. Launch League of Legends on your primary computer.
2. Choose your main champion and begin playing normally.
3. When you want to control Yuumi, press and hold the alt key on your primary computer. This will activate the Yuumi controller on your Yuumi controller computer.
4. Move your mouse on your primary computer to where you want Yuumi to go and click the right mouse button. Yuumi will move to that location.
5. Release the alt key on your primary computer to return control to your main champion.



   
