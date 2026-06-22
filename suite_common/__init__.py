# suite_common — shared scaffold for the GNOME office suite (Letters, Tables, Decks).
# SPDX-License-Identifier: GPL-3.0-or-later

# Provide a fallback _() for development use.  The launcher script
# (tables.in / decks.in / letters.in) calls gettext.textdomain()
# at startup, which binds the real gettext._; this placeholder returns
# the string unchanged until then.
try:
    from gettext import gettext as _
except ImportError:
    def _(s):
        return s
