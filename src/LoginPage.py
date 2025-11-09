import PySimpleGUI as sg

# theme setup
my_theme = {
    'BACKGROUND': '#0b192f',
    'TEXT': '#0b192f',
    'INPUT': '#68e9d7',
    'TEXT_INPUT': '#000000',
    'SCROLL': '#c7e78b',
    'BUTTON': ('#0b192f', '#68e9d7'),
    'PROGRESS': ('#01826B', '#D0D0D0'),
    'BORDER': 0,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0,
}
if 'MyTheme' not in sg.theme_list():
    sg.theme_add_new('MyTheme', my_theme)
sg.theme('MyTheme')
#end theme

valid_credentials = {"user@example.com": "password123"}

def custom_popup(title, text, size=(400, 150)):
    popup_layout = [
        [sg.Text(text, font=('Calibri', 16), text_color='#68e9d7')],
        [sg.Button("OK", font=("Neue Haas Grotesk Dis...", 14),
                   button_color=('#0b192f', '#68e9d7'), border_width=0, size=(5, 1))]
    ]
    popup_window = sg.Window(title, popup_layout, element_justification='c', size=size)
    while True:
        event, _ = popup_window.read()
        if event in (sg.WIN_CLOSED, "OK"):
            break
    popup_window.close()

def validate_login(email, password):
    if email in valid_credentials and valid_credentials[email] == password:
        custom_popup("Login Successful", f"Welcome, {email}!", size=(500, 180))
        return True
    custom_popup("Login Failed", "Invalid email or password", size=(400, 150))
    return False

# --- CENTERED LAYOUT ---
center_block = [
    [sg.Text("PAKKJ", font=("Calibri", 36, "bold"),
             text_color="#68e9d7", background_color="#0b192f")],
    [sg.Text("Email ID:", size=(10, 1), font=("Calibri", 14),
             background_color="#0b192f", text_color="#68e9d7"),
     sg.InputText(key='email', size=(30, 1), font=("Arial", 14))],
    [sg.Text("Password:", size=(10, 1), font=("Calibri", 14),
             background_color="#0b192f", text_color="#68e9d7"),
     sg.InputText(key='password', size=(30, 1), password_char='*', font=("Arial", 14))],
    [sg.Button("LOGIN", size=(12, 1), font=("Neue Haas Grotesk Dis...", 14),
               button_color=('#0b192f', '#68e9d7'), border_width=0)]
]

layout = [
    [sg.VPush()],
    [sg.Column(
        center_block,
        background_color="#0b192f",
        element_justification="center",
        expand_x=True
    )],
    [sg.VPush()]
]

screen_width, screen_height = sg.Window.get_screen_size()
window = sg.Window(
    "Login Page",
    layout,
    size=(screen_width, screen_height),
    element_justification='center',
    background_color=sg.theme_background_color(),
    finalize=True
)

# --- EVENT LOOP ---
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "LOGIN":
        if validate_login(values['email'], values['password']):
            window.close()
            import BudgetApp
            BudgetApp.mainPage()
            break

window.close()
