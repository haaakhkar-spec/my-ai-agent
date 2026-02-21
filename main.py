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
                #box { border: 2px solid #0f0; height: 350px; overflow-y: auto; padding: 15px; background: #050505; margin-bottom: 15px; box-shadow: 0 0 10px #0f0; }
                input { width: 70%; padding: 12px; background: #000; border: 1px solid #0f0; color: #0f0; outline: none; }
                button { padding: 12px 20px; background: #0f0; color: #000; font-weight: bold; border: none; cursor: pointer; }
                .msg { margin: 10px 0; border-bottom: 1px solid #111; padding-bottom: 5px; }
            </style>
        </head>
        <body>
            <h2 style="color:#0f0">> X-PROJECT: SYSTEM READY</h2>
            <div id="box">جاري الاتصال بالعقل الاصطناعي... تمت العملية بنجاح. أنا أسمعك الآن، تفضل بسؤالك.</div>
            <div style="display:flex; gap:10px;">
                <input type="text" id="userInput" placeholder="اسأل مبرمجك الخاص...">
                <button onclick="ask()">إرسال</button>
            </div>
            <script>
                async function ask() {
                    const i = document.getElementById('userInput');
                    const b = document.getElementById('box');
                    if(!i.value) return;
                    b.innerHTML += '<div class="msg"><b>أنت:</b> ' + i.value + '</div>';
                    const text = i.value;
                    i.value = '';
                    try {
                        const res = await fetch('/chat?q=' + encodeURIComponent(text));
                        const data = await res.json();
                        b.innerHTML += '<div class="msg" style="color:#0ff"><b>الوكيل:</b><br>' + data.a + '</div>';
                    } catch(e) {
                        b.innerHTML += '<div style="color:red">خطأ: السيرفر لم يستجب. تأكد من تحديث Render.</div>';
                    }
                    b.scrollTop = b.scrollHeight;
                }
            </script>
        </body>
    </html>
    """

@app.get("/chat")
async def chat(q: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"Bearer {KEY}"},
                json={
                    "model": "llama3-8b-8192",
                    "messages": [{"role": "user", "content": q}]
                },
                timeout=30.0
            )
            result = response.json()
            answer = result['choices'][0]['message']['content']
            return {"a": answer}
        except Exception as e:
            return {"a": "حدث خطأ أثناء محاولة الرد. يرجى المحاولة مرة أخرى."}
