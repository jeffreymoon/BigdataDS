
"""
Python Basic Lab 1-1
Word Count with 2 lists
without 'dict'

word_cnt_list(path)
    interface that interacts with user

word_cnt_db(path)
    making 2 lists 'words' and 'cnts'
"""
import re

def word_cnt_db(path):
    """
    :param path: path of file
    :return: [words, cnts]
    """
    # try open file at 'path' (parameter)
    try:
    # making 2 lists words & cnts
    # words's index and cnts's index are corresponding
        fh = open(path)
        words = list()  # store words (dict's key)
        cnts = list()  # store counts (dict's val)
        
        for line in fh:
            word_list = line.split()
            # print(word_list)
            for word in word_list:
                if ':' in word:
                    continue
                word = re.sub(pattern='[,.?;:]', repl='', string=word)
                word = word.strip()
                if len(word) < 1:
                    continue
                
                # print(word)
                if not word in words:
                    words.append(word)
                    cnts.append(1)
                else:
                    cnts[words.index(word)] += 1
                    
    except:
        print("There is no filename")
        exit(0)

    # CAUTION : word's len < 1
    #           end with white space or [, . ? : ; ' " \n]
    #           ignore n:n
    #           be careful '\n' : using strip()

    return [words, cnts]


def word_cnt_list(path):
    """
    :param path: path file
    :return: None
    """
    # use 'word_cnt_db(path)' get Database
    wcd = word_cnt_db(path)
    wordList = wcd[0]
    wordCountList = wcd[1]

    # while user enter "EXITprogram" get word to find
    # CAUTION : get input without prompt
    #   -> just call input() not input( 'anything' )

    # CAUTION : if there are no 'word2find' in words print '0'

    # exit program
    # CAUTION : if user enter 'EXITprogram', then print 'exit'

    while (True):
        text = input()
        if text == "EXITprogram":
            print("exit")
            # top_words = list()
            # top_count = list()
            # for _ in range(10):
            #     top_cnt = max(wordCountList)
            #     top_word = wordList[(wordCountList).index(top_cnt)]
            #     top_words.append(top_word)
            #     top_count.append(top_cnt)
            #     wordCountList.pop(top_cnt)
            #     wordList.pop(top_word)
            # print(top_words, top_count)
            return

        if text in wordList:
            idx = (wordList).index(text)
            print(wordCountList[idx])
        else:
            print(0)
    exit(0)


if __name__ == '__main__':
    path = './genesis.txt'
    word_cnt_list(path)
