from selenium.webdriver.support.ui import Select
from model.info_contact import Infos
from selenium.webdriver.common.by import By
import re
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
		self.contact_cache = None



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
		self.change_field_value("email", info_contact.email)
		self.change_field_value("email2", info_contact.email2)
		self.change_field_value("email3", info_contact.email3)
		self.selest("//div[@id='content']/form/select[1]//option%s",info_contact.day_Birthday)
		self.selest("//div[@id='content']/form/select[2]//option%s",info_contact.month_Birthday)
		self.selest("//div[@id='content']/form/select[3]//option%s",info_contact.day_Anniversary)
		self.selest("//div[@id='content']/form/select[4]//option%s",info_contact.month_Anniversary)



	def delete_first_contact(self):
		self.delete_contact_by_index(0)


	def delete_contact_by_index(self, index):
		wd = self.app.wd
		self.open_hp()
		self.select_contact_by_index(index)
		#submit deleting
		wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
		wd.switch_to_alert().accept()
		self.open_hp()
		self.contact_cash = None



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
		self.modify_contact_by_index(new_contact, 0)




	def modify_contact_by_index(self, new_contact, index):
		wd = self.app.wd
		self.open_hp()
		self.select_contact_by_index(index)
		# click modify
		wd.find_elements_by_css_selector("img[alt=\"Edit\"]")[index].click()
		self.fill_form(new_contact)
		#submit update
		wd.find_element_by_name("update").click()
		self.open_hp()
		self.contact_cash = None

	def select_first_contact(self):
		wd = self.app.wd
		wd.find_element_by_name("selected[]").click()

	def select_contact_by_index(self,index):
		wd = self.app.wd
		wd.find_elements_by_name("selected[]")[index].click()


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
			for element in wd.find_elements_by_name("entry"):
				td_values = element.find_elements(By.TAG_NAME, "td")
				lastname = td_values[1].text
				firstname = td_values[2].text
				id = element.find_element_by_name("selected[]").get_attribute("value")
				all_phones = td_values[5].text
				all_email = td_values[4].text
				address = td_values[3].text
				self.contact_cache.append(Infos(lastname=lastname, firstname=firstname, id = id,
												all_phones_on_hp = all_phones,all_email_on_hp = all_email, address = address))
		return self.contact_cache

	def open_contact_to_edit_by_index(self,index):
		wd = self.app.wd
		self.open_hp()
		row = wd.find_elements_by_name('entry')[index]
		cell = row.find_elements_by_tag_name('td')[7]
		cell.find_element_by_tag_name('a').click()

	def open_contact_view_by_index(self,index):
		wd = self.app.wd
		self.open_hp()
		row = wd.find_elements_by_name('entry')[index]
		cell = row.find_elements_by_tag_name('td')[6]
		cell.find_element_by_tag_name('a').click()



	def get_contact_info_from_edit_page(self, index):
		wd = self.app.wd
		self.open_contact_to_edit_by_index(index)
		email = wd.find_element_by_name('email').get_attribute('value')
		email2 = wd.find_element_by_name('email2').get_attribute('value')
		email3 = wd.find_element_by_name('email3').get_attribute('value')
		firstname = wd.find_element_by_name('firstname').get_attribute('value')
		lastname = wd.find_element_by_name('lastname').get_attribute('value')
		address = wd.find_element_by_name('address').get_attribute('value')
		id = wd.find_element_by_name('id').get_attribute('value')
		home = wd.find_element_by_name('home').get_attribute('value')
		mobile = wd.find_element_by_name('mobile').get_attribute('value')
		work = wd.find_element_by_name('work').get_attribute('value')
		phone2 = wd.find_element_by_name('phone2').get_attribute('value')
		return Infos(email=email,email2=email2,email3=email3,
					 firstname=firstname,lastname=lastname,id=id,home=home,mobile=mobile,work=work,phone2=phone2,address = address)






	def get_contact_from_view_page(self,index):
		wd = self.app.wd
		self.open_contact_view_by_index(index)
		text= wd.find_element_by_id('content').text
		home = re.search('H: (.*)',text).group(1)
		work =re.search('W: (.*)',text).group(1)
		mobile = re.search('M: (.*)',text).group(1)
		phone2 = re.search('P: (.*)',text).group(1)
		return Infos(home=home,mobile=mobile,work=work,phone2=phone2)




	def edit_contact_by_id(self, id):
		wd = self.app.wd
		self.app.open_hp()
		self.select_contact_by_id(id)
		wd.find_element_by_css_selector('img[alt="Edit"]').click()
		self.input('lastname', 'new lastname')
		wd.find_element_by_name("update").click()
		self.contacts_cache = None


	def input(self, field_name, text):
		wd = self.app.wd
		if text is not None:
			wd.find_element_by_name(field_name).click()
			wd.find_element_by_name(field_name).clear()
			wd.find_element_by_name(field_name).send_keys(text)


	def edit_contact_form(self, Contact):
		wd = self.app.wd
		self.fill_form(Contact)
		self.contact_cache = None


	def select_contact_by_id(self, id):
		wd = self.app.wd
		wd.find_element_by_css_selector("input[value='%s']" % id).click()
	def delete_contact_by_id(self, id):
		wd = self.app.wd
		self.select_contact_by_id(id)
		wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
		wd.switch_to_alert().accept()
		self.open_hp()
		self.contact_cache = None

	def open_contact_to_edit_by_id(self, id):
		wd = self.app.wd
		self.app.open_hp()
		wd.find_element_by_xpath("//input[@value='%s']/../../td[8]/a" % id).click()

	def open_contact_to_view_by_id(self, id):
		wd = self.app.wd
		self.open_hp()
		wd.find_element_by_xpath("//input[@value='%s']/../../td[7]/a" % id).click()

