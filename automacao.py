import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.3

# Obter a resolução atual da tela
screen_width, screen_height = pyautogui.size()

# Função para calcular coordenadas relativas
def calcular_coordenadas(x_relativo, y_relativo):
    x = int(screen_width * x_relativo)
    y = int(screen_height * y_relativo)
    return x, y

# Função para abrir o navegador (chrome)
def abrir_navegador():
    pyautogui.press("win")
    time.sleep(2)
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(3)

# Função para entrar no link
def entrar_link(link):
    time.sleep(2)
    pyautogui.write(link)
    pyautogui.press("enter")
    time.sleep(5)

# Função para fazer login
def fazer_login(email, senha):
    x, y = calcular_coordenadas(0.36, 0.46)  # Ajuste essas coordenadas conforme necessário
    pyautogui.click(x, y)
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)

# Função para cadastrar produtos
def cadastrar_produtos(tabela):
    for linha in tabela.index:
        x, y = calcular_coordenadas(0.355, 0.338)  # Ajuste essas coordenadas conforme necessário
        pyautogui.click(x, y)
        codigo = tabela.loc[linha, "codigo"]
        pyautogui.write(str(codigo))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "marca"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "tipo"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "categoria"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "custo"]))
        pyautogui.press("tab")
        obs = tabela.loc[linha, "obs"]
        if not pd.isna(obs):
            pyautogui.write(str(obs))
        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.scroll(5000)

# Passo 1: Entrar no sistema da empresa
abrir_navegador()
time.sleep(3)
entrar_link("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# Passo 2: Fazer login
fazer_login("pythonimpressionador@gmail.com", "123456")

# Passo 3: Importar a base de produtos pra cadastrar
tabela = pd.read_csv("produtos_aula1.csv")
print(tabela)

# Passo 4: Cadastrar um produto
cadastrar_produtos(tabela)
