#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@AUTHOR: Kalos Lazo
@GITHUB: lzmkalos
"""

import os;
from subprocess import PIPE,Popen;
from colorama import init, Fore,Back,Style;

from src.xorg import xorg_list;
from src.misc import misc_list;
from src.software import soft_list;

init(autoreset=True);

class Arch:
    """this class define the state and behavior of the arch installation"""
    span=f"{Fore.RED}==============================";
    FNULL = open(os.devnull, 'w');

    def __init__(self,lt:list[str])->None:
        self.lt=lt;
    
    def start_daemons(self)->None:
        print(f"\n{self.span}\n[!] Starting script...\n{self.span}");
        for l in self.lt:
            self.handle_install(l);
    
    def handle_install(self,lt:list[str])->None:
        print(f"\n{self.span}\n>> running daemons...\n{self.span}");
        for pkg in lt:
            print(f"\n> working on package [{Fore.RED}{pkg}{Fore.LIGHTWHITE_EX}] ...");
            cmd=f'sudo pacman -S {str(pkg)} --noconfirm --needed';
            pkg=Popen(cmd,shell=True,stdin=PIPE,stderr=PIPE);
            pkg.wait();
            print(f"{Fore.GREEN} Done!");
    
    def make_links(self)->None:
        folder_arr = ["alacritty", "macchina", "qtile", "rofi", "zathura", "starship"];
        for folder in folder_arr:
            print(f"\n> working on path [{Fore.RED}{folder}{Fore.LIGHTWHITE_EX}] ...");
            cmd=f'mkdir ~/.config/{str(folder)}';
            pkg=Popen(cmd,shell=True,stdin=PIPE,stderr=PIPE);
            pkg.wait();
            print(f"{Fore.GREEN} Done!");

def main()->None:
    pkg=[xorg_list, misc_list, soft_list];
    obj=Arch(pkg);
    obj.start_daemons();
    obj.make_links();

if __name__=="__main__":
    main();
