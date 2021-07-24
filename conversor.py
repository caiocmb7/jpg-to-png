from PIL import Image 
import os
input_path = r'C:\Users\Caio\Desktop\smartbee\imagens\baseParaWCAMA\dataset\novaBaseAtualizada\abelhasNaoApis'

for filename in os.listdir(input_path):
    current_img = Image.open(input_path + '\\' + filename)
    current_img.save(input_path + '\\' +
                     filename + '.png', 'PNG')