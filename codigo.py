#waszap
#botão de iniciar chat
#popup para entrar no chat
#quando entrar no chat: (aparecer para todo mundo)
    #a mensagem que vc entrou no chat
    #o campo e o botão de enviar mens
#a cada mens que vc enviar (aparecer para todo mundo)
    # nome: texto da mens



# ft.app(target=main, view=ft.WEB_BROWSER) - para tranformar em um site
# target apontando qual é o main
# control + C para pausar terminal


import flet as ft

def main(pagina):
    texto = ft.Text("waszap")

    chat = ft.Column()

    nome_user = ft.TextField(label="Escreva seu nome")
    campo_mens = ft.TextField(label="Digite sua mensagem")
    botao_enviar_mens = ft.TextButton("Enviar")

    def entrar_modal(event):
        #fechar modal
        modal.open=False
        #remover botão iniciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        #criar campo de mens do user
        pagina.add(ft.Row(
            [campo_mens, botao_enviar_mens]
        ))
        #criar o botão de enviar mens do user
        pagina.update()

    modal = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao waszap"),
        content=nome_user,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_modal)],
        )
        

    def entrar_chat(evento):
        pagina.dialog = modal
        modal.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat",on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main)