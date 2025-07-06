from fastapi import FastAPI, Response
from google import genai
from pydantic import BaseModel
import os
class Generate(BaseModel):
    character : str
    hairColour : str
    clothing : str
app = FastAPI()
@app.get("/")
def hello():
    return {"Hello": "World"}
    
@app.post("/create")
def inputt(generate : Generate):
    promptt  = f"A cute, cartoon-style {generate.character} with soft, {generate.hairColour} hair in gentle pastel shades, wearing a {generate.clothing}. Having a cheerful smile, big sparkling eyes, and a friendly, playful expression. The design uses minimalistic lines and soft shading, with bright and soothing colors. The background is a simple pastel tone with small, floating heart shapes, creating a warm and inviting sticker look."
    client = genai.Client(api_key=os.getenv("API_KEY"))
    result = client.models.generate_images(
        model="models/imagen-4.0-generate-preview-06-06",
        prompt = promptt,
        config=dict(
            number_of_images=1,
            output_mime_type="image/jpeg",
            person_generation="ALLOW_ADULT",
            aspect_ratio="1:1",
        ),
    )
    print(result)
    for generated_image in result.generated_images:
        return Response(content=generated_image.image.image_bytes, media_type="image/png")
    

