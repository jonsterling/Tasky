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

    def uuid(self):
        return self.data['uuid']

    def id(self):
        return self.data['id']

    def due_today(self):
        return self.due_date() == datetime.datetime.today().date()

    def due_date(self):
        if 'due' in self.data:
            return datetime.datetime.strptime(self.data['due'][:8],
                    "%Y%m%d").date()
        return None

    def due_date_string(self):
        if self.due_today():
            return 'today'

        date = self.due_date()
        if date:
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

    def undo(self):
        Utility.run_command('task rc.confirmation:no undo')


