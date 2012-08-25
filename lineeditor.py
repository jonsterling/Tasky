import urwid

class LineEditor(urwid.Edit):

    __metaclass__ = urwid.signals.MetaSignals
    signals = ['done']

    def keypress(self, size, key):
        if key == 'enter':
            urwid.emit_signal(self, 'done', self.get_edit_text())
            return

        if key == 'esc':
            urwid.emit_signal(self, 'done', None)
            return

        return urwid.Edit.keypress(self, size, key)
