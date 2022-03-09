def read_file(filename):   #讀取檔案
    lines = []
    with open(filename, 'r', encoding='utf-8-sig')as f: #怪符號用-sig
        for line in f:
            lines.append(line.strip('\n'))
    return lines
    

def count(lines):
    new = []
    person = None  #none適合用來當作預設值
    allen_word_count = 0
    allen_sticker_count = 0
    allen_picture_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_picture_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_picture_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m) 
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_picture_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print('Allen說了: ', allen_word_count, '個字', allen_sticker_count, '個貼圖', allen_picture_count, '個圖片')
    print('Viki說了: ', viki_word_count, '個字', viki_sticker_count, '個貼圖', viki_picture_count, '個圖片')


# def write_file(filename, lines):
#     with open(filename, 'w')as f:
#         for line in lines:
#             f.write(line + '\n')


def main():
    lines = read_file('LINE-Viki.txt')  #檔名用參數較好
    count(lines)
    (lines)
    # write_file('lineoutput.txt', lines)
main()
