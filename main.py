from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>X-Project Agent</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { background-color: #000; color: #00ff00; font-family: 'Courier New', monospace; text-align: center; padding: 20px; }
                .container { border: 2px solid #00ff00; padding: 20px; max-width: 500px; margin: auto; box-shadow: 0 0 15px #00ff00; }
                #chatbox { height: 250px; border: 1px solid #444; margin: 20px 0; padding: 10px; overflow-y: auto; text-align: left; background: #050505; }
                input { width: 70%; padding: 10px; background: #000; border: 1px solid #00ff00; color: #00ff00; outline: none; }
                button { padding: 10px; background: #00ff00; color: #000; border: none; font-weight: bold; cursor: pointer; width: 25%; }
                button:hover { background: #008800; color: white; }
                .agent-msg { color: cyan; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1> > X-PROJECT: ACTIVE</h1>
                <div id="chatbox">نظام الوكيل: مرحباً بك.. أنا متصل وجاهز للأوامر.</div>
                <input type="text" id="userInput" placeholder="اكتب أمرك هنا...">
                <button onclick="send()">إرسال</button>
            </div>

            <script>
                function send() {
                    var input = document.getElementById('userInput');
                    var box = document.getElementById('chatbox');
                    if(input.value.trim() !== "") {
                        box.innerHTML += "<div><strong>أنت:</strong> " + input.value + "</div>";
                        box.innerHTML += "<div class='agent-msg'><strong>الوكيل:</strong> استلمت أمرك.. جاري تفعيله برمجياً.</div>";
                        input.value = "";
                        box.scrollTop = box.scrollHeight;
                    }
                }
            </script>
        </body>
    </html>
    """
