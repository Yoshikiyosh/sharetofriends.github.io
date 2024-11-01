from PIL import Image

# Load the webp image
img = Image.open("東京駅.webp")
# Save it as jpg
img.save("東京駅.jpg", "JPEG")

 
