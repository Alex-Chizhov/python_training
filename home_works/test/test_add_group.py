# -*- coding: utf-8 -*-
from model.group import Group
import pytest



#testdata =[
#        Group(name=name, header=header, footer=footer)
#            for name in ['',random_string('name',10)]
#            for header in ['',random_string('header',10)]
#            for footer in ['',random_string('footer',10)]
#  ]



def test_new_group_add(app,json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.creator(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)







if __name__ == '__main__':
	pytest.main('test_add_group.py')