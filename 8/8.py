import os
from PIL import Image

data = [l for l in open(os.path.join(os.path.dirname(__file__),'input.txt')).read()]
width = 25
heigth = 6

# data = list('0222112222120000')
# width = 2
# heigth = 2

layersize = width * heigth
# layers = [i for i in range(0,len(data), layersize)]
layers = [data[i:i+layersize] for i in range(0,len(data), layersize)]

fewest_0_digits = 99999999
fewest_0_digits_layer = -1

for i, layer in enumerate(layers):
    zeros = layer.count('0')
    if zeros < fewest_0_digits:
        fewest_0_digits = zeros
        fewest_0_digits_layer = i

a = layers[fewest_0_digits_layer].count('1')
b = layers[fewest_0_digits_layer].count('2')

print(f'part 1: {a * b}')

image = Image.new('RGB', (width, heigth))

layers.reverse()
for layer in layers:
    for i, pixel in enumerate(layer):
        c = int(pixel)
        if c > 1:
            continue
        coord = (i % width, i // width)
        image.putpixel(coord, (c * 255, c * 255, c * 255))

image.show()
print('done')