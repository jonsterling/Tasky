import subprocess
import json

class Utility:

    @staticmethod
    def run_command(args):
        subprocess.Popen(args, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, shell=True).communicate()

class TaskWarrior:

    def pending_tasks(self, args=''):
        raw_output = subprocess.check_output(['task', 'export',
            'status:pending', args])

        task_json = '[%s]' % raw_output
        return json.loads(task_json, strict=False)

    def complete(self, task):
        Utility.run_command('task %s done' % task['uuid'])

    def delete(self, task):
        Utility.run_command('task %s rc.confirmation:no del' % task['uuid'])

    def add(self, value):
        Utility.run_command('task add ' + value)

    def mod(self, task, value):
        Utility.run_command('task %s mod %s' % (task['uuid'], value))

    def undo(self):
        Utility.run_command('task rc.confirmation:no undo')


