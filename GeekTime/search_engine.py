"""
    Create a simple search engine:搜索器、索引器、检索器和用户接口
    语料(corpus)、倒序索引(inverted index)
    模拟敏捷开发过程中的迭代开发流程

"""
import re


class SearchEngineBase:  # 搜索引擎基类
    def __init__(self):
        pass

    # 读取文件内容，将文件路径作为ID，和内容一起送到process_corpus
    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    # 对内容进行处理和保存，处理后的内容称为索引（index）
    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented.')

    # 给定一个询问，处理询问，再通过索引检索，然后返回
    def search(self, query):
        raise Exception('search not implemented')


def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input()
        if query == 'quitquitquit':
            break
        results = search_engine.search(query)
        print(f'found {len(results)} result(s)')
        for result in results:
            print(result)


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results


class BOWEngine(SearchEngineBase):
    def __init__(self):
        super().__init__()
        self.__id_to_words = {}

    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)

    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results

    @staticmethod
    def query_match(query_words, words):
        for query_words in query_words:
            if query_words not in words:
                return False
        return True

    @staticmethod
    def parse_text_to_words(text):
        #  使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w]', ' ', text)
        #  转为小写
        text = text.lower()
        #  生成所有单词的列表
        word_list = text.split(' ')
        #  去除空白单词
        word_list = filter(None, word_list)
        #  返回单词的set
        return set(word_list)


class BOWInvertedIndexEngine(SearchEngineBase):
    def __init__(self):
        super(BOWInvertedIndexEngine, self).__init__()
        self.inverted_index = {}

    def process_corpus(self, idw, text):
        words = self.parse_text_to_words(text)
        for word in words:
            if word not in self.inverted_index:
                self.inverted_index[word] = []
            self.inverted_index[word].append(idw)

    def search(self, query):
        query_words = list(self.parse_text_to_words(query))
        query_words_index = list()
        for query_word in query_words:
            query_words_index.append(0)

        # 如果某一个查询单词的倒序索引为空，立刻返回
        for query_word in query_words:
            if query_word not in self.inverted_index:
                return []
        result = []
        while True:

            # 首先获得当前状态下的所有倒序索引的index
            current_ids = []

            for idx, query_word in enumerate(query_words):
                current_index = query_words_index[idx]
                current_inverted_list = self.inverted_index[query_word]

                # 已经遍历到了某一个倒序索引的末尾，结束search
                if current_index >= len(current_inverted_list):
                    return result

                current_ids.append(current_inverted_list[current_index])

            # 然后，如果current_ids的所有元素都一样，那么表明这个单词在这个元素对应的文档中出现
            if all(x == current_ids[0] for x in current_ids):
                result.append(current_ids[0])
                query_words_index = [x + 1 for x in query_words_index]
                continue

            # 如果不是，最小的元素加1
            min_val = min(current_ids)
            min_val_pos = current_ids.index(min_val)
            query_words_index[min_val_pos] += 1

    @staticmethod
    def parse_text_to_words(text):
        #  使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w]', ' ', text)
        #  转为小写
        text = text.lower()
        #  生成所有单词的列表
        word_list = text.split(' ')
        #  去除空白单词
        word_list = filter(None, word_list)
        #  返回单词的set
        return set(word_list)


if __name__ == "__main__":
    # simple_engine = SimpleEngine()
    # main(simple_engine)
    # bow_engine = BOWEngine()
    # main(bow_engine)
    bii_engine = BOWInvertedIndexEngine()
    main(bii_engine)
