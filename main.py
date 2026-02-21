from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import httpx

app = FastAPI()

# مفتاحك الذي يعمل
KEY = "Gsk_i1oiuUp0ZiJw6njRXctxWGdyb3FYbrhRAyrAbqu4qYrjM4RtV6un"

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>X-PROJECT AI</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { background: #000; color: #0f0; font-family: monospace; padding: 20px; }
                #box { border: 1px solid #0f0; height: 300px; overflow-y: auto; padding: 10px; background: #050505; margin-bottom: 10px; }
                input { width: 70%; padding: 12px; background: #000; border: 1px solid #0f0; color: #0f0; }
                button { padding: 12px; background: #0f0; color: #000; font-weight: bold; border: none; cursor: pointer; }
                .msg { margin: 8px 0; }
            </style>
        </head>
        <body>
            <h3>> X-PROJECT: ACTIVE</h3>
            <div id="box">تم إصلاح النظام.. أنا أسمعك الآن، اطلب ما تريد.</div>
            <input type="text" id="ui" placeholder="اكتب هنا...">
            <button onclick="ask()">إرسال</button>
            <script>
                async function ask() {
                    const i = document.getElementById('ui'), b = document.getElementById('box');
                    if(!i.value) return;
                    b.innerHTML += '<div class="msg"><b>أنت:</b> ' + i.value + '</div>';
                    const res = await fetch('/chat?q=' + encodeURIComponent(i.value));
                    const data = await res.json();
                    b.innerHTML += '<div style="color:#0ff" class="msg"><b>الوكيل:</b> ' + data.a + '</div>';
                    i.value = ''; b.scrollTop = b.scrollHeight;
                }
            </script>
        </body>
    </html>
    """

@app.get("/chat")
async def chat(q: str):
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {KEY}"},
            json={
                "model": "llama3-8b-8192",
                "messages": [{"role": "user", "content": q}]
            }
        )
        return {"a": r.json()['choices'][0]['message']['content']}
