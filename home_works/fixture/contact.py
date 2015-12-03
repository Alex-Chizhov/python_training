class ContactHelper:

	def __init__(self,app):
		self.app = app

	def link_add_new(self):
		wd = self.app.wd
		wd.find_element_by_link_text("add new").click()

	def input_save_form(self):
		wd = self.app.wd
		wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


	def type(self, field_name ,text):
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
		self.type("firstname",info_contact.firstname)
		self.type("middlename",info_contact.middelname)
		self.type("lastname",info_contact.lastname)
		self.type("nickname",info_contact.nickname)
		self.type("title",info_contact.title)
		self.type("company",info_contact.company)
		self.type("address",info_contact.address)
		self.type("home",info_contact.home)
		self.type("mobile",info_contact.mobile)
		self.type("work",info_contact.work)
		self.type("fax",info_contact.fax)
		self.type("homepage",info_contact.homepage)
		self.type("address2",info_contact.address2)
		self.type("phone2",info_contact.phone2)
		self.type("notes",info_contact.notes)
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
		#home
		wd.find_element_by_link_text("home").click()



	def modify_first_contact(self,new_contact_data):
		wd = self.app.wd
		wd.find_element_by_link_text("home").click()
		# select first contact
		wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
		# fill form
		self.fill_form(new_contact_data)
		# sumbit modification
		wd.find_element_by_name("update").click()
		wd.find_element_by_link_text("home").click()



