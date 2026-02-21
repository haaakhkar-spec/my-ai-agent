from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>X-Agent Online</title>
            <style>
                body { background: #000; color: #0f0; font-family: monospace; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; text-shadow: 0 0 5px #0f0; }
                .box { border: 2px solid #0f0; padding: 40px; box-shadow: 0 0 20px #0f0; text-align: center; background: rgba(0,255,0,0.05); }
                .pulse { animation: pulse 2s infinite; }
                @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.5; } 100% { opacity: 1; } }
            </style>
        </head>
        <body>
            <div class="box">
                <h1 class="pulse"> > X-PROJECT_INTELLIGENCE: ACTIVE</h1>
                <p>ذكاؤك الخاص متصل الآن بنجاح.</p>
                <p> [ الحالة: مستعد للعمل ] </p>
            </div>
        </body>
    </html>
    """
