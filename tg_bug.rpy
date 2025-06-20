init python:
    import requests
    import json

    # Настройки Telegram бота
    TELEGRAM_TOKEN = "ВАШ-ТОКЕН-БОТА"
    TELEGRAM_CHAT_ID = "ВАШ-ЧАТ-АЙДИ"

    def send_to_telegram(message):
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "Markdown"
        }
        try:
            response = requests.post(url, json=payload)
            return response.status_code == 200
        except:
            return False

screen bug_report_screen():
    modal True
    zorder 200

    default bug_text = ""

    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 400
        padding (30, 30)
        background "#000a"
        
        vbox:
            spacing 25
            xalign 0.5
            text "🐛 {size=+10}Сообщение об ошибке{/size}" style "bug_title" xalign 0.5
            hbox:
                spacing 15
                text "📝" size 30
                input:
                    value ScreenVariableInputValue("bug_text")
                    length 500
                    xsize 600
                    ysize 150
                    style "bug_input"
            hbox:
                xalign 0.5
                spacing 50
                
                textbutton "📤 Отправить":
                    style "bug_button"
                    action [
                        Function(send_to_telegram, f"*BUG REPORT*\n\n{bug_text}"),
                        Hide("bug_report_screen"),
                        Notify("✅ Сообщение отправлено!")
                    ]
                    
                textbutton "❌ Отмена":
                    style "bug_button_cancel"
                    action Hide("bug_report_screen")

screen bug_button():
    textbutton "🐛":
        style "bug_emoji_button"
        action Show("bug_report_screen")
        align (1.0, 0.0)
        offset (-30, 30)

init -1:
    # Стили для кнопок и элементов
    style bug_title:
        color "#fff"
        outlines [(2, "#000", 0, 0)]
        text_align 0.5
        
    style bug_input:
        background "#fff"
        color "#ffffff"
        selected_color "#000"
        size 24
        padding (10, 10)
        
    style bug_button:
        background "#4caf50"
        hover_background "#66bb6a"
        padding (25, 10)
        color "#fff"
        bold True
        size 28
        
    style bug_button_cancel:
        background "#f44336"
        hover_background "#ef5350"
        padding (25, 10)
        color "#fff"
        bold True
        size 28
        
    style bug_emoji_button:
        background "#0000"
        hover_background "#fff3"
        padding (15, 15)
        color "#fff"
        size 40
        bold True
        outlines [(3, "#000", 0, 0)]
        hover_outlines [(3, "#ff0", 0, 0)]

label start:
    show screen bug_button
    "Добро пожаловать в игру!"
    return