# Taskwarrior Utilities

Just put these files in your path! To make a `tasky` command, do the
following:

~~~~sh
ln -s tasky.py tasky
chmod +x tasknote
chmod +x tasky
~~~~

## Tasky: a modal, interactive Taskwarrior client

Tasky is pretty well undocumented, but it is basically a curses-based
shell to make interacting with Taskwarrior easier. The main keys are the
following:

1. `j`, `k`: scrolling.

2. `i`: insert new task.

3. `e` or `RETURN`: edit the selected task (see below).

4. `c`: complete the selected task. No confirmation.

5. `d`: delete the selected task. No confirmation.

6. `u`: undo whatever you did last. No confirmation.

7. `:`: enter **command mode**. Basically, enter any arbitrary
   Taskwarrior commands (without `task`). Example: `proj:tasky del`.

8. `!`: enter **shell mode**. Run any arbitrary shell command.

9. `f`: change the current filter (see below).

10. `n`: runs `tasknote` for a given task in a new `tmux` pane. Since I
    built Tasky for myself, this command requires you to be in a `tmux`
    session. I plan to make this configurable later.

Tasky supports mouse input! You can click a task to select it, and
scrolling also works.


### Filters

Filters in Tasky are quite simple. In order to get your tasks, Tasky
runs `task export`; a *filter* is simply a string that is appended to
the `task export` command. So, a valid filter would be something like
`proj:tasky` or `due:today` or `due:tomorrow +important`. The current
filter is displayed in the header.

**If you run Tasky with arguments, those will be used as the initial
filter.**

### Editing and Inserting

The text you enter is appended to a `task add` or `task # mod` command.
That means you can change a task's project or tags or due date using
this mode.

When adding new tasks, the current filter is appended. That means that
if you are currently viewing tasks in a certain project that are due
today, new tasks will also have those attributes.


### Still to do

Tasky does not yet support sorting or arbitrary searching.


## Tasknote

Tasknote is another small utility that allows you to associate a text
file with a task. It is included in this repository.
