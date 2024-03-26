import sublime
import sublime_plugin
import re


class ExampleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")

class NotesFormatCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        self.view.run_command('select_all')
        content = self.view.substr(self.view.sel()[0]).strip()

        # 清理duokan日期标签
        pa = r'^[\d]*-[\d]*-[\d]* [\d]*:[\d]*:[\d]*[\r\n]*$'
        pa = re.compile(pa, re.M)
        content = re.sub(pa, '', content)

        # 清理kindle日期标签
        pa = r'^(标注|Highlight)\((.)*\)(.)*$'
        pa = re.compile(pa, re.M)
        content = re.sub(pa, '', content)

        pa = r'^(书签|Bookmark) - (.)*$'
        pa = re.compile(pa, re.M)
        content = re.sub(pa, '', content)


        content = content.replace('　', '')
        content = content.replace(' ', '')

        print(content)

        self.view.run_command('cut')
        self.view.insert(edit, 0, content)
        sublime.set_clipboard('')


class NotesAddQuoteCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        self.view.run_command('select_all')
        content = self.view.substr(self.view.sel()[0]).strip()
        content = content.replace('>> ', '')

        pa = r'[\n]'
        pa = re.compile(pa, re.M)
        content = re.sub(pa, '\n>', content)
        content = '>' + content

        pa = r'\n>\n>\n>'
        pa = re.compile(pa, re.M)
        content = re.sub(pa, '\n\n\n>', content)

        pa = r'>【】'
        pa = re.compile(pa, re.M)
        content = re.sub(pa, '\n', content)


        print(content)

        self.view.run_command('cut')
        self.view.insert(edit, 0, content)
        sublime.set_clipboard('')

class NotesReverseQuoteCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        self.view.run_command('select_all')
        content = self.view.substr(self.view.sel()[0]).strip()


        pa = r'((##(\s)*)[^#]*(###(\s)*)[^#]*)'
        pa = re.compile(pa, re.M)
        res = pa.findall(content)

        content = ''
        print(len(res))
        for i in range(len(res) - 1, -1, -1):
            content = content + res[i][0] + '\n\n'

        self.view.run_command('cut')
        self.view.insert(edit, 0, content)
        sublime.set_clipboard('')

class NotesDeleteBraketsCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        self.view.run_command('select_all')
        content = self.view.substr(self.view.sel()[0]).strip()

        pa = re.compile(r'(【)(.*?)(】[\s]*)', re.S)
        content = re.sub(pa, '', content)

        self.view.run_command('cut')
        self.view.insert(edit, 0, content)
        sublime.set_clipboard('')







