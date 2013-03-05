import urwid

class TaskWidget (urwid.WidgetWrap):

    def __init__ (self, task):
        self.task = task

        desc = urwid.Text(task.description())
        proj = urwid.Text(task.project() + ' ', align='right')

        due  = urwid.Text(task.due_date_string() + ' ', align='right')
        tags = urwid.Text(task.tags_string() + ' ', align='right')

        item = urwid.AttrMap(urwid.Columns([
            ('fixed', 11, urwid.AttrWrap(proj, 'proj', 'proj_focus')),
            desc,
            tags,
            ('fixed', 11, due)
        ]), 'body', 'body_focus')

        urwid.WidgetWrap.__init__(self, item)

    def selectable (self):
        return True

    def keypress(self, size, key):
        return key

