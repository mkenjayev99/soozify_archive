import os
import re
from pathlib import Path

# Parent directory containing the subdirectories (change if needed)
parent_directory = '.'  # Current folder; or e.g., r'C:\path\to\parent'

# List of subdirectories to process
subdirs = ['Gojuon/Chunks', 'Dakuon/Chunks', 'Youon/Chunks']

# Mapping from Hiragana to Romaji (standard Hepburn transliteration)
hiragana_to_romaji = {
    # Basic Gojuon
    'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
    'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
    'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
    'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
    'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
    'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
    'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
    'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    'わ': 'wa', 'を': 'o', 'ん': 'n',
    
    # Dakuon & Handakuon
    'が': 'ga', 'ぎ': 'gi', 'ぐ': 'gu', 'げ': 'ge', 'ご': 'go',
    'ざ': 'za', 'じ': 'ji', 'ず': 'zu', 'ぜ': 'ze', 'ぞ': 'zo',
    'だ': 'da', 'ぢ': 'ji', 'づ': 'zu', 'で': 'de', 'ど': 'do',
    'ば': 'ba', 'び': 'bi', 'ぶ': 'bu', 'べ': 'be', 'ぼ': 'bo',
    'ぱ': 'pa', 'ぴ': 'pi', 'ぷ': 'pu', 'ぺ': 'pe', 'ぽ': 'po',
    
    # Youon (contracted sounds)
    'きゃ': 'kya', 'きゅ': 'kyu', 'きょ': 'kyo',
    'しゃ': 'sha', 'しゅ': 'shu', 'しょ': 'sho',
    'ちゃ': 'cha', 'ちゅ': 'chu', 'ちょ': 'cho',
    'にゃ': 'nya', 'にゅ': 'nyu', 'にょ': 'nyo',
    'ひゃ': 'hya', 'ひゅ': 'hyu', 'ひょ': 'hyo',
    'みゃ': 'mya', 'みゅ': 'myu', 'みょ': 'myo',
    'りゃ': 'rya', 'りゅ': 'ryu', 'りょ': 'ryo',
    'ぎゃ': 'gya', 'ぎゅ': 'gyu', 'ぎょ': 'gyo',
    'じゃ': 'ja', 'じゅ': 'ju', 'じょ': 'jo',
    'びゃ': 'bya', 'びゅ': 'byu', 'びょ': 'byo',
    'ぴゃ': 'pya', 'ぴゅ': 'pyu', 'ぴょ': 'pyo',
}

# Process each subdirectory
for subdir in subdirs:
    directory_path = Path(parent_directory) / subdir
    if not directory_path.exists():
        print(f"Skipping {subdir}: Directory does not exist")
        continue
    
    print(f"\nProcessing directory: {subdir}")
    
    audio_files = [f for f in directory_path.glob('kana_*.mp3') if ')(' in f.name]
    
    for file_path in audio_files:
        print(f"Processing: {file_path.name}")
        
        # Extract the hiragana from the filename, e.g., from "kana_1(あ)(ア).mp3" get "あ"
        match = re.search(r'\((\S+)\)\(\S+\)', file_path.name)
        if match:
            hiragana = match.group(1).strip()
            romaji = hiragana_to_romaji.get(hiragana)
            
            if romaji:
                # Get the original stem without the (hiragana)(katakana)
                original_stem = re.sub(r'\(\S+\)\(\S+\)$', '', file_path.stem)
                # Replace space with nothing or underscore if desired
                original_stem = original_stem.replace(' ', '')  # Removes space
                # original_stem = original_stem.replace(' ', '_')  # Use underscore instead
                
                # New name: append _romaji
                new_stem = f"{original_stem}{romaji}"
                new_name = f"{new_stem}.mp3"
                new_path = file_path.with_name(new_name)
                
                # Rename
                os.rename(file_path, new_path)
                print(f"Renamed to: {new_name}")
            else:
                print(f"Skipping {file_path.name}: No romaji mapping for '{hiragana}'")
        else:
            print(f"Skipping {file_path.name}: No matching hiragana/katakana pattern found")

print("\nDone! All directories processed.")
