import flet
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    UserControl,
    border_radius,
    colors,
    ButtonStyle,
    CircleBorder,
    FontWeight
)

class CalcApp(UserControl):
        def reset (self):
            self.operador = "+"
            self.operando1 = 0 
            self.new_operand = True

        def build(self):
            self.reset()
            self.result = Text(value="0", size=30, italic=True, weight=FontWeight.BOLD , color=colors.PURPLE_100)
            self.monito = Text(value="☝️🤓", size=30)

            return Container(
                width=350,
                bgcolor=colors.BLACK,
                border_radius=border_radius.all(20),
                padding=20,
                content=Column(
                    controls=[
                        Row(controls=[self.monito, self.result], alignment="end"),
                        Row(
                            controls=[
                                ElevatedButton(
                                    text="AC",
                                    bgcolor=colors.DEEP_PURPLE_300,
                                    color=colors.BLACK,
                                    on_click=self.button_clicked,
                                    data="AC",
                                    expand=1, #hace mas largo el boton
                                    ),
                                ElevatedButton(
                                    text="+/-",
                                    bgcolor=colors.DEEP_PURPLE_300,
                                    color=colors.BLACK,
                                    on_click=self.button_clicked,
                                    data="+/-",
                                    expand=1 #hace mas largo el boton
                                    ),
                                ElevatedButton(
                                    text="%",
                                    bgcolor=colors.DEEP_PURPLE_300,
                                    color=colors.BLACK,
                                    on_click=self.button_clicked,
                                    data="%",
                                    expand=1 #hace mas largo el boton
                                    ),
                                ElevatedButton(
                                    text="/",
                                    bgcolor=colors.PURPLE_ACCENT_400,
                                    color=colors.BLACK,
                                    on_click=self.button_clicked,
                                    data="/",
                                    expand=1 #hace mas largo el boton
                                    )
                            ]
                        ),
                        Row(
                            controls=[
                                ElevatedButton(
                                    text="7",
                                    on_click=self.button_clicked,
                                    data="7",
                                    style=ButtonStyle(shape=CircleBorder(), padding=25)
                                    ),
                                ElevatedButton(
                                    text="8",
                                    on_click=self.button_clicked,
                                    data="8",
                                    style=ButtonStyle(shape=CircleBorder(), padding=25)
                                    ),
                                ElevatedButton(
                                    text="9",
                                    on_click=self.button_clicked,
                                    data="9",
                                    style=ButtonStyle(shape=CircleBorder(), padding=25)
                                    ),
                                ElevatedButton(
                                    text="*",
                                    bgcolor=colors.PURPLE_ACCENT_400,
                                    color=colors.BLACK,
                                    on_click=self.button_clicked,
                                    data="*",
                                    expand=1 #hace mas largo el boton
                                    ),
                            ]
                        ),
                        Row(
                            controls=[
                                ElevatedButton(
                                    text="4",
                                    on_click=self.button_clicked,
                                    data="4",
                                    style=ButtonStyle(shape=CircleBorder(), padding=25)
                                    ),
                                ElevatedButton(
                                    text="5",
                                    on_click=self.button_clicked,
                                    data="5",
                                    style=ButtonStyle(shape=CircleBorder(), padding=25)
                                    ),
                                ElevatedButton(
                                    text="6",
                                    on_click=self.button_clicked,
                                    data="6",
                                    style=ButtonStyle(shape=CircleBorder(), padding=25)
                                    ),
                                ElevatedButton(
                                    text="-",
                                    bgcolor=colors.PURPLE_ACCENT_400,
                                    color=colors.BLACK,
                                    on_click=self.button_clicked,
                                    data="-",
                                    expand=1 #hace mas largo el boton
                                    ),
                            ]
                        ),
                        Row(
                            controls=[
                                ElevatedButton(
                                    text="1",
                                    on_click=self.button_clicked,
                                    data="1",
                                    style=ButtonStyle(shape=CircleBorder(), padding=25)
                                    ),
                                ElevatedButton(
                                    text="2",
                                    on_click=self.button_clicked,
                                    data="2",
                                    style=ButtonStyle(shape=CircleBorder(), padding=25)
                                    ),
                                ElevatedButton(
                                    text="3",
                                    on_click=self.button_clicked,
                                    data="3",
                                    style=ButtonStyle(shape=CircleBorder(), padding=25)
                                    ),
                                ElevatedButton(
                                    text="+",
                                    bgcolor=colors.PURPLE_ACCENT_400,
                                    color=colors.BLACK,
                                    on_click=self.button_clicked,
                                    data="+",
                                    expand=1 #hace mas largo el boton
                                    ),
                            ]
                        ),
                        Row(
                            controls=[
                                ElevatedButton(
                                    text="0",
                                    on_click=self.button_clicked,
                                    data="0",
                                    style=ButtonStyle(shape=CircleBorder(), padding=25)
                                    ),
                                ElevatedButton(
                                    text=".",
                                    on_click=self.button_clicked,
                                    data=".",
                                    style=ButtonStyle(shape=CircleBorder(), padding=25)
                                    ),
                                ElevatedButton(
                                    text="=",
                                    bgcolor=colors.PURPLE_ACCENT_400,
                                    color=colors.BLACK,
                                    on_click=self.button_clicked,
                                    data="=",
                                    expand=2 #hace mas largo el boton
                                    ),
                            ]
                        )
                    ]
            )
        )

        def button_clicked(self, e):
                data = e.control.data
                if self.result.value == "Error" or data == "AC":
                    self.result.value = "0"
                    self.reset()

                elif data in ("1","2","3","4","5","6","7","8","9","0",".",):
                    if self.result.value == "0" or self.new_operand == True:
                        self.result.value = data
                        self.new_operand = False
                    else:
                        self.result.value += data

                elif data  in ("+","-","*","/"):
                    self.result.value = self.calcular(
                        self.operando1, float(self.result.value), self.operador
                    )
                    self.operador = data
                    if self.result.value == "Error":
                        self.operando1 = "0"
                    else:
                        self.operando1 = float(self.result.value)
                    self.new_operand = True
                
                elif data in ("="):
                    self.result.value = self.calcular(
                        self.operando1, float(self.result.value), self.operador
                    )
                    self.reset()

                elif data in ("%"):
                    self.result.value = float(self.result.value) / 100
                    self.reset()
                
                elif data in ("+/-"):
                    if float(self.result.value) > 0:
                        self.result.value = "-" + str(self.result.value)

                    elif float(self.result.value) < 0:
                        self.result.value = str(
                            self.format_number(abs(float(self.result.value)))
                        )
                self.update()

        def format_number(self, num):
            if num % 1 == 0:
                return int(num)
            else:
                return num

        def calcular(self, operando1, operando2, operador):
            
            if operador == "+":
                return self.format_number(operando1 + operando2)
            
            elif operador == "-":
                return self.format_number(operando1 - operando2)
            
            elif operador == "*":
                return self.format_number(operando1 * operando2)
            
            elif operador == "/":
                if operando2 == 0:
                    return "Error"
                else:
                    return self.format_number(operando1 / operando2)

def main(page: flet.page):
    page.title = "Mi primera calculadora ☝️🤓"

    page.window_width = 400

    page.window_height = 450

    calc = CalcApp()

    page.add(calc)


flet.app(target=main)