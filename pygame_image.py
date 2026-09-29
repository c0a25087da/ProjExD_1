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
    kk_rct = kk_img.get_rect() #10-1こうかとんRectの取得
    kk_rct.center = 300, 200 #10-2こうかとんRectの初期座標の設定
    tmr = 0
    sum_y = 0
    sum_x = 0
    while True:
        y1 = 0
        y2 = 0
        x1 = 0
        x2 = 0
        x = tmr%3200 #練習9 3199までいったら0に戻る背景のループ
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        key_lst = pg.key.get_pressed() #10-3全キーの押下状態を取得
        #print(key_lst)
        kk_rct.move_ip((-1, 0))
        
        if key_lst[pg.K_UP]: #10-4矢印キーでこうかとんが移動
            y1 = -1
        if key_lst[pg.K_DOWN]:
            y2 = 1
        if key_lst[pg.K_RIGHT]:
            x1 = 2
        if key_lst[pg.K_LEFT]:
            x2 = -1
        
        sum_x = x1 + x2
        
        sum_y = y1 + y2
        
        kk_rct.move_ip((0+sum_x, 0+sum_y))

        
        screen.blit(bg_img, [-x, 0]) #練習5背景画像を右から左へ
        screen.blit(bg_reverse_img, [-x+1600, 0]) #反転した背景画像の貼り付け
        screen.blit(bg_img, [-x+3200, 0]) #練習9
        screen.blit(kk_img, kk_rct) #練習4こうかとんのはりつけ
        pg.display.update()
        tmr += 1        
        clock.tick(200) #FPS変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()