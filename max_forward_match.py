import re
import os


def max_fd_match(sent,word_list):
    """

    :param sent: 句子
    :param word_dict: 词典
    :return:分词后列表
    """

    word_len = [len(word) for word in word_list]
    maxlen = max(word_len)
    cut_word = []
    i = 0
    nlen = maxlen
    while i < len(sent) and nlen >0 :
        word = sent[i:i+nlen]
        print(word)
        if word in word_list:
            cut_word.append(word)
            i = i + nlen
            nlen = maxlen
        else:
            if len(word) == 2:
                cut_word.append(word)
                i = i + nlen
                nlen = maxlen
            else:
              nlen = nlen -1
    return cut_word



if __name__ == '__main__':
    word_dict = ['新华网', '日本', '记者', '行政', '改革', '二战', '靖国神社', '内阁', '东京', '中国', '韩国', '亚洲', '国家','关系']
    test_str = '''新华网东京电记者吴谷丰据日本共同社28日报道，日本行政改革担当大臣稻田朋美当天参拜了供
    奉有二战甲级战犯牌位的靖国神社。她成为第四个参拜靖国神社的安倍内阁成员。    靖国神社位于东京千代田区，供奉
    有包括东条英机在内的14名第二次世界大战甲级战犯的牌位。长期以来，日本部分政客参拜靖国神社，导致日本与中国、韩国等亚洲国家关系'''
    print(max_fd_match(test_str, word_dict))