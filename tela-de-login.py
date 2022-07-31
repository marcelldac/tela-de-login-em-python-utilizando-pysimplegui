from PySimpleGUI import PySimpleGUI as sg


sg.theme('Reddit')
layout = [  
    [sg.Text('User'),sg.Input(key='usuario')],
    [sg.Text('Pass'),sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Remember this?')],
    [sg.Button('Login')]
]


janela = sg.Window('Login', layout)


while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Login':
        if valores['usuario'] == 'Marcelldac' and valores['senha'] == 'marcelldac':
            print('Bem-vindo ao login')
        else:
            print('Você não é bem vindo')
    