# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.group import Group
from model.info_contact import Infos















def test_add_group(app):
	old_groups = app.group.get_group_list()
	group = Group(name="123", header="123", footer="123")
	app.group.creator(group)
	new_groups = app.group.get_group_list()
	assert len(old_groups)+1 == len(new_groups)
	old_groups.append(group)
	assert  sorted(old_groups,key=Group.id_or_max) == sorted(new_groups,key=Group.id_or_max)




def test_add_empty_group(app):
	old_groups = app.group.get_group_list()
	group = Group(name="", header="", footer="")
	app.group.creator(group)
	new_groups = app.group.get_group_list()
	assert len(old_groups)+1 == len(new_groups)
	old_groups.append(group)
	assert  sorted(old_groups,key=Group.id_or_max) == sorted(new_groups,key=Group.id_or_max)










def test_add_contact(app):
	old_contact = app.contact.get_contact_list()
	app.contact.link_add_new()
	contact = Infos(firstname="qq", middelname="qq", lastname="qq", nickname="qq", title="qq", company="qq",
								address="ww", home="11", mobile="22", fax="22", homepage="wewr.ru", day_Birthday="[7]",
								month_Birthday="[10]", year_Birthday="1980", day_Anniversary="[18]", month_Anniversary="[7]",
								year_Anniversary="2000", address2="12", phone2="12", notes="12", work ='qwe', photo ="C:\\Users\\Alex\\Documents\\GitHub\\python_training\\home_work_3\\avatar.jpg")
	app.contact.fill_form(contact)
	app.contact.input_save_form()
	new_contact = app.contact.get_contact_list()

	assert len(old_contact) +1== len(new_contact)
	old_contact.append(contact)
	assert  sorted(old_contact,key=Infos.id_or_max) == sorted(new_contact,key=Infos.id_or_max)









if __name__ == '__main__':
	pytest.main('test_add_group_and_contact.py')