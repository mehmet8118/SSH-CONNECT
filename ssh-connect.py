from pexpect import pxssh
import os,sys

def baglan(command):
    s = pxssh.pxssh()
    if not s.login('ip', 'ad', 'sifre'):
        print("SSH session failed on login.")
        print(str(s))
    else:
        print("Baglanti saglandi...\n\n")
        s.sendline(str(command))
        s.prompt()  # match the prompt
        print(s.before.decode("utf-8"))


os.system("clear")
while 1:

    command = input("\n\n==>")
    baglan(command)
    continue

