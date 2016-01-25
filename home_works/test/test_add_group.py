# -*- coding: utf-8 -*-
from model.group import Group
import pytest



#testdata =[
#        Group(name=name, header=header, footer=footer)
#            for name in ['',random_string('name',10)]
#            for header in ['',random_string('header',10)]
#            for footer in ['',random_string('footer',10)]
#  ]


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.creator(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



if __name__ == '__main__':
	pytest.main('test_add_group.py')