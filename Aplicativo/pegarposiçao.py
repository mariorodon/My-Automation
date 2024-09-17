import pyautogui
from time import sleep

# Obtém a posição atual do mouse
sleep(1)
posicao_mouse = pyautogui.position()

# Exibe a posição do mouse
sleep(1)
print(f"A posição do mouse é: {posicao_mouse}")
