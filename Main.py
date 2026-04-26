# passo a passo da automação
# 1 entrar no sistema/site da empresa
# 2 fazer login
# 3 importar a base de dados
# 4 cadastrar um produto
# 5 repetir o processo 4

import pyautogui
import time
pyautogui.PAUSE = 0.5

# Passo 1: entrar no sistema
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
# declaração da variavel "link"
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# Passo 2: fazer login
pyautogui.click(x=899, y=466)
pyautogui.write("projetodeautomação@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Passo 3: importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")

# Passo 4: cadastrar um produto
for linha in tabela.index:

    pyautogui.click(x=926, y=320)
    codigo = str(tabela.loc[linha,"codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab"
                    )
    marca = str(tabela.loc[linha,"marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
    

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# Passo 5: repetir o processo ate o fim