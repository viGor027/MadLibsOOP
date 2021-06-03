import re


class Main:
    dirs = {'Luck':'stories/itsmyluck.txt', 'Love':'stories/loveatfirstsight.txt', 'Zoo':'stories/triptothezoo.txt'}
    def __init__(self):
        picked = self.pick_story()
        fields_to_replace = self.get_fields(self.dirs[picked])
        ready_to_replace = self.ask_to_fill(fields_to_replace)
        final_result = self.replace_fields(self.dirs[picked], fields_to_replace, ready_to_replace)
        print(final_result)

    def pick_story(self):
        print("Type in the title: ")
        for k,v in Main.dirs.items():
            print(k)
        choice = str(input('Your choice: '))
        return choice

    def get_fields(self, directory):
        results = []
        pattern = re.compile(r'<\s*(.*?)\s*>')
        with open(directory, 'r', encoding='utf-8') as f:
            text = f.read()
            matches = pattern.finditer(text)
        #print(matches)
        for i in matches:
           # print(i[0])
            results.append(i[0])
        return results

    def ask_to_fill(self, blank_fields):
        filled_fields = []
        for i in blank_fields:
            filled_fields.append(input("Type in a(n) " + i[1:-1] +": "))
        print(filled_fields)
        return filled_fields

    def replace_fields(self,story, blank_fields, filled_fields):
        with open(story, 'r', encoding='utf-8') as f:
            text = f.read()
            for i in range(len(blank_fields)):
                text = text.replace(blank_fields[i], filled_fields[i])
        return text

if __name__ == "__main__":
    run = Main()