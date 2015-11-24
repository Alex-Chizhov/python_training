# -*- coding: utf-8 -*-


from group import Group
from info_contact import Infos
from application import Application
import pytest

@pytest.fixture
def app(request):
	fixture = Application()
	request.addfinalizer(fixture.destroy)
	return fixture
	




	






def test_add_group(app):
	app.login( username="admin", password="secret")
	app.group_creator( Group(name="123", header="123", footer="123"))
	app.logout()




def test_add_contact(app):
		
	app.login( username="admin", password="secret")
	app.link_add_new()
	app.fill_form_contact( Infos(firstname="qq", middelname="qq", lastname="qq", nickname="qq", title="qq", company="qq",
						  addres="ww", home="11", mobile="22", fax="22", homepage="wewr.ru", day_Birthday="[7]",
						  month_Birthday="[10]", year_Birthday="1980", day_Anniversary="[18]", month_Anniversary="[7]",
						  year_Anniversary="2000", address2="12", phone2="12", notes="12", work ='qwe',photo ="C:\\Users\\Alex\\Documents\\GitHub\\python_training\\home_work_3\\avatar.jpg"))
	app.input_save_form()
	app.logout()











def test_add_empty_group(app):
		

	app.login( username="admin", password="secret")
	app.group_creator( Group(name="", header="", footer=""))

	app.logout()






