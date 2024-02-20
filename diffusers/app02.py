import diffusers
from PTL import Image, ImageDraw, ImageFont

def text_to_image(text, deffuser_model):
    deffuser = diffusers.load_diffuser(diffuser_model)
    inage_data = diffuser.generate(text)