from anki.lang import getLang

if getLang() == "de":
    LANG = "de"
else:
    LANG = "en"


t_dc_label = {
    "en": "Show sibling cards (= cards belonging to the same note) right after each other",
    "de": "Karten, die zu derselben Notiz gehören, unmittelbar nacheinander abfragen",
}


t_dc_explan = {
    "en": (u"Say you have note1 (with the new cards 1,2,3) and note2 (with the new"
           u"cards A,B). By default Anki will show you the cards in this mixed order: 1, A, 2, B, "
           u"3. If the option \"%s\" is enabled the order will be: 1, 2, "
           u"3, A, B.<br><br>This function is disabled (greyed out) when you have checked"
           u"\"Bury related new cards until the next day\"." % t_dc_label[LANG]),
    "de": (u"<b></b>Angenommen man hat eine Notiz1 (mit den neuen Karten 1,2,3) und eine Notiz2 "
           u"(mit den Karten A,B). Dann wird Anki standardmäßig diese neuen Karten in folgender "
           u"gemischter Reihenfolge anzeigen: 1, A, 2, B, 3. Wenn die Option \"%s\" aktiviert ist, "
           u"gilt diese Reihenfolge: 1, 2, 3, A, B.<br><br>Diese Option ist deaktviert "
           u"(ausgegraut) wenn die Option \"Verwandte neue Karten nicht am selben Tag lernen, "
           u"sondern bis zum Folgetag zurückstellen\" aktiviert ist." % t_dc_label[LANG]),
}


t_menu = {
    "en": "&Study",
    "de": "&Lernen",
}


t_menu_entry = {
    "en": u'no same-day spacing for siblings/show due siblings in order (ignore deck settings)',
    "de": u'Zusammengehörende Karten direkt nacheinander abfragen (Deckeinstellungen ignorieren)',
}


t_menu_toggle = {
    "en": (u"Option has been activated! Sibling Cards (= cards belonging to the same note) "
           u"will now always be asked right after each other and the deck setting for this "
           u"option will be ignored/overriden.<br><br>"
           u"To put the review of specific "
           u"cards off until tomorrow press the \"-\"-key when you are asked about them. "
           u"This makes sense in situations where you've just been asked: \"What does 'Kuchen' "
           u"mean in Englisch?\" And the next question is: \"What does 'cake' mean in "
           u"German?\"<br><br>"
           u"More information about this option can be found on the page "
           u"<a href=\"https://ankiweb.net/shared/info/268644742\">"
           u"of the corresponding Anki-Add-On</a>."),
    "de": (u"Option aktiviert! Karten, die zu derselben Notiz gehören, werden "
           u"jetzt immer unmittelbar nacheinander abgefragt und die deck-spezifischen "
           u"Einstellungen werden ignoriert/übergangen.<br><br>"
           u"Um bestimmte einzelne Karten erst morgen abfragen zu lassen, kannst du, "
           u"wenn du danach gefragt wirst, einfach die \"-\"-Taste (Bindestrich-Taste) "
           u"auf deiner Tastatur drücken. Das ist z.B. sinnvoll, wenn du gerade gefragt "
           u"wurdest: \"Was heißt 'Kuchen' auf Englisch?\" Und dann direkt danach: \"Was "
           u"bedeutet 'cake' auf Deutsch?\"<br><br>Weitere Infos zu dieser Funktion findest "
           u"du auf der Seite <a href=\"https://ankiweb.net/shared/info/268644742\">des "
           u"dazugehörigen Anki-Addons</a>.")
}
