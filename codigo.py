#waszap
#botão de iniciar chat
#popup para entrar no chat
#quando entrar no chat: (aparecer para todo mundo)
    #a mensagem que vc entrou no chat
    #o campo e o botão de enviar mens
#a cada mens que vc enviar (aparecer para todo mundo)
    # nome: texto da mens



# ft.app(target=main) - para abri como um app
# target apontando qual é o main
# control + C para pausar terminal
# pubsub - um tunel de inf


import flet as ft

def main(pagina):
    texto = ft.Text("waszap")

    chat = ft.Column()

    nome_user = ft.TextField(label="Escreva seu nome")

    def enviar_mens_global(mensagem):
        texto_mens = mensagem["texto"]
        user_mens = mensagem["user"]
        #add mens no chat
        chat.controls.append(ft.Text(f"{user_mens}: {texto_mens}"))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mens_global)

    def enviar_mens(event):
        pagina.pubsub.send_all({"texto":campo_mens.value, "user": nome_user.value})

        #limpar chat
        campo_mens.value = ""
        pagina.update()

    campo_mens = ft.TextField(label="Digite sua mensagem")
    botão_enviar_mens = ft.TextButton("Enviar", on_click=enviar_mens)

    def entrar_modal(event):
        #abrir chat
        pagina.add(chat)
        #fechar modal
        modal.open=False
        #remover botão iniciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        #criar campo de mens do user
        #criar o botão de enviar mens do user
        pagina.add(ft.Row(
            [campo_mens, botão_enviar_mens]
        ))
        
        pagina.add(botão_enviar_mens)
        pagina.update()

    modal = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao waszap"),
        content=nome_user,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_modal)],
        )
        

    def entrar_chat(event):
        pagina.dialog = modal
        modal.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat",on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER)