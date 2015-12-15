from selenium.webdriver.support.ui import Select
from model.info_contact import Infos
class ContactHelper:

	def __init__(self,app):
		self.app = app

	def open_hp(self):
		wd = self.app.wd
		if not (wd.current_url.endswith("/") and len (wd.find_elements_by_name("Last name")) > 0):
			wd.find_element_by_link_text("home").click()



	def link_add_new(self):
		wd = self.app.wd
		wd.find_element_by_link_text("add new").click()

	def input_save_form(self):
		wd = self.app.wd
		wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


	def change_field_value(self, field_name, text):
		wd = self.app.wd
		if text is not None:
			wd.find_element_by_name(field_name).click()
			wd.find_element_by_name(field_name).clear()
			wd.find_element_by_name(field_name).send_keys(text)

	def input_foto(self, field_name ,text):
		wd = self.app.wd
		if text is not None:
			wd.find_element_by_name(field_name).send_keys(text)


	def selest(self, field_name ,text):
		wd = self.app.wd
		if text is not None:
			if not wd.find_element_by_xpath(field_name % text).is_selected():
				wd.find_element_by_xpath(field_name % text).click()







	def fill_form(self, info_contact):
		wd = self.app.wd
		self.change_field_value("firstname", info_contact.firstname)
		self.change_field_value("middlename", info_contact.middelname)
		self.change_field_value("lastname", info_contact.lastname)
		self.change_field_value("nickname", info_contact.nickname)
		self.change_field_value("title", info_contact.title)
		self.change_field_value("company", info_contact.company)
		self.change_field_value("address", info_contact.address)
		self.change_field_value("home", info_contact.home)
		self.change_field_value("mobile", info_contact.mobile)
		self.change_field_value("work", info_contact.work)
		self.change_field_value("fax", info_contact.fax)
		self.change_field_value("homepage", info_contact.homepage)
		self.change_field_value("address2", info_contact.address2)
		self.change_field_value("phone2", info_contact.phone2)
		self.change_field_value("notes", info_contact.notes)
		self.input_foto("photo",info_contact.photo)
		self.input_foto("byear",info_contact.year_Birthday)
		self.input_foto("ayear",info_contact.year_Anniversary)
		self.selest("//div[@id='content']/form/select[1]//option%s",info_contact.day_Birthday)
		self.selest("//div[@id='content']/form/select[2]//option%s",info_contact.month_Birthday)
		self.selest("//div[@id='content']/form/select[3]//option%s",info_contact.day_Anniversary)
		self.selest("//div[@id='content']/form/select[4]//option%s",info_contact.month_Anniversary)





	def delete_first_contact(self):
		wd = self.app.wd
		#select first contact
		wd.find_element_by_name("selected[]").click()
		# Delite
		wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
		# agree in new window
		wd.switch_to_alert().accept()
		self.open_hp()



	def modify_first_contact(self,new_contact_data):
		wd = self.app.wd
		self.open_hp()
		# select first contact
		wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
		# fill form
		self.fill_form(new_contact_data)
		self.click_update()
		self.open_hp()

	def click_update(self):
		wd = self.app.wd
		wd.find_element_by_name("update").click()

	def count(self):
		wd = self.app.wd
		self.open_hp()
		return len(wd.find_elements_by_name("selected[]"))


	def count_modify(self,field_name):
		wd = self.app.wd
		self.open_hp()
		wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
		return len(wd.find_element_by_name(field_name).get_attribute("value"))

	def count_modify_amonth(self):
		wd = self.app.wd
		self.open_hp()
		wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
		return  len (wd.find_element_by_name('amonth').get_attribute("value"))


	contact_cache = None

	def get_contact_list(self):
		if self.contact_cache is None:
			wd = self.app.wd
			self.open_hp()
			self.contact_cache = []
			for row in wd.find_elements_by_name('entry'):
				cells = row.find_elements_by_tag_name('td')
				firstname = cells[1].text
				lastname  = cells[2].text
				id = cells[0].find_element_by_tag_name('input').get_attribute('value')
				self.contact_cache.append(Infos(firstname=firstname,lastname = lastname, id = id))
		return list(self.contact_cache)
