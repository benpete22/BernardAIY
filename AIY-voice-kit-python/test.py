#!/usr/bin/env python3

"""Bernard's speak and say"""
import aiy.audio
def main():
    while True:
        textinput = input("put what you want here: ")
        aiy.audio.say(textinput)
if __name__ == '__main__':
    main()
