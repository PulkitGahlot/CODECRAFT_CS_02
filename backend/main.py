from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from PIL import Image
from io import BytesIO

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------- TEXT ENCRYPTION --------

class CipherRequest(BaseModel):
    text: str
    shift: int
    mode: str  # 'encrypt' or 'decrypt'

def caesar_ascii_cipher(text, shift, mode):
    result = ""
    for char in text:
        if mode == 'encrypt':
            result += chr((ord(char) + shift) % 256)
        elif mode == 'decrypt':
            result += chr((ord(char) - shift) % 256)
        else:
            result += char
    return result

@app.post("/cipher")
def process_cipher(req: CipherRequest):
    result = caesar_ascii_cipher(req.text, req.shift, req.mode)
    return {"result": result}

# -------- IMAGE ENCRYPTION --------

# --------By XORing with a key------------------
@app.post("/image_cipher")
async def image_cipher(
    mode: str = Form(...),
    key: int = Form(...),
    file: UploadFile = File(...)
):
    from PIL import Image
    from io import BytesIO

    image = Image.open(file.file).convert("RGB")
    pixels = image.load()
    width, height = image.size
    key=175
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            if mode in ["encrypt", "decrypt"]:
                # XOR each RGB channel with the key
                pixels[i, j] = (
                    r ^ key,
                    g ^ key,
                    b ^ key
                )

    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/png")



# -----------By reversing RGB values-------------
# @app.post("/image_cipher")
# async def image_cipher(
#     mode: str = Form(...),
#     file: UploadFile = File(...)
# ):
#     image = Image.open(file.file).convert("RGB")
#     pixels = image.load()
#     width, height = image.size

#     for i in range(width):
#         for j in range(height):
#             r, g, b = pixels[i, j]

#             if mode == "encrypt":
#                 # Rotate RGB → GBR
#                 pixels[i, j] = (g, b, r)
#             elif mode == "decrypt":
#                 # Reverse GBR → RGB
#                 pixels[i, j] = (b, r, g)

#     buffer = BytesIO()
#     image.save(buffer, format="PNG")
#     buffer.seek(0)

#     return StreamingResponse(buffer, media_type="image/png")


# ---------image encryption using ceasar cipher------------
# @app.post("/image_cipher")
# async def image_cipher(
#     mode: str = Form(...),
#     key: int = Form(...),
#     file: UploadFile = File(...)
# ):
#     image = Image.open(file.file).convert("RGB")
#     pixels = image.load()
#     width, height = image.size

#     for i in range(width):
#         for j in range(height):
#             r, g, b = pixels[i, j]
#             if mode == "encrypt":
#                 pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
#             elif mode == "decrypt":
#                 pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

#     buffer = BytesIO()
#     image.save(buffer, format="PNG")
#     buffer.seek(0)

#     return StreamingResponse(buffer, media_type="image/png")