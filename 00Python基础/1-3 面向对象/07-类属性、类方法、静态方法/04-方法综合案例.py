class Game(object):
    top_score = 0

    def __init__(self, player_game):
        self.player_game = player_game

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        print("历史记录%d" % cls.top_score)

    def start_game(self):
        print("%s开始游戏了" % self.player_game)


# 查看游戏的帮助信息
Game.show_help()
# 查看历史最高分
Game.show_top_score()
# 创建游戏对象
game = Game("小明")
game.start_game()

