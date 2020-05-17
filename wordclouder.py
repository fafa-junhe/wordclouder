import wordcloud
import os
import matplotlib.pyplot as plt

word_list = input("word list(test,test2,test3) or file:")
split_s = input("split symbol(,):")
if word_list == "":
    word_list = "test,test2,test3"
if split_s == "":
    split_s = ","
if os.path.isfile(word_list):
    word_list = open(word_list, "r").read()
word_list.split(split_s)
scale = input("scale(4):")
image = input("background(None):")
if image == "" or image == "None":
    image = None
else:
    if os.path.isfile(image):
        image = plt.imread(image)
    else:
        raise FileNotFoundError("image file don't exist")
prefer_horizontal = input("horizontal percent(.9):")
if prefer_horizontal.isdigit():
    prefer_horizontal = int(prefer_horizontal)
if prefer_horizontal == "":
    prefer_horizontal = .9

background_color = input("background color(white):")
random_state = input("color kinds(30):")
font_path = input("font_path(None):")
file = input("the file that save to(img.png):")
if font_path == "" or font_path == "None":
    font_path = None
if random_state.isdigit():
    random_state = int(random_state)
if random_state == "":
    random_state = 30
if background_color == "":
    background_color = "white"
if file == "":
    file = "img.png"
if scale.isdigit():
    scale = int(scale)
if scale == "":
    scale = 4
wordcloud.WordCloud(
    scale=scale,
    mask=image,
    prefer_horizontal=prefer_horizontal,
    background_color=background_color,
    random_state=random_state,
    font_path=font_path,
).generate(word_list).to_file(file)
print("Successful!")
