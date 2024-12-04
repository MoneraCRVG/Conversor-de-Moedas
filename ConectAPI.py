import flet as ft

def main(page: ft.Page):
    # Função para realizar a conversão
    def convert_currency(e):
        try:
            reais = float(reais_input.value)
            dollars = reais / 5.0 
            result.value = f"USD {dollars:.2f}"
        except ValueError:
            result.value = "Por favor, insira um número válido"
        page.update()
    
    # Título
    page.title = "Conversor de Moeda (USD para BRL)"

    # Campo de entrada para BRL
    reais_input = ft.TextField(label="Valor em Dólares (USD)", width=200)

    # Botão para acionar a conversão
    convert_button = ft.ElevatedButton(text="Converter", on_click=convert_currency)

    # Texto para exibir o resultado
    result = ft.Text(value="BRL 0.00", size=20)

    # Adicionando componentes à página
    page.add(
        ft.Column(
            [
                ft.Text("Conversor de Moeda (BRL para USD)", size=30),
                reais_input,
                convert_button,
                result,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Executar o aplicativo
ft.app(target=main)