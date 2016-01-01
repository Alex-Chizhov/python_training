from selenium.webdriver.support.ui import Select
from model.info_contact import Infos
from selenium.webdriver.common.by import By

class ContactHelper:

	def __init__(self,app):
		self.app = app

	def open_hp(self):
		wd = self.app.wd
		if not (wd.current_url.endswith("/") and len (wd.find_elements_by_name("Last name")) > 0):
			wd.find_element_by_link_text("home").click()



	def create(self, contact):
		wd = self.app.wd
		self.link_add_new()
		self.fill_form(contact)
		# submit adding new contact
		wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
		self.open_hp()




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



	#def modify_first_contact(self,new_contact_data):
		#wd = self.app.wd
		#self.open_hp()
		# select first contact
		#wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
		# fill form
		#self.fill_form(new_contact_data)
		#self.click_update()
		#self.open_hp()

	def modify_first_contact(self, new_contact):
		wd = self.app.wd
		self.open_hp()
		self.select_first_contact()
		# click modify
		wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
		self.fill_form(new_contact)
		#submit update
		wd.find_element_by_name("update").click()
		self.open_hp()

	def select_first_contact(self):
		wd = self.app.wd
		wd.find_element_by_name("selected[]").click()


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

	def get_contact_list(self):
		wd = self.app.wd
		self.open_hp()
		contacts = []
		for element in wd.find_elements_by_name("entry"):
			td_values = element.find_elements(By.TAG_NAME, "td")
			last_name = td_values[1].text
			first_name = td_values[2].text
			id = element.find_element_by_name("selected[]").get_attribute("value")
			contacts.append(Infos(lastname=last_name, firstname=first_name, id = id))
		return contacts


