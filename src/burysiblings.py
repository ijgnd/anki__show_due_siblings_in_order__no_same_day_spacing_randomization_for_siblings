# -*- coding: utf-8 -*-

# Add-on for Anki that modifies the function _burySiblings
#
# Copyright: - 2019 ijgnd
#            - 2019 Thomas Kahn
#            - Ankitects Pty Ltd and contributors
#
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html


from pprint import pprint as pp

from anki import version
from anki.hooks import addHook, wrap
from anki.lang import getLang
from anki.sched import Scheduler as schedv1
from anki.utils import ids2str, intTime

import aqt
from aqt import mw
from aqt.utils import showInfo, tooltip
from aqt.qt import *

anki20 = version.startswith("2.0.")
if not anki20:
    from anki.schedv2 import Scheduler as schedv2


from .texts import *


if getLang() == "de":
    LANG = "de"
else:
    LANG = "en"


def siblings_in_order(queue, did):
    if nospacing:
        return True
    else:
        conf = mw.col.decks.get(did)['conf']
        if queue == 2:
            if no_sa_da_spa_rev.get(str(conf), False):
                return True
        else:
            if no_sa_da_spa_new.get(str(conf), False):
                return True


def my_burySiblings(self, card):
    toBury = []
    nconf = self._newConf(card)
    buryNew = nconf.get("bury", True)
    rconf = self._revConf(card)
    buryRev = rconf.get("bury", True)
    if hasattr(card, 'odid'):
        did = card.odid
        if not card.odid:   # == 0
            did = card.did
    else:
        did = card.did
    # loop through and remove from queues
    for cid, queue in self.col.db.execute("""
select id, queue from cards where nid=? and id!=?
and (queue=0 or (queue=2 and due<=?))""",
            card.nid, card.id, self.today):
        if queue == 2:  # review
            if buryRev:
                toBury.append(cid)
            # if bury disabled, we maybe discard to give same-day spacing
            if not siblings_in_order(queue, did):
                try:
                    self._revQueue.remove(cid)
                except ValueError:
                    pass
        else:
            if buryNew:
                toBury.append(cid)
            # if bury disabled, we maybe discard to give same-day spacing
            if not siblings_in_order(queue, did):
                try:
                    self._newQueue.remove(cid)
                except ValueError:
                    pass
    # then bury
    if toBury:
        if not anki20 and self.col.schedVer() != 1:
            self.buryCards(toBury, manual=False)
        else:
            self.col.db.execute(
                "update cards set queue=-2,mod=?,usn=? where id in "+ids2str(toBury),
                intTime(), self.col.usn())
            self.col.log(toBury)
schedv1._burySiblings = my_burySiblings
if not anki20:
    schedv2._burySiblings = my_burySiblings




def onProfileLoaded():
    global no_sa_da_spa_new
    global no_sa_da_spa_rev
    if '268644742_no_intraday_spacing_New_dconfs' in mw.col.conf:
        no_sa_da_spa_new = mw.col.conf['268644742_no_intraday_spacing_New_dconfs']
    else:
        no_sa_da_spa_new = {}
        mw.col.conf['268644742_no_intraday_spacing_New_dconfs'] = {}
        mw.col.setMod()
    if '268644742_no_intraday_spacing_Rev_dconfs' in mw.col.conf:
        no_sa_da_spa_rev = mw.col.conf['268644742_no_intraday_spacing_Rev_dconfs']
    else:
        no_sa_da_spa_rev = {}
        mw.col.conf['268644742_no_intraday_spacing_Rev_dconfs'] = {}
        mw.col.setMod()
addHook('profileLoaded', onProfileLoaded)




def toggle_bury_new(self):
    if self.form.bury.isChecked():   # this checks the state after the change
        self.form.cb_no_sa_da_spa_new.setChecked(False)
        self.form.cb_no_sa_da_spa_new.setEnabled(False)
    else:
        self.form.cb_no_sa_da_spa_new.setEnabled(True)
