import flet as ft

def main(page: ft.Page):
    page.vertical_alignment= ft.MainAxisAlignment.START
    page.bgcolor= "#ffffff"
    page.window.width = 1200
    page.window.height = 650
    page.window_center()
    page.padding = 0
    page.window_resizable = False
    page.window_title_bar_buttons_hidden = True
    
    c1= ft.Container(bgcolor="#000000", width=200, height= 650, padding= 10,
                    content= ft.Column([

                        ft.Row ([
                        ft.IconButton(ft.icons.HOME, icon_color= "#ffffff"),
                        ft.Text("Inicio", color= "#ffffff", size=15)
                    ]),

                        ft.Row ([
                        ft.IconButton(ft.icons.SUPERVISED_USER_CIRCLE, icon_color= "#ffffff"),
                        ft.Text("Alunos", color= "#ffffff", size=15)
                    ]),
                
                        ft.Row ([
                        ft.IconButton(ft.icons.CLASS_, icon_color= "#ffffff"),
                        ft.Text("Turmas", color = "#ffffff", size=15)
                    ]),
                    
                        ft.Row ([
                        ft.IconButton(ft.icons.SUBJECT, icon_color= "#ffffff"),
                        ft.Text("Disciplinas", color = "#ffffff", size=15)
                    ]),

                        ft.Row ([
                        ft.IconButton(ft.icons.DISABLED_VISIBLE_OUTLINED, icon_color= "#ffffff"),
                        ft.Text("Alunos desativados", color = "#ffffff", size=15)
                    ]),

                        ft.Row ([
                        ft.IconButton(ft.icons.SEND, icon_color= "#ffffff"),
                        ft.Text("Enviar notificações", color = "#ffffff", size=15)
                    ]),



                    ft.Container (height= 150),

                    ft.Divider (color= "#ffffff"),


                        ft.Row ([
                        ft.IconButton(ft.icons.EXIT_TO_APP, icon_color= "#ffffff", icon_size= 30, on_click= lambda e: sair(e)),
                        ft.Text("Sair", color = "#ffffff", size=15)
                    ])
                ])
            
                    
            )
    
def sair (e):
    page.window_class()
    page.update()


    page.add(c1)
ft.app(main)
