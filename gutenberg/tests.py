from gutenberg import *

def test_word_count():
	assert word_count("Hello good sir") == {"hello":1, "good":1, "sir":1}
	assert word_count("Hello, hello good sir") == {"hello":2, "good":1, "sir":1}
	assert word_count("As he walked again and again") == {"as":1, "he":1, "walked":1, "again":2, "and":1}
	assert word_count("""Hello, my name is Ewala. I come from the planet Alawe, in the galaxy Ewala, in the universe Alawe. But the point is I tried. If you think you need to go to the bakery, please do so now, because I do not want to be interrupted while I tell you my story. ...but anyway, I have been thinking about my happiness lately and have come to the conclusion that I am happy. This is annoying. If you saw a chicken as happy as me, I'll replace it, and give you a full refund... no questions asked! But that's not the point. The point is I am battery operated. Well, actually I am not.""") == {"the":8,"i":8,"you":5,"to":4,"is":4,"point":3,"not":3,"my":3,"but":3,"am":3,"in":2,"if":2,"have":2,"happy":2,"ewala":2,"do":2,"come":2,"as":2,"and":2,"alawe":2,"a":2,"while":1,"well":1,"want":1,"universe":1,"tried":1,"this":1,"thinking":1,"think":1,"that's":1,"that":1,"tell":1,"story":1,"so":1,"saw":1,"replace":1,"refund":1,"questions":1,"please":1,"planet":1,"operated":1,"now":1,"no":1,"need":1,"name":1,"me":1,"lately":1,"it":1,"interrupted":1,"i'll":1,"hello":1,"happiness":1,"go":1,"give":1,"galaxy":1,"full":1,"from":1,"conclusion":1,"chicken":1,"been":1,"because":1,"be":1,"battery":1,"bakery":1,"asked":1,"anyway":1,"annoying":1,"actually":1,"about":1}

def test_cutoff():
	assert cutoff({'one':1, 'two':2, 'three':3}, 1) == {'three': 3}
	assert cutoff({'one':1, 'two':2, 'three':3, 'four': 4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10}, 4) == {'ten': 10, 'nine':9, 'eight':8, 'seven':7}