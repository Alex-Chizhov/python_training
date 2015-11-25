# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.group import Group
from model.info_contact import Infos


@pytest.fixture
def app(request):
	fixture = Application()
	request.addfinalizer(fixture.destroy)
	return fixture












def test_add_group(app):
	app.session.login( username="admin", password="secret")
	app.group.creator(Group(name="123", header="123", footer="123"))
	app.session.logout()




def test_add_contact(app):
	
	app.session.login( username="admin", password="secret")
	app.contact.link_add_new()
	app.contact.fill_form(Infos(firstname="qq", middelname="qq", lastname="qq", nickname="qq", title="qq", company="qq",
								addres="ww", home="11", mobile="22", fax="22", homepage="wewr.ru", day_Birthday="[7]",
								month_Birthday="[10]", year_Birthday="1980", day_Anniversary="[18]", month_Anniversary="[7]",
								year_Anniversary="2000", address2="12", phone2="12", notes="12", work ='qwe', photo ="C:\\Users\\Alex\\Documents\\GitHub\\python_training\\home_work_3\\avatar.jpg"))
	app.contact.input_save_form()
	app.session.logout()











def test_add_empty_group(app):
	

	app.session.login( username="admin", password="secret")
	app.group.creator(Group(name="", header="", footer=""))

	app.session.logout()



if __name__ == '__main__':
	pytest.main('test_add_group_and_contact.py')