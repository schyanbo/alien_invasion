import sys
import pygame
from bullet import Bullet
from alien import Alien
def check_keydown_events(event,ai_settings, screen, ship, bullets):
    """响应按键"""
    #printf(event.key)
    if event.key ==pygame.K_RIGHT:
        #向右移动飞船
#                ship.rect.centerx += 1
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #创建一颗子弹，并将其加入Bullets中
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        
def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有达到子弹限制，就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    
        
def check_keyup_events(event,ship):
    """响应键松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        
def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
                    
def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    #更新屏幕上的图像，并切换到新屏幕
    #每次循环时都重绘屏幕
    #screen.fill(bg_color)
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    for alien in aliens.sprites():
        alien.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()
    
def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    #更新子弹的位置
    bullets.update()
    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    #print(len(bullets))

def get_no_aliens_x(ai_settings, alien_width):
    """计算每行可以容纳多少外星人"""
    width_btw_alien = 1.5*alien_width
    available_space_x = ai_settings.screen_width - width_btw_alien
    number_aliens_x = int(available_space_x/width_btw_alien)
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    width_btw_alien = 1.5*alien_width
    alien.x = alien_width + width_btw_alien*alien_number
    alien.rect.x = alien.x
    aliens.add(alien)
    
def create_fleet(ai_settings, screen, aliens):
    """创建外星人群"""
    #创建外星人群
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_no_aliens_x(ai_settings, alien.rect.width)
    #创建第一行外星人
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen,aliens, alien_number)

