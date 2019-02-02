'''
功能：人工降雪动态版
'''
import pygame
import random

# 初始化pygame
pygame.init()

# 根据背景图片的大小，设置屏幕长宽
SIZE = (1000, 700)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("下雪了")
background = pygame.image.load('snow1.jpg')

# 雪花列表
snow = []

# 初始化雪花：[x坐标, y坐标, x轴速度, y轴速度]
for i in range(300):
    x = random.randrange(0, SIZE[0])#SIZE[0]即1000
    y = random.randrange(0, SIZE[1])#SIZE[1]即700
    speedx = random.randint(-1, 2)#雪花飘落的x轴速度
    speedy = random.randint(2, 4)#雪花飘落的y轴速度
    snow.append([x, y, speedx, speedy])#加入到snow列表中

clock = pygame.time.Clock()

# 游戏主循环
done = False
while not done:
    # 消息事件循环，判断退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # screen.fill((0, 0, 0))#黑背景
    # 图片背景
    screen.blit(background, (0, 0))

    # 雪花列表循环
    for i in range(len(snow)):
        # 绘制雪花，颜色、位置、大小
        # snow[i][:2]表示第i个雪花的从0-1的切片，即x和y坐标
        #snow[i][3]表示第i个雪花的第3个元素，即y轴速度数值相等的圆半径
        pygame.draw.circle(screen, (255, 255, 255), snow[i][:2], snow[i][3])

        # 移动雪花位置（下一次循环起效）
        snow[i][0] += snow[i][2] #新x坐标是在原来x坐标的基础上+x轴速度
        snow[i][1] += snow[i][3] #新y坐标是在原来y坐标的基础上+y轴速度

        # 如果雪花落出屏幕，重设位置
        if snow[i][1] > SIZE[1]:#y坐标超出了y轴最大值700
            snow[i][1] = random.randrange(-10, 0)#重新设置y轴位置
            snow[i][0] = random.randrange(0, SIZE[0])#重新设置x轴位置

    # 刷新屏幕
    pygame.display.flip()
    clock.tick(20)

# 退出
pygame.quit()