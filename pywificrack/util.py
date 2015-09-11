import subprocess
import shlex

class Util(object):
    @classmethod
    def getWifiName(self):
        cmd0 = 'iwlist wlp3s0mon scan'
        cmd1 = 'grep ESSID'
        cmd2 = 'awk -F\\\" \'{print $2}\''
        p0 = subprocess.Popen(shlex.split(cmd0), stdout = subprocess.PIPE)
        p1 = subprocess.Popen(shlex.split(cmd1), stdin = p0.stdout, stdout = subprocess.PIPE)
        p2 = subprocess.Popen(shlex.split(cmd2), stdin = p1.stdout, stdout = subprocess.PIPE)
        out,err = p2.communicate()
        print out
