from django.shortcuts import render
from dataclasses import dataclass
from typing import List
@dataclass
class Monsters:
    name: str
    description: str
    parents: str

# Create your views here.
def monster_views(request):
    scream_team = {
        "GHOULS":{
        "Frankie": Monsters('Frankie Stein',
        'Frankie Stein is a wholehearted, and pretty-in-personality kind of girl. She is optimistic, positive, kind-hearted and always gets along with others, although she is naive.',
        "She is the Daughter of Frankenstein's monster and his bride."),
        "Clawdeen": Monsters('Clawdeen',
        'Clawdeen is confident, energetic, and fierce girl. She has a hard-exterior but is very sweet on the inside and to those closest to her.',
        "Daughter of Harriet Wolf and her spouse."),
        "Draculaura": Monsters('Draculaura',
        'Draculaura is sweet, energetic, friendly, sensitive and easygoing, though she can be a bit childish. ',
        "She is the adopted daughter of Dracula."),
        "Cleo": Monsters('Cleo De Nile',
        "Cleo is extremely royal, so she expects everyone to treat her like it. Usually, her attitude is selfish, arrogant, and sassy, but deep down, Cleo's a very caring, kind, and thoughtful ghoul who cares about her friends.",
        "She is the daughter of the Mummy Ramses and Dedyet.")
    } }
    return render(request, "index.html", scream_team)

def all_views(request, friends):
    scream_team = {
        "peeps":friends,
        "GHOULS":{
        "Frankie": Monsters('Frankie Stein',
        'Frankie Stein is a wholehearted, and pretty-in-personality kind of girl. She is optimistic, positive, kind-hearted and always gets along with others, although she is naive.',
        "She is the Daughter of Frankenstein's monster and his bride."),
        "Clawdeen": Monsters('Clawdeen',
        'Clawdeen is confident, energetic, and fierce girl. She has a hard-exterior but is very sweet on the inside and to those closest to her.',
        "Daughter of Harriet Wolf and her spouse."),
        "Draculaura": Monsters('Draculaura',
        'Draculaura is sweet, energetic, friendly, sensitive and easygoing, though she can be a bit childish. ',
        "She is the adopted daughter of Dracula."),
        "Cleo": Monsters('Cleo De Nile',
        "Cleo is extremely royal, so she expects everyone to treat her like it. Usually, her attitude is selfish, arrogant, and sassy, but deep down, Cleo's a very caring, kind, and thoughtful ghoul who cares about her friends.",
        "She is the daughter of the Mummy Ramses and Dedyet.")
    } }
    return render(request,"info.html",scream_team)

