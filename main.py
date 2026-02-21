import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import httpx

app = FastAPI()

# مفتاحك الذي ارسلته لي
GROQ_API_KEY = "Gsk_i1oiuUp0ZiJw6njRXctxWGdyb3FYbrhRAyrAbqu4qYrjM4RtV6un"

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>X-PROJECT AI: PRO-DEVELOPER</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { background-color: #000; color: #00ff00; font-family: 'Courier New', monospace; margin: 0; padding: 10px; display: flex; flex-direction: column; height: 100vh; }
                .header { border-bottom: 2px solid #00ff00; padding: 10px; text-align: center; box-shadow: 0 0 10px #00ff00; }
                #chatbox { flex: 1; overflow-y: auto; padding: 20px; background: #050505; border: 1px solid #111; margin: 10px 0; border-radius: 5px; }
                .input-area { display: flex; gap: 5px; padding-bottom: 20px; }
                input { flex: 1; background: #000; border: 1px solid #00ff00; color: #00ff00; padding: 12px; outline: none; border-radius: 5px; }
                button { background: #00ff00; color: #000; border: none; padding: 0 20px; font-weight: bold; cursor: pointer; border-radius: 5px; }
                .user-msg { color: #fff; margin: 10px 0; }
                .ai-msg { color: #00ffff; margin: 10px 0; border-left: 3px solid #00ffff; padding-left: 10px; white-space: pre-wrap; }
            </style>
        </head>
        <body>
            <div class="header"><h3> > X-PROJECT_INTELLIGENCE: DEV_MODE</h3></div>
            <div id="chatbox">الوكيل: أنا الآن مبرمجك الخاص.. اطلب مني كتابة أي كود أو برنامج وسأبدأ فوراً.</div>
            <div class="input-area">
                <input type="text" id="userInput" placeholder="مثلاً: اصنع لي برنامج آلة حاسبة بلغة Python...">
                <button onclick="askAI()">إرسال</button>
            </div>

            <script>
                async function askAI() {
                    const input = document.getElementById('userInput');
                    const box = document.getElementById('chatbox');
                    const text = input.value;
                    if (!text) return;

                    box.innerHTML += `<div class="user-msg"><b>أنت:</b> ${text}</div>`;
                    input.value = "";
                    box.scrollTop = box.scrollHeight;

                    const response = await fetch('/chat?msg=' + encodeURIComponent(text));
                    const data = await response.json();
                    
                    box.innerHTML += `<div class="ai-msg"><b>الوكيل:</b><br>${data.reply}</div>`;
                    box.scrollTop = box.scrollHeight;
                }
            </script>
        </body>
    </html>
    """

@app.get("/chat")
async def chat(msg: str):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a senior software engineer. Answer in Arabic and provide full code when asked to build something."},
            {"role": "user", "content": msg}
        ]
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data, timeout=30.0)
        result = response.json()
        reply = result['choices'][0]['message']['content']
        return {"reply": reply}
