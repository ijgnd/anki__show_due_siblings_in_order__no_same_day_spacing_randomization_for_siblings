# Add-on for Anki - check the description on Ankiweb or 
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# use this at your own risk

# Copyright: - 2019 ijgnd
#            - Ankitects Pty Ltd and contributors
#            - Thomas Kahn (German translations)


from types import SimpleNamespace

from anki.lang import getLang


if getLang().startswith("de"):
    LANG = "de"
else:
    LANG = "en"

at = {}

# at[""] = {
#     "en" = ""
#     "de" = ""
# }

at["togglemsg"] = {
    "en": ("Option has been activated! Sibling Cards (= cards belonging to the same note) "
           "will now be asked right after each other if you didn't enable 'Bury related "
           "new cards until the next day' in the deck settings.<br><br>"
           "To put the review of specific "
           "cards off until tomorrow press the \"-\"-key when you are asked about them. "
           "This makes sense in situations where you've just been asked: \"What does 'Kuchen' "
           "mean in Englisch?\" And the next question is: \"What does 'cake' mean in "
           "German?\"<br><br>"
           "More information about this option can be found on the page "
           "<a href=\"https://ankiweb.net/shared/info/268644742\">"
           "of the corresponding Anki-Add-On</a>."),
    "de": ("Option aktiviert! Karten, die zu derselben Notiz gehören, werden "
           "jetzt unmittelbar nacheinander abgefragt, sofern du in den Deckeinstellungen "
           "nicht \"Verwandte neue Karten nicht am selben Tag lernen\" aktiviert hast.<br><br>"
           "Um bestimmte einzelne Karten erst morgen abfragen zu lassen, kannst du, "
           "wenn du danach gefragt wirst, einfach die \"-\"-Taste (Bindestrich-Taste) "
           "auf deiner Tastatur drücken. Das ist z.B. sinnvoll, wenn du gerade gefragt "
           "wurdest: \"Was heißt 'Kuchen' auf Englisch?\" Und dann direkt danach: \"Was "
           "bedeutet 'cake' auf Deutsch?\"<br><br>Weitere Infos zu dieser Funktion findest "
           "du auf der Seite <a href=\"https://ankiweb.net/shared/info/268644742\">des "
           "dazugehörigen Anki-Addons</a>."),
}


at["togglemsg_with_override"] = {
    "en": ("Option has been activated! Sibling Cards (= cards belonging to the same note) "
           "will now be asked right after each other and according to your settings in the "
           "add-on config the deck settings for 'Bury related "
           "new cards until the next day' will be ignored.<br><br>"
           "To put the review of specific "
           "cards off until tomorrow press the \"-\"-key when you are asked about them. "
           "This makes sense in situations where you've just been asked: \"What does 'Kuchen' "
           "mean in Englisch?\" And the next question is: \"What does 'cake' mean in "
           "German?\"<br><br>"
           "More information about this option can be found on the page "
           "<a href=\"https://ankiweb.net/shared/info/268644742\">"
           "of the corresponding Anki-Add-On</a>."),
    "de": ("Option aktiviert! Karten, die zu derselben Notiz gehören, werden "
           "jetzt unmittelbar nacheinander abgefragt. Aufgrund deiner Einstellungen in "
           "der Add-on Konfiguration wird die Einstellung "
           "\"Verwandte neue Karten nicht am selben Tag lernen\" aus den Stapeleinstellungen "
           "ignoriert.<br><br>"
           "Um bestimmte einzelne Karten erst morgen abfragen zu lassen, kannst du, "
           "wenn du danach gefragt wirst, einfach die \"-\"-Taste (Bindestrich-Taste) "
           "auf deiner Tastatur drücken. Das ist z.B. sinnvoll, wenn du gerade gefragt "
           "wurdest: \"Was heißt 'Kuchen' auf Englisch?\" Und dann direkt danach: \"Was "
           "bedeutet 'cake' auf Deutsch?\"<br><br>Weitere Infos zu dieser Funktion findest "
           "du auf der Seite <a href=\"https://ankiweb.net/shared/info/268644742\">des "
           "dazugehörigen Anki-Addons</a>."),
}


at["menuname"] = {
    "en": "&Study",
    "de": "&Kartenreihenfolge",
}
at["labelname"] = {
    "en": "change scheduler - no same-day spacing for siblings/show due siblings in order",
    "de": "Verwandte neue Karten direkt nacheinander abfragen",
}


at["startup_reminder_ignore_decksettings"] = {
    "en": ('Info: add-on "show new siblings in order" is enabled and overrides the deck settings '
           'for sibling burying.'),
    "de": ('Hinweis: Erweiterung "show new siblings in order" ist aktiviert und überlagert '
           'die Stapeleinstellung \"Verwandte neue Karten nicht am selben Tag lernen\"'),
}

at["startup_reminder"] = {
    "en": 'Info: the add-on "show new siblings in order " is enabled',
    "de": 'Zur Erinnerung: Die Erweiterung "show new siblings in order" ist aktiviert',
}


localized = {}
for k, v in at.items():
    if LANG in v:
        localized[k] = v[LANG]
    elif "en" in v:
        localized[k] = v["en"]
    else:
        print('missing text, value: {}'.format(k))
t = SimpleNamespace(**localized)
