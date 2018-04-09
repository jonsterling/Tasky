import urwid

class ScrollingListBox(urwid.ListBox):

    def scroll_down(self):
        focus = self.get_focus()[1]
        if focus is not None:
            try:
                self.set_focus(focus + 1)
            except:
                return

    def scroll_up(self):
        focus = self.get_focus()[1]
        if focus > 0:
            self.set_focus(focus - 1)

    def mouse_event(self, size, event, button, col, row, focus):
        button_map = {
            4: self.scroll_down,
            5: self.scroll_up
        }

        if button in button_map:
            button_map[button]()

        return urwid.ListBox.mouse_event(self, size, event, button, col, row, focus)

    def keypress(self, size, key):
        key_map = {
            'j': self.scroll_down,
            'k': self.scroll_up
        }

        if key in key_map:
            key_map[key]()

        return urwid.ListBox.keypress(self, size, key)

