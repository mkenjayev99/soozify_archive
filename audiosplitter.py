from pydub import AudioSegment
from pydub.silence import split_on_silence

audio0 = AudioSegment.from_mp3("Gojuon/Gojuon.mp3")
audio1 = AudioSegment.from_mp3("Dakuon/Dakuon_Handakuon.mp3")
audio2 = AudioSegment.from_mp3("Youon/Youon.mp3")

chunks0 = split_on_silence(audio0, min_silence_len=300, silence_thresh=-40)
chunks1 = split_on_silence(audio1, min_silence_len=300, silence_thresh=-40)
chunks2 = split_on_silence(audio2, min_silence_len=300, silence_thresh=-40)

numeration = 0
for i, chunk in enumerate(chunks0):
    numeration += 1
    chunk.export(f"Gojuon/Chunks/kana_{numeration}.mp3", format="mp3")

for i, chunk in enumerate(chunks1):
    numeration += 1
    chunk.export(f"Dakuon/Chunks/kana_{numeration}.mp3", format="mp3")

for i, chunk in enumerate(chunks2):
    numeration += 1
    chunk.export(f"Youon/Chunks/kana_{numeration}.mp3", format="mp3")