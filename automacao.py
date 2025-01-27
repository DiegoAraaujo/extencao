import pandas as pd
import pyautogui as pt

df = pd.read_csv('dados_formulario.csv')


pt.press("winleft")
pt.write("chrome")
