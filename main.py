import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import httpx

app = FastAPI()

# مفتاحك الذي استخرجته
GROQ_API_KEY = "Gsk_i1oiuUp0ZiJw6njRXctxWGdyb3FYbrhRAyrAbqu4qYrjM4RtV6un"

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>X-PROJECT AI: CODER</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { background-color: #000; color: #00ff00; font-family: monospace; padding: 20px; display: flex; flex-direction: column; height: 100vh; margin: 0; }
                #display { flex: 1; border: 1px solid #00ff00; background: #050505; padding: 15px; overflow-y: auto; margin-bottom: 10px; border-radius: 8px; box-shadow: 0 0 10px #00ff00; }
                .input-box { display: flex; gap: 5px; }
                input { flex: 1; background: #000; border: 1px solid #00ff00; color: #00ff00; padding: 12px; border-radius: 5px; outline: none; }
                button { background: #00ff00; color: #000; border: none; padding: 12px 20px; font-weight: bold; cursor: pointer; border-radius: 5px; }
                pre { background: #111; padding: 10px; border-radius: 5px; color: #00ffff; white-space: pre-wrap; word-break: break-all; }
            </style>
        </head>
        <body>
            <h3> > X-PROJECT_INTELLIGENCE: ACTIVE </h3>
            <div id="display">أهلاً بك.. أنا مبرمجك الخاص. اطلب مني صنع أي برنامج الآن.</div>
            <div class="input-box">
                <input type="text" id="userInput" placeholder="مثلاً: اكتب كود بايثون لإرسال رسائل واتساب...">
                <button onclick="ask()">تنفيذ</button>
            </div>

            <script>
                async function ask() {
                    const inp = document.getElementById('userInput');
                    const disp = document.getElementById('display');
                    const text = inp.value;
                    if(!text) return;
                    
                    disp.innerHTML += `<div style="color:white; margin-top:10px;"><b>أنت:</b> ${text}</div>`;
                    inp.value = "";
                    
                    const res = await fetch('/chat?msg=' + encodeURIComponent(text));
                    const data = await res.json();
                    
                    disp.innerHTML += `<div style="color:#00ffff; margin-top:10px;"><b>الوكيل:</b><br><pre>${data.reply}</pre></div>`;
                    disp.scrollTop = disp.scrollHeight;
                }
            </script>
        </body>
    </html>
    """

@app.get("/chat")
async def chat(msg: str):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are an expert programmer. Provide full, working code for any task requested. Answer in Arabic."},
            {"role": "user", "content": msg}
        ]
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(url, headers=headers, json=data, timeout=30.0)
        reply = r.json()['choices'][0]['message']['content']
        return {"reply": reply}
