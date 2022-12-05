# Card_simulation.py

"""This application lets you test the card simulation Classes and print the card images"""

# import required packages

from deck import DeckOfCards

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path

deck = DeckOfCards()  # create a deck
path = Path('.').joinpath('card_images')

figure, axes_list = plt.subplots(nrows=4, ncols=13)

for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)  # hide xaxis labels
    axes.get_yaxis().set_visible(False)  # hide yaxis labels
    image_name = deck.deal_card().image_name  # deal a card in each iteration and get the name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))  # locate image using path for the image name
    axes.imshow(img)  # show image
