# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.group import Group



from model.group import Group




def test_new_group_add(app):
    old_groups = app.group.get_group_list()
    group = Group(name="New group", header="New group header", footer="New group footer")
    app.group.creator(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_new_empty_group_add(app):
    #old_groups = app.group.get_group_list()
    #group = Group(name="", header="", footer="")
    #app.group.creator(group)
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) + 1 == len(new_groups)
    #old_groups.append(group)
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)






if __name__ == '__main__':
	pytest.main('test_add_group.py')