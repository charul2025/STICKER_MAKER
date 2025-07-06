# 🧸 Cute Character Sticker Generator API

A FastAPI-powered service that turns simple descriptions into adorable, cartoon-style character stickers. No art skills required—just bring your imagination.

---

## ✨ Why This Exists

Sometimes you just want a cute little character that *looks* like what you picture in your head—but drawing or writing the perfect AI prompt? Ugh, too much effort.

This project is your shortcut. It:

- 🧑‍🎨 Lets anyone generate custom cartoon stickers, just by saying what they want
- ⚙️ Automates prompt-writing for AI image models
- 🎨 Works with any character type or style (kids, adults, anything in between)

No design tools, no dragging pixels. Just pure creativity, made easy.

---

## ⚡ How It Works

### 🔧 Built With:
- [FastAPI](https://fastapi.tiangolo.com/) – for a sleek and speedy API
- [AI Image Model (e.g., Imagen, DALLE, etc.)] – plugged in to turn prompts into visuals

### 🧪 API Endpoint:
**POST** `/create`

#### 📦 Request Body:
```json
{
  "character": "girl",
  "hairColour": "black",
  "clothing": "red hoodie"
}
