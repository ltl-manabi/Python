def clean_text(text):
    import string
    import re
    import mojimoji as mj
    import unicode_script_map as usm
    from unicode_script import ScriptType

    text = mj.zen_to_han(text, kana=False)  # 全角英数字を半角に変換
    text = text.lower()
    text = re.sub('\n', '', text)  # 改行文字の除去
    #text = "".join([c if usm.get_script_type(c) != ScriptType.U_Common or c == '\u30fc' or c in string.digits else ' ' for c in text])  # 記号類を除去
    text = re.sub('(.)\\1{3,}', ' ', text)  # 草を枯らす
    text = re.sub('^ ', '', text)  # 行頭のスペースを削除する
    text = re.sub(' $', '', text)  # 行末のスペースを削除する

    return(text)


def parse_text(file):
    import re
    res_lines = []

    with open(file, 'r') as f:
        lines = f.readlines()
        lines = lines[2:]  # 1行目と2行目を除去する
        for line in lines:
            lfonly = re.search('^\n$', line)  # リストの要素が改行のみ (空行) であるか
            if lfonly:
                continue  # 空行であった場合処理をスキップする
            res_line = clean_text(line)    
            res_lines.append(res_line)
            res = ' '.join(res_lines)
    return(res)
