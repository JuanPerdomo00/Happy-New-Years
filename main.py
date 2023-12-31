#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===

from cansii import CAnsii as clr


def apply_colors_to_ascii(ascii_art, colors_lst):
    for _ in range(1, 366):
        clr.color_in_ascii(ascii_art, 0.5, colors_lst)


ascii_art = '''
 _   _    __    ____  ____  _  _    _  _  ____  _    _    _  _  ____    __    ____  ___ 
( )_( )  /__\  (  _ \(  _ \( \/ )  ( \( )( ___)( \/\/ )  ( \/ )( ___)  /__\  (  _ \/ __)
 ) _ (  /(__)\  )___/ )___/ \  /    )  (  )__)  )    (    \  /  )__)  /(__)\  )   /\__ \\
(_) (_)(__)(__)(__)  (__)   (__)   (_)\_)(____)(__/\__)   (__) (____)(__)(__)(_)\_)(___/
                                                                               
 ____  _  _     ____   __    _  _  ____  ____  _  _  ___                                
(  _ \( \/ )   (_  _) /__\  ( )/ )( ___)(  _ \( \/ )/ __)                               
 ) _ < \  /   .-_)(  /(__)\  )  (  )__)  )___/ \  / \__ \                               
(____/ (__)   \____)(__)(__)(_)\_)(____)(__)   (__) (___/     

God loves you so much!!! :)
'''


if __name__ == "__main__":
    try:
        colors = (clr.BLUE, clr.CYAN, clr.GREEN, clr.RED,clr.YELLOW, clr.MAGENTA)  
        apply_colors_to_ascii(ascii_art, colors)
    except KeyboardInterrupt:
        print(clr.green_underline("\nBye... :)"))
