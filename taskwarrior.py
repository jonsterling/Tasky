import subprocess
import json
import datetime

class Utility:

    @staticmethod
    def run_command(args):
        subprocess.Popen(args, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, shell=True).communicate()

class Task:

    def __init__(self, data):
        self.data = data

    def description(self):
        return self.data.get('description', '')

    def project(self):
        return self.data.get('project', '')

    def tags(self):
        return [ t.encode('utf-8') for t in self.data.get('tags', []) ]

    def tags_string(self):
        tags = [ "+" + t for t in self.tags() ]
        return ", ".join(tags)

    def uuid(self):
        return self.data['uuid']

    def id(self):
        return self.data['id']

    def due_date(self):
        return self.parse_date_at_key('due')

    def start_date(self):
        return self.parse_date_at_key('start')

    def is_started(self):
        return self.start_date() is not None

    def due_date_string(self):
        return Task.show_date(self.due_date())

    def parse_date_at_key(self, key):
        if key in self.data:
            return datetime.datetime.strptime(self.data[key][:8],
                    "%Y%m%d").date()
        return None

    @staticmethod
    def show_date(date):
        if date:
            if date == datetime.datetime.today().date():
                return 'today'
            return date.strftime("%m/%d")
        return ''

class TaskWarrior:

    def pending_tasks(self, args=''):
        raw_output = subprocess.check_output(['task', 'export',
            'status:pending', args])

        task_json = '[%s]' % raw_output
        return [Task(task) for task in json.loads(task_json, strict=False)]

    def complete(self, task):
        Utility.run_command('task %s done' % task.uuid())

    def delete(self, task):
        Utility.run_command('task %s rc.confirmation:no del' % task.uuid())

    def add(self, value):
        Utility.run_command('task add ' + value)

    def mod(self, task, value):
        Utility.run_command('task %s mod %s' % (task.uuid(), value))

    def start(self, task):
        Utility.run_command('task %s start' % task.uuid())

    def stop(self, task):
        Utility.run_command('task %s stop' % task.uuid())

    def toggle_active(self, task):
        if task.is_started():
            self.stop(task)
        else:
            self.start(task)

    def undo(self):
        Utility.run_command('task rc.confirmation:no undo')


