import codecs
import re

def to_basic_form(note):
    without_punctuation = re.split(r'\W*', note, flags=re.U)
    stripped = map(lambda x: x.rstrip(), without_punctuation)
    without_empty_strings = filter(lambda x: len(x) > 0, stripped)
    return without_empty_strings


def to_basic_forms(data):
    return list(map(to_basic_form, data))


def parse_note(path, filename):
    with open(path+filename, 'r') as f:
        notes = unicode(f.read(), "utf-8").split('\n')
        print notes

    notes = to_basic_forms(notes)
    with codecs.open(path+filename.split(".")[0]+"_basic.txt", 'wb', "utf-8") as target_file:
        for note in notes:
            print note
            target_file.write(' '.join(note)+"\n")



if __name__ == '__main__':
    # if len(sys.argv) == 2:
    # filename = sys.argv[1]
    # main(filename)
    # else:
    # print("Usage:")
    #     print("  python main.py [data_file]")
    path = "resources/"
    filename = "short_ocean_korpus.txt"
    parse_note(path, filename)
