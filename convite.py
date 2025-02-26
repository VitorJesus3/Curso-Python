#Instalar as bibliotecas IPython e Image

from PIL import Image, ImageDraw, ImageFont
from IPython.display import Image as imgx

nomes = ['Jeferson','Vitor','Mariana']
evento = 'Formatura do Python'
data = '27 de Fevereiro de 2025'
local = 'Av Paulista, na Clarify'

for nome in nomes:
    # Criando uma imgaem em RGB com fundo branco(600 por 400px)
    img = Image.new("RGB", (600,400),(255,255,255)) # É criada a imagem com fundo branco 
    draw = ImageDraw.Draw(img) # Preparando a ferramenta para desenhar a imagem

    # Fontes que serão usadas no texto
    font_title = ImageFont.truetype('arial.ttf',36)
    # Fonte do titulo e tamanho 
    font_text = ImageFont.truetype('arial.ttf',24)
    # Fonte para o texto do evento e tamanho
    # adicionando o texto principal na imagem (titulo do convite com nome) 
    draw.text((50,50), f'Convite para {nome}',
            (0,0,0),
            font=font_title
            )
    draw.text((50,100), evento,
            (0,0,0),
            font=font_text
            )
    draw.text((50,150), data,
            (0,0,0),
            font=font_text
            )
    draw.text((50,200), local,
            (0,0,0),
            font=font_text
            )
    # desenho
    draw.rectangle(
        [(45,45), (555,355)],
        outline=(0,0,0),
        width=5
        )
    img.save(
        f'{nome}.jpg'
        )
    