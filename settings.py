class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width=1280
        self.screen_height=760
        #灰色
        self.bg_color=(230,230,230)
        #蓝色
#        self.bg_color=(0,0,255)
        #飞船的设置
        self.ship_speed_factor = 10
        #子弹设置
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        #外星人设置
