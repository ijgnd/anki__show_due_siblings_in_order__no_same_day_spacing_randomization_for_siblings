# Add-on for Anki that modifies the function _burySiblings
#
# Copyright: 2019 ijgnd
#            2018-2019 Lovac42
#            Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html


from anki.hooks import addHook
from anki.lang import getLang
from anki.sched import Scheduler as schedv1
from anki.schedv2 import Scheduler as schedv2
from anki.utils import ids2str, intTime

from aqt import mw
from aqt.utils import showInfo, tooltip
from aqt.qt import *

from .texts import t


def gc(arg, fail=False):
    return mw.addonManager.getConfig(__name__).get(arg, fail)


def wc(arg, val):
    config = mw.addonManager.getConfig(__name__)
    config[arg] = val
    mw.addonManager.writeConfig(__name__, config)


def my_burySiblings(self, card):
    toBury = []
    nconf = self._newConf(card)
    buryNew = nconf.get("bury", True)
    rconf = self._revConf(card)
    buryRev = rconf.get("bury", True)
    # loop through and remove from queues
    for cid, queue in self.col.db.execute("""
select id, queue from cards where nid=? and id!=?
and (queue=0 or (queue=2 and due<=?))""",
            card.nid, card.id, self.today):
        if queue == 2:
            trytoremove = True
            if nospacing:
                trytoremove = False
            if buryRev and not gc("override deck bury options"):
                toBury.append(cid)
                trytoremove = True
            if trytoremove:
            # if bury disabled, we still discard to give same-day spacing
                try:
                    self._revQueue.remove(cid)
                except ValueError:
                    pass
        else:
            trytoremove = True
            if nospacing:
                trytoremove = False
            if buryNew and not gc("override deck bury options"):
                toBury.append(cid)
                trytoremove = True
            if trytoremove:
            # if bury disabled, we still discard to give same-day spacing
                try:
                    self._newQueue.remove(cid)
                except ValueError:
                    pass
    # then bury
    if toBury:
        if self.col.schedVer() != 1:
            self.buryCards(toBury, manual=False)
        else:
            self.col.db.execute(
            "update cards set queue=-2,mod=?,usn=? where id in "+ids2str(toBury),
            intTime(), self.col.usn())
            self.col.log(toBury)
schedv1._burySiblings = my_burySiblings
schedv2._burySiblings = my_burySiblings



def toggleSameDaySpacing():
    global nospacing
    nospacing ^= True
    wc("enabled", nospacing)
    if nospacing:
        if gc("override deck bury options"):
            showInfo(t.togglemsg_with_override)
        else:
            showInfo(t.togglemsg)
    mw.reset()



def add_same_day_spacing_to_menu():
    menu = None
    for a in mw.form.menubar.actions():
        if t.menuname == a.text():
            menu=a.menu()
            menu.addSeparator()
            break
    if not menu:
        menu=mw.form.menubar.addMenu(t.menuname)
    a = menu.addAction(t.labelname)
    a.setCheckable(True)
    a.setChecked(nospacing)
    a.toggled.connect(toggleSameDaySpacing)


def onProfileLoaded():
    global nospacing
    nospacing = gc("enabled")
    if nospacing and not gc("hide startup warning"):
        if gc("override deck bury options"):
            tooltip(t.startup_reminder_ignore_decksettings)
        else:
            tooltip(t.startup_reminder)
    add_same_day_spacing_to_menu()
addHook('profileLoaded', onProfileLoaded)
