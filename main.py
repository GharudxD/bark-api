import replicate
import os
import CONST
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

REPLICATE_API_TOKEN = CONST.REPLICATE_API_TOKEN
os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

app = FastAPI()


def helper_function(promt):
    output = replicate.run(
        "suno-ai/bark:b76242b40d67c76ab6742e987628a2a9ac019e11d56ab96c4e91ce03b79b2787",
        input={"prompt": f"{promt}"}
    )
    return output['audio_out']

@app.get('/{prompt}', response_class=HTMLResponse)
async def get_audio(prompt):
    res = helper_function(prompt)

    html_content = f"""
        <html>
            <head>
                <title>Audio of prompt</title>
            </head>
            <body>
                <audio controls>
                    <source src="{res}" type="audio/mpeg">
                </audio>
            </body>
        </html>
        """
    return HTMLResponse(content=html_content, status_code=200)

if __name__ == "__main__":
    uvicorn.run(app,host='0.0.0.0',port=9000)
