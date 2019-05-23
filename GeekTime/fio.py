"""
    1 文件输入输出（NLP练习）
    2 JSON 序列化实战练习
"""
import re
import json


def parse(text):
    # 使用正则表达式去除标点符号和换行符
    text = re.sub(r'[^\w]', ' ', text)
    # 小写
    text = text.lower()
    # 生成所有单词的列表
    word_list = text.split(' ')
    # 去除空白单词
    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1
    # 按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)

    return sorted_word_cnt


def json_pra():
    params = {'symbol': '12345', 'type': 'limit', 'price': 123.4, 'amount': 23}
    params_str = json.dumps(params)

    print('after json serialization……')
    print(f'type of params_str = {type(params_str)}, params_str = {params_str}')

    original_params = json.loads(params_str)

    print('after json deserialization……')
    print(f'type of original_params = {type(original_params)}, original_params = {original_params}')


if __name__ == "__main__":
    with open('in.txt', 'r')as f_in:
        txt = f_in.read()
    word_and_freq = parse(txt)

    with open('out.txt', 'w')as f_out:
        for word, freq in word_and_freq:
            f_out.write(f'{word} {freq}\n')
    json_pra()
