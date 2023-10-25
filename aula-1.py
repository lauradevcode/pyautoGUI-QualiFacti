import pyautogui

# Retorna as coordenadas x e y atuais do cursor do mouse

pyautogui.hotkey("win","r")
pyautogui.write("mspaint")
pyautogui.press("enter")
x, y = pyautogui.position()
# Imprime as coordenadas do cursor do mouse
print(x, y)
