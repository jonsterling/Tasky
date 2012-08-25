import urwid
import datetime

class TaskWidget (urwid.WidgetWrap):

    def __init__ (self, task):
        self.task = task

        desc = urwid.Text(task.get('description', ''))
        proj = urwid.Text(task.get('project','') + ' ', align='right')

        due = urwid.Text(self._due_date_string() + ' ', align='right')

        item = urwid.AttrMap(urwid.Columns([
            ('fixed', 11, urwid.AttrWrap(proj, 'proj', 'proj_focus')),
            desc,
            ('fixed', 11, due)
        ]), 'body', 'body_focus')

        urwid.WidgetWrap.__init__(self, item)

    def selectable (self):
        return True

    def keypress(self, size, key):
        return key

    def _due_today(self):
        return self._due_date() == datetime.datetime.today().date()

    def _due_date(self):
        if 'due' in self.task:
            return datetime.datetime.strptime(self.task['due'][:8],
                    "%Y%m%d").date()
        return None

    def _due_date_string(self):
        if self._due_today():
            return 'today'

        date = self._due_date()
        if date:
            return date.strftime("%m/%d")

        return ''


