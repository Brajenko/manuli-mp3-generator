from gtts import gTTS
import pymorphy2

N = 100

f = open('manuli{}.mp3'.format(N), 'wb')

morph = pymorphy2.MorphAnalyzer()

text = ' '.join(['{} {}.'.format(i,
                                 morph.parse('манул')[0].make_agree_with_number(i).word)
                 for i in range(1, N + 1)])

tts = gTTS(text, lang='ru')

tts.write_to_fp(f)

f.close()
