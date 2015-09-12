import subprocess
import shlex

class Util(object):
    @classmethod
    def getWifiNames(cls):
        cards = Util.getWirelessCards()
        if len(cards) < 1:
            return None
        cmds = [ 'iwlist ' + cards[0] + ' scan', 'grep ESSID', 'awk -F\\\" \'{print $2}\'']
        return Util.runPipedCmds(cmds) 
    
    @classmethod
    def getWifiNamesByCard(cls, card):
        cmds = [ 'iwlist ' + card + ' scan', 'grep ESSID', 'awk -F\\\" \'{print $2}\'']
        return Util.runPipedCmds(cmds) 

    @classmethod
    def getWirelessCards(cls):
        cmds = ['sudo airmon-ng', 'awk \'{print $2}\'']
        ret = []
        for x in Util.runPipedCmds(cmds).split('\n')[1:]:
            if len(x) > 0:
                ret.append(x)
        return ret 
       
    
    @classmethod
    def runPipedCmds(cls,cmds):
        if len(cmds) < 1:
            return None
        plist = []
        cmd0 = cmds[0]
        p0 = subprocess.Popen(shlex.split(cmd0),stdout = subprocess.PIPE)
        plist.append(p0)
        for cmd in cmds[1:]:
            pn = subprocess.Popen(shlex.split(cmd),stdin=plist[-1].stdout, stdout = subprocess.PIPE)
            plist.append(pn)
        out,err = plist[-1].communicate()
        return out
