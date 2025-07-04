import flet as ft
import httpx

async def main(page: ft.Page):
    page.title = "Jonggod Support App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # FastAPIからのメッセージを表示するテキスト
    fastapi_message_text = ft.Text("Loading message from FastAPI...")

    async def get_fastapi_message(e):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get("http://127.0.0.1:8000/")
                if response.status_code == 200:
                    fastapi_message_text.value = f"Message from FastAPI: {response.json()['message']}"
                else:
                    fastapi_message_text.value = f"Error from FastAPI: {response.status_code}"
        except httpx.RequestError as exc:
            fastapi_message_text.value = f"HTTP Request Error: {exc}"
        page.update()

    page.add(
        ft.Column(
            [
                ft.Text("Hello from Flet!", size=30),
                fastapi_message_text,
                ft.ElevatedButton("Get Message from FastAPI", on_click=get_fastapi_message),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    # アプリケーション起動時に一度メッセージを取得
    await get_fastapi_message(None)


if __name__ == "__main__":
    ft.app(target=main)
