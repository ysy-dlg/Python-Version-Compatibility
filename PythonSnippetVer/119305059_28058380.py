#open your image file and convert to black/white
image_file = Image.open('Desktop/350px-Wiktionary_small.svg.png')
image_file = image_file.convert('1')  # to black/white
W = to_ascii(image_file)
W = hashes_to_text(W,'Wikipedia')
print W