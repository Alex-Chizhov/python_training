from model.group import Group
import random
import string
import os.path
import getopt
import sys
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    print(str(err))
    getopt.usage()
    sys.exit(2)

n = 4
f = 'data/groups.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


def randstring(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+string.punctuation+' '*5
    return prefix+''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_data = [Group(name="", header="", footer="")] + [
    Group(name=randstring('gname', 10), header=randstring('gheader', 10), footer=randstring('gfooter', 10))
    for i in range(n)
 ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(test_data))