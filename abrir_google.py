import pyautogui as abrirGoogle

abrirGoogle.sleep(4)
print(abrirGoogle.position())

abrirGoogle.moveTo(x=698, y=754)
abrirGoogle.click(x=698, y=754)

abrirGoogle.sleep(3)

abrirGoogle.typewrite('preco do dolar')
abrirGoogle.sleep(2)
abrirGoogle.press('enter')