aqt.deckconf.DeckConf.toggle_bury_new = toggle_bury_new


def toggle_bury_rev(self):
    if self.form.bury.isChecked():   # this checks the state after the change
        self.form.cb_no_sa_da_spa_rev.setChecked(False)
        self.form.cb_no_sa_da_spa_rev.setEnabled(False)
    else:
        self.form.cb_no_sa_da_spa_rev.setEnabled(True)
aqt.deckconf.DeckConf.toggle_bury_rev = toggle_bury_rev


def setupUi(self, Dialog):
    # don't hardcode rows as in Load Balancer because then they are not compatible
    # new
    self.cb_no_sa_da_spa_new = QCheckBox(t_dc_label[LANG])
    self.cb_no_sa_da_spa_new.setToolTip(t_dc_explan[LANG])
    self.gridLayout.addWidget(self.cb_no_sa_da_spa_new, self.gridLayout.rowCount(), 0, 1, 3)
    # rev
    self.cb_no_sa_da_spa_rev = QCheckBox(t_dc_label[LANG])
    self.cb_no_sa_da_spa_rev.setToolTip(t_dc_explan[LANG])
    self.gridLayout_3.addWidget(self.cb_no_sa_da_spa_rev, self.gridLayout_3.rowCount(), 0, 1, 3)


def loadConf(self):
    global no_sa_da_spa_new
    global no_sa_da_spa_rev
    self.form.cb_no_sa_da_spa_new.setChecked(no_sa_da_spa_new.get(str(self.conf['id']), False))
    self.form.cb_no_sa_da_spa_rev.setChecked(no_sa_da_spa_rev.get(str(self.conf['id']), False))
    self.form.bury.clicked.connect(self.toggle_bury_new)
    self.toggle_bury_new()
    self.form.buryRev.clicked.connect(self.toggle_bury_rev)
    self.toggle_bury_rev()


def saveConf(self):
    global no_sa_da_spa_new
    global no_sa_da_spa_rev
    nosamedayNew = self.form.cb_no_sa_da_spa_new.isChecked()
    nosamedayRev = self.form.cb_no_sa_da_spa_rev.isChecked()
    no_sa_da_spa_new[str(self.conf['id'])] = nosamedayNew
    no_sa_da_spa_rev[str(self.conf['id'])] = nosamedayRev
    mw.col.conf['268644742_no_intraday_spacing_New_dconfs'][str(self.conf['id'])] = nosamedayNew
    mw.col.conf['268644742_no_intraday_spacing_Rev_dconfs'][str(self.conf['id'])] = nosamedayRev
    mw.col.setMod()
    pp(mw.col.conf)


aqt.forms.dconf.Ui_Dialog.setupUi = wrap(aqt.forms.dconf.Ui_Dialog.setupUi, setupUi, pos="after")
aqt.deckconf.DeckConf.loadConf = wrap(aqt.deckconf.DeckConf.loadConf, loadConf, pos="after")
aqt.deckconf.DeckConf.saveConf = wrap(aqt.deckconf.DeckConf.saveConf, saveConf, pos="before")





nospacing = False
def toggleSameDaySpacing():
    global nospacing
    nospacing ^= True
    # don't remember this:
    # mw.col.conf['268644742_intraday_spacing_global_override'] ^= True
    # mw.col.setMod()
    # mw.reset()
    if nospacing:
        showInfo(t_menu_toggle[LANG])


menu_added = 0
def add_same_day_spacing_to_menu():
    global menu_added
    menu_added += 1
    if not menu_added > 1:
        menu = None
        for a in mw.form.menubar.actions():
            if t_menu[LANG] == a.text():
                menu = a.menu()
                menu.addSeparator()
                break
        if not menu:
            menu = mw.form.menubar.addMenu(t_menu[LANG])
        a = menu.addAction(t_menu_entry[LANG])
        a.setCheckable(True)
        a.setChecked(nospacing)
        a.toggled.connect(toggleSameDaySpacing)
addHook('profileLoaded', add_same_day_spacing_to_menu)
