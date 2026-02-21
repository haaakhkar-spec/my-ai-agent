from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import httpx

app = FastAPI()

# مفتاحك الخاص للذكاء الاصطناعي
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
                #box { border: 1px solid #0f0; height: 300px; overflow-y: auto; padding: 10px; background: #050505; margin-bottom: 10px; border-radius: 5px; }
                .input-area { display: flex; gap: 5px; }
                input { flex: 1; padding: 12px; background: #000; border: 1px solid #0f0; color: #0f0; outline: none; }
                button { padding: 10px 20px; background: #0f0; color: #000; border: none; font-weight: bold; cursor: pointer; }
                .msg { margin: 10px 0; line-height: 1.4; }
            </style>
        </head>
        <body>
            <h3>> X-PROJECT: ACTIVE</h3>
            <div id="box">نظام الذكاء الاصطناعي جاهز.. اطلب كوداً أو اسأل سؤالاً.</div>
            <div class="input-area">
                <input type="text" id="userInput" placeholder="اكتب أمرك هنا...">
                <button onclick="ask()">إرسال</button>
            </div>
            <script>
                async function ask() {
                    const i = document.getElementById('userInput');
                    const b = document.getElementById('box');
                    if(!i.value) return;
                    b.innerHTML += '<div class="msg"><b>أنت:</b> ' + i.value + '</div>';
                    const res = await fetch('/chat?q=' + encodeURIComponent(i.value));
                    const data = await res.json();
                    b.innerHTML += '<div class="msg" style="color:#0ff"><b>الوكيل:</b><br>' + data.a + '</div>';
                    i.value = '';
                    b.scrollTop = b.scrollHeight;
                }
            </script>
        </body>
    </html>
    """

@app.get("/chat")
async def chat(q: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {KEY}"},
            json={
                "model": "llama3-8b-8192",
                "messages": [{"role": "system", "content": "You are a pro coder. Answer in Arabic."}, {"role": "user", "content": q}]
            }
        )
        data = response.json()
        return {"a": data['choices'][0]['message']['content']}
