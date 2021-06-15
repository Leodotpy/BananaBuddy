import random
import webbrowser

small_sites_list = [
    "https://www.google.com/search?q=how+to+peel+a+banana",
    "https://www.google.com/search?q=how+much+potassium+in+a+banana",
    "https://www.youtube.com/watch?v=eRBOgtp0Hac",
    "https://www.reddit.com/r/banana/",
    "https://theamazingworldofgumball.fandom.com/wiki/Banana_Joe",
    "https://www.google.com/search?q=how+to+make+banana+bread",
    "https://www.youtube.com/watch?v=sFukyIIM1XI",
    "https://www.youtube.com/watch?v=LH5ay10RTGY"

]

webbrowser.open(random.choice(small_sites_list, ))

