import random

game = True


########################################################################################################################################################
#### Toutes les listes de kanas ont étés générées automatiquement par l'IA Github Copilot, j'ai vérifié par mes soins si il n'y avait pas d'erreurs.####
########################################################################################################################################################

 #list of every hiraganas in japanese characters linked to their romaji
hiraganas = {   'あ': 'a',  'い': 'i',  'う': 'u',  'え': 'e',  'お': 'o',  'か': 'ka',  'き': 'ki',  'く': 'ku',  'け': 'ke', 
'こ': 'ko',  'さ': 'sa',  'し': 'shi',  'す': 'su',  'せ': 'se',  'そ': 'so',  'た': 'ta',  'ち': 'chi',  'つ': 'tsu',  'て': 'te',
'と': 'to',  'な': 'na',  'に': 'ni',  'ぬ': 'nu',  'ね': 'ne',  'の': 'no',  'は': 'ha',  'ひ': 'hi',  'ふ': 'fu',  'へ': 'he',
'ほ': 'ho',  'ま': 'ma',  'み': 'mi',  'む': 'mu',  'め': 'me',  'も': 'mo',  'や': 'ya',  'ゆ': 'yu',  'よ': 'yo',  'ら': 'ra',
'り': 'ri',  'る': 'ru',  'れ': 're',  'ろ': 'ro',  'わ': 'wa',  'を': 'wo',  'ん': 'n',  'が': 'ga',  'ぎ': 'gi',  'ぐ': 'gu',
'げ': 'ge',  'ご': 'go',  'ざ': 'za',  'じ': 'ji',  'ず': 'zu',  'ぜ': 'ze',  'ぞ': 'zo',  'だ': 'da',  'ぢ': 'ji',  'づ': 'zu',
'で': 'de',  'ど': 'do',  'ば': 'ba',  'び': 'bi',  'ぶ': 'bu',  'べ': 'be',  'ぼ': 'bo',  'ぱ': 'pa',  'ぴ': 'pi',  'ぷ': 'pu',
'ぺ': 'pe',  'ぽ' : 'po'}

#list of every japanese hiraganas Yōon combination linked to their romaji like きゃ -> kya in order and close when the list is finished
hiraganas_yoon = {'きゃ': 'kya', 'きゅ': 'kyu', 'きょ': 'kyo', 'ぎゃ': 'gya', 'ぎゅ': 'gyu', 'ぎょ': 'gyo', 'しゃ': 'sha', 'しゅ': 'shu',
'じ': 'ji', 'しょ': 'sho', 'ちゃ': 'cha', 'ちゅ': 'chu', 'ちょ': 'cho', 'ぢゃ': 'dya', 'ぢゅ': 'dyu', 'ぢょ': 'dyo', 'ひゃ': 'hya',
'ひゅ': 'hyu', 'ひょ': 'hyo', 'びゃ': 'bya', 'びゅ': 'byu', 'びょ': 'byo', 'ぴゃ': 'pya', 'ぴゅ': 'pyu', 'ぴょ': 'pyo', 'みゃ': 'mya',
'みゅ': 'myu', 'みょ': 'myo', 'りゃ': 'rya', 'りゅ': 'ryu', 'りょ': 'ryo', 'ぎゅ': 'gyu', 'ぢゅ': 'dyu', 'ひゅ': 'hyu', 'びゅ': 'byu',
'ぴゅ': 'pyu', 'みゅ': 'myu', 'りゅ': 'ryu', 'ぎょ': 'gyo', 'ぢょ': 'dyo', 'ひょ': 'hyo', 'びょ': 'byo', 'ぴょ': 'pyo', 'みょ': 'myo',
'りょ': 'ryo'}

 #list of every katakanas in japanese characters linked to their romaji and close when the list is finished
katakanas = {   'ア': 'a',  'イ': 'i',  'ウ': 'u',  'エ': 'e',  'オ': 'o',  'カ': 'ka',  'キ': 'ki',  'ク': 'ku',  'ケ': 'ke',
'コ': 'ko',  'サ': 'sa',  'シ': 'shi',  'ス': 'su',  'セ': 'se',  'ソ': 'so',  'タ': 'ta',  'チ': 'chi',  'ツ': 'tsu',  'テ': 'te',
'ト': 'to',  'ナ': 'na',  'ニ': 'ni',  'ヌ': 'nu',  'ネ': 'ne',  'ノ': 'no',  'ハ': 'ha',  'ヒ': 'hi',  'フ': 'fu',  'ヘ': 'he',
'ホ': 'ho',  'マ': 'ma',  'ミ': 'mi',  'ム': 'mu',  'メ': 'me',  'モ': 'mo',  'ヤ': 'ya',  'ユ': 'yu',  'ヨ': 'yo',  'ラ': 'ra',
'リ': 'ri',  'ル': 'ru',  'レ': 're',  'ロ': 'ro',  'ワ': 'wa',  'ヲ': 'wo',  'ン': 'n',  'ガ': 'ga',  'ギ': 'gi',  'グ': 'gu',
'ゲ': 'ge',  'ゴ': 'go',  'ザ': 'za',  'ジ': 'ji',  'ズ': 'zu',  'ゼ': 'ze',  'ゾ': 'zo',  'ダ': 'da',  'ヂ': 'ji',  'ヅ': 'zu',
'デ': 'de',  'ド': 'do',  'バ': 'ba',  'ビ': 'bi',  'ブ': 'bu',  'ベ': 'be',  'ボ': 'bo',  'パ': 'pa',  'ピ': 'pi',  'プ': 'pu',
'ペ': 'pe',  'ポ': 'po'}

#list of every japanese katakanas Yōon combination linked to their romaji like キャ -> kya in order and close when the list is finished
katakanas_yoon = {'キャ': 'kya', 'キュ': 'kyu', 'キョ': 'kyo', 'ギャ': 'gya', 'ギュ': 'gyu', 'ギョ': 'gyo', 'シャ': 'sha', 'シュ': 'shu',
'ジ': 'ji', 'ショ': 'sho', 'チャ': 'cha', 'チュ': 'chu', 'チョ': 'cho', 'ヂャ': 'dya', 'ヂュ': 'dyu', 'ヂョ': 'dyo', 'ヒャ': 'hya',
'ヒュ': 'hyu', 'ヒョ': 'hyo', 'ビャ': 'bya', 'ビュ': 'byu', 'ビョ': 'byo', 'ピャ': 'pya', 'ピュ': 'pyu', 'ピョ': 'pyo', 'ミャ': 'mya',
'ミュ': 'myu', 'ミョ': 'myo', 'リャ': 'rya', 'リュ': 'ryu', 'リョ': 'ryo', 'ギュ': 'gyu', 'ヂュ': 'dyu', 'ヒュ': 'hyu', 'ビュ': 'byu',
'ピュ': 'pyu', 'ミュ': 'myu', 'リュ': 'ryu', 'ギョ': 'gyo', 'ヂョ': 'dyo', 'ヒョ': 'hyo', 'ビョ': 'byo', 'ピョ': 'pyo', 'ミョ': 'myo',
'リョ': 'ryo'}







#Rassembler tous les dictionnaires en un seul dictionnaire
dictionnaire = {**hiraganas, **hiraganas_yoon} #**katakanas, #**katakanas_yoon

while game is True:

    kana, phonetique = random.choice(list(dictionnaire.items()))
    print(kana)

    reponse = input("Quel est la phonétique de ce kana ? ")
    if reponse == phonetique:
        print("Bravo, la réponse est juste !")
        print("")
    elif phonetique is not reponse:
        print("Réesayez !")
        print("")
    
