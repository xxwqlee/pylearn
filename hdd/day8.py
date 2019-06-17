"""
    PorkGame: 21
    review oop
"""
import random


class Card:
    """"一张牌"""
    __slots__ = ('_suite', '_face')

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return f'{self._suite, face_str}'

    def __repr__(self):
        return self.__str__()


class Poker(object):  # without jokers
    """一副牌"""

    def __init__(self):
        self._cards = [Card(suite, face)  # has-a关系
                       for suite in '♠♥♣♦'
                       for face in range(1, 14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """洗牌(随机乱序)"""
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌"""
        return self._current < len(self._cards)


class Player(object):
    """玩家"""

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []
        self._wager = 1000

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        """摸牌"""
        self._cards_on_hand.append(card)

    def arrange(self, card_key):
        """玩家整理手上的牌"""
        self._cards_on_hand.sort(key=card_key)

    @staticmethod
    def get_key(card):
        return card.suite, card.face


class GameSimple21:

    def __init__(self, num_of_player):
        if not isinstance(num_of_player, int):
            raise Exception('num_of_player must be an integer.')
        if num_of_player < 2 or num_of_player > 6:
            raise Exception('num_of_player must be within range of 2-6')
        self._num_of_players = num_of_player
        self.players = [Player('庄家')]
        for i in range(1, num_of_player):
            self.players.append(Player(f'闲家{i}'))
        self.poker = Poker()

    def init_deal(self):
        self.poker.shuffle()
        for player in self.players:
            if player.name == '庄家':
                player.get(self.poker.next)
                # TODO：庄家有一张为暗牌
                player.get(self.poker.next)
                # TODO: 判断是否为BlackJack
            else:
                player.get(self.poker.next)
                player.get(self.poker.next)

    def show_card(self):
        for player in self.players:
            print(f"{player.name}: {player.cards_on_hand}")

    def bet(self):
        pass
        # TODO: 下注

    def hit(self):
        pass
        # TODO: 拿牌

    def buy_insurance(self):
        pass
        # TODO:买保险

    def double(self):
        pass
        # TODO: 加倍

    def surrender(self):
        pass
        # TODO: 投降


def deal_test():  # 排序规则-先根据花色再根据点数排序
    p = Poker()
    p.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    for _ in range(13):
        for player in players:
            player.get(p.next)
    for player in players:
        player.arrange(player.get_key)
        print(f"{player.name}: {player.cards_on_hand}")


if __name__ == '__main__':
    deal_test()
    new_game = GameSimple21(6)
    new_game.init_deal()
    new_game.show_card()
