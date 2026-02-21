from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>X-Project Console</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { background-color: #000; color: #0f0; font-family: monospace; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
                .terminal { border: 2px solid #0f0; padding: 20px; width: 90%; max-width: 500px; box-shadow: 0 0 20px #0f0; border-radius: 10px; }
                #log { height: 200px; overflow-y: auto; border: 1px solid #050; margin-bottom: 10px; padding: 10px; text-align: left; font-size: 14px; background: #050505; }
                input { width: 70%; padding: 10px; background: #000; border: 1px solid #0f0; color: #0f0; outline: none; }
                button { width: 25%; padding: 10px; background: #0f0; color: #000; border: none; cursor: pointer; font-weight: bold; }
                button:active { background: #fff; }
            </style>
        </head>
        <body>
            <div class="terminal">
                <h3>> X-PROJECT_SYSTEM: ONLINE</h3>
                <div id="log">نظام الوكيل: بانتظار أوامرك...</div>
                <input type="text" id="command" placeholder="اكتب أمرك هنا...">
                <button onclick="execute()">تنفيذ</button>
            </div>
            <script>
                function execute() {
                    const cmd = document.getElementById('command');
                    const log = document.getElementById('log');
                    if(cmd.value) {
                        log.innerHTML += "<div><span style='color:white'>أنت:</span> " + cmd.value + "</div>";
                        log.innerHTML += "<div><span style='color:cyan'>الوكيل:</span> جاري معالجة الأمر... تم الاستلام بنجاح.</div>";
                        cmd.value = '';
                        log.scrollTop = log.scrollHeight;
                    }
                }
            </script>
        </body>
    </html>
    """
