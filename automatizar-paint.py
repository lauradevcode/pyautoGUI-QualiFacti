import pyautogui
# configurar o tempo entra as açoes
pyautogui.PAUSE = 2.5
# Automatizar o meu teclado
# utilizar funcoes capazes de abrir o paint
pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.press("enter")
# Mover o mouse para a posição do botao 'lapis'
x, y = (404, 76)
# clicar no botao do lapis
pyautogui.click(x, y)
# pisicionar sobre a tela de desenho
pyautogui.moveTo(370, 152)
pyautogui.PAUSE = 2.0
distance = 300
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.5)  # mover para a direita
    distance -= 25
    pyautogui.dragRel(0, distance, duration=0.5)  # mover para baixo
    pyautogui.dragRel(-distance, 0, duration=0.5)  # mover para a esquerda
    distance -= 25
    pyautogui.dragRel(0, -distance, duration=0.5)  # mover para cima
