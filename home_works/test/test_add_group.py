# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.group import Group
import pytest
import random
import string

def random_string(prefix,maxlen):
    syvmols = string.ascii_letters + string.digits +string.punctuation + ' '*10
    return prefix+''.join([random.choice(syvmols) for i in range(random.randrange(maxlen))])
from model.group import Group


testdata = [Group(name='',header='',footer='')]+[
    Group(name = random_string('name',10),header=random_string('header',15),footer=random_string('footer',20))
    for i in range(5)
]

#testdata =[
#        Group(name=name, header=header, footer=footer)
#            for name in ['',random_string('name',10)]
#            for header in ['',random_string('header',10)]
#            for footer in ['',random_string('footer',10)]
#  ]

@pytest.mark.parametrize('group',testdata,ids=[repr(x) for x in testdata])
def test_new_group_add(app,group):
    old_groups = app.group.get_group_list()
    app.group.creator(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)







if __name__ == '__main__':
	pytest.main('test_add_group.py')