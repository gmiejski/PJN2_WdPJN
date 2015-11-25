import re
import sys
# from lib.clp import CLP
#
# clp = CLP()


def to_basic_form(note):
    without_punctuation = re.split(r'\W*', note, flags=re.U)
    print without_punctuation
    # return [key for key in without_punctuation if clp.rec(key) and clp.label(clp.rec(key)[0])[0] != 'G']


def to_basic_forms(data):
    return list(map(to_basic_form, data))


def parse_note(filename):
    with open(filename, 'r') as f:
        notes = unicode(f.read(), "utf-8").split('\n')
        print notes
        notes = to_basic_forms(notes)
        for note in notes:
            print note
            # print(notes.encode('utf-8'))
            # notes = re.findall(ur"<tr><td[^>]*?>\s?(.*?)</td><td[^>]*?><strong>\s?(.*?)</strong>\s?\[(.*?)\]</td><td[^>]*?>\s?(.*?)</td></tr>", notes, re.DOTALL)
            # snippet_list = map(parse_note_to_snippet_list, notes)
            # snippet_list = [x for x in snippet_list if x is not None]
            # return snippet_list


# def print_snippet_list(snippet_list):
# for snippet in snippet_list:
# whole_set = [i for side in snippet for i in side]
# print u' '.join(whole_set).encode('utf-8')

def main(filename):
    parse_note(filename)


if __name__ == '__main__':
    # if len(sys.argv) == 2:
    # filename = sys.argv[1]
    #     main(filename)
    # else:
    #     print("Usage:")
    #     print("  python main.py [data_file]")
    filename = "resources/short_ocean_korpus.txt"
    main(filename)
