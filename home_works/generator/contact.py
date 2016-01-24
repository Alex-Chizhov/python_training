from model.info_contact import *
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    print(str(err))
    getopt.usage()
    sys.exit(2)

n = 4
f = "data/contacts.json"
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def randstring(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+string.punctuation+' '*5  # add 5 spaces
    return prefix+''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_data = [Infos(firstname="", lastname="", email="")] + [
    Infos(firstname=randstring('fname', 10), lastname=randstring('lname', 10), email=randstring('email', 10))
    for i in range(4)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(test_data))


