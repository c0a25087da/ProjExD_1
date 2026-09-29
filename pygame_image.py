import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_reverse_img = pg.transform.flip(bg_img, True, False) #背景画像の左右反転
    kk_img = pg.image.load("fig/3.png") #練習3こうかとん画像の貼り付け
    kk_img = pg.transform.flip(kk_img, True, False) #練習3こうかとんの左右反転
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200 #練習9 3199までいったら0に戻る背景のループ
        screen.blit(bg_img, [-x, 0]) #練習5背景画像を右から左へ
        screen.blit(bg_reverse_img, [-x+1600, 0]) #反転した背景画像の貼り付け
        screen.blit(bg_img, [-x+3200, 0]) #練習9
        screen.blit(kk_img, [300, 200]) #練習4こうかとんのはりつけ
        pg.display.update()
        tmr += 1        
        clock.tick(200) #FPS変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()