import turtle
import pandas


def scrivi_regione(dato):
    t = turtle.Turtle()
    t.hideturtle()
    t.up()
    regioni_data = data[data.Regione == dato]
    t.goto(int(regioni_data.x), int(regioni_data.y))
    t.write(dato, align='center', font=("Arial", 14, "normal"))


screen = turtle.Screen()
screen.title('Indovina le Regioni')
screen.setup(1000, 900)

image = 'italia.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('regioni.csv')
regioni_list = data.Regione.to_list()
regioni_indovinate = []

# # prendo le coordinate al click del mouse
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


while len(regioni_indovinate) < 20:
    risposta = screen.textinput(title=f'{len(regioni_indovinate)}/20 Regioni corrette',
                                prompt="Quale regione manca?").title()

    if risposta == 'Esci':
        regioni_mancanti = []
        for regione in regioni_list:
            if regione not in regioni_indovinate:
                regioni_mancanti.append(regione)

        new_data = pandas.DataFrame(regioni_mancanti)
        new_data.to_csv('regioni da studiare.csv')

        break

    if risposta == 'Soluzione':
        for regione in regioni_list:
            scrivi_regione(regione)

        screen.exitonclick()

    if risposta in regioni_list:
        regioni_indovinate.append(risposta)
        scrivi_regione(risposta)
