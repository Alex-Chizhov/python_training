from selenium.webdriver.firefox.webdriver import WebDriver



class Application:
	def  __init__(self):
		self.wd = WebDriver()
		self.wd.implicitly_wait(60)
	
	def logout(self):
		wd = self.wd
		wd.find_element_by_link_text("Logout").click()

	def return_to_group_page(self):
		wd = self.wd
		wd.find_element_by_link_text("group page").click()

	def group_creator(self, group):
		wd = self.wd
		# open_gp
		wd.find_element_by_link_text("groups").click()
		# init_group_creator
		wd.find_element_by_name("new").click()
		# fill_group_form
		wd.find_element_by_name("group_name").click()
		wd.find_element_by_name("group_name").clear()
		wd.find_element_by_name("group_name").send_keys(group.name)
		wd.find_element_by_name("group_header").click()
		wd.find_element_by_name("group_header").clear()
		wd.find_element_by_name("group_header").send_keys(group.header)
		wd.find_element_by_name("group_footer").click()
		wd.find_element_by_name("group_footer").clear()
		wd.find_element_by_name("group_footer").send_keys(group.footer)
		# sumbit_creation_group
		wd.find_element_by_name("submit").click()
		self.return_to_group_page()

	def login(self, username, password):
		wd = self.wd
		self.open_hp()
		wd.find_element_by_name("user").click()
		wd.find_element_by_name("user").clear()
		wd.find_element_by_name("user").send_keys("%s" % username)
		wd.find_element_by_id("LoginForm").click()
		wd.find_element_by_name("pass").click()
		wd.find_element_by_name("pass").clear()
		wd.find_element_by_name("pass").send_keys(password)
		wd.find_element_by_css_selector("input[type=\"submit\"]").click()

	def open_hp(self):
		wd = self.wd
		wd.get("http://localhost/addressbook/")

	def link_add_new(self):
		wd = self.wd
		wd.find_element_by_link_text("add new").click()

	def input_save_form(self):
		wd = self.wd
		wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

	def fill_form_contact(self, info_contact):
		wd = self.wd
		# inpuy firstname
		wd.find_element_by_name("firstname").click()
		wd.find_element_by_name("firstname").send_keys(info_contact.firstname)
		# input middelname
		wd.find_element_by_name("middlename").click()
		wd.find_element_by_name("middlename").send_keys(info_contact.middelname)
		# input lastname
		wd.find_element_by_name("lastname").click()
		wd.find_element_by_name("lastname").send_keys(info_contact.lastname)
		# input nickname
		wd.find_element_by_name("nickname").click()
		wd.find_element_by_name("nickname").send_keys(info_contact.nickname)
		# input title
		wd.find_element_by_name("title").click()
		wd.find_element_by_name("title").send_keys(info_contact.title)
		#input company
		wd.find_element_by_name("company").click()
		wd.find_element_by_name("company").send_keys(info_contact.company)
		# input addres
		wd.find_element_by_name("address").click()
		wd.find_element_by_name("address").send_keys(info_contact.addres)
		# input home
		wd.find_element_by_name("home").click()
		wd.find_element_by_name("home").send_keys(info_contact.home)
		# input mobile
		wd.find_element_by_name("mobile").click()
		wd.find_element_by_name("mobile").send_keys(info_contact.mobile)
		# input work
		wd.find_element_by_name("work").click()
		wd.find_element_by_name("work").send_keys(info_contact.work)
		# input fax
		wd.find_element_by_name("fax").click()
		wd.find_element_by_name("fax").send_keys(info_contact.fax)
		# input homepage
		wd.find_element_by_name("homepage").click()
		wd.find_element_by_name("homepage").send_keys(info_contact.homepage)
		# Birthday
		if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option%s"% info_contact.day_Birthday).is_selected():
			wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option%s" % info_contact.day_Birthday).click()
		if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option%s" % info_contact.month_Birthday).is_selected():
			wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option%s" % info_contact.month_Birthday).click()
		wd.find_element_by_name("byear").click()
		wd.find_element_by_name("byear").send_keys(info_contact.year_Birthday)
		# Anniversary
		if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option%s" % info_contact.day_Anniversary).is_selected():
			wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option%s" % info_contact.day_Anniversary).click()
		if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option%s" % info_contact.month_Anniversary).is_selected():
			wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option%s" % info_contact.month_Anniversary).click()
		wd.find_element_by_name("ayear").click()
		wd.find_element_by_name("ayear").send_keys(info_contact.year_Anniversary)

		# input address 2
		wd.find_element_by_name("address2").click()
		wd.find_element_by_name("address2").send_keys(info_contact.address2)
		# input phone 2
		wd.find_element_by_name("phone2").click()
		wd.find_element_by_name("phone2").send_keys(info_contact.phone2)
		# input notes
		wd.find_element_by_name("notes").click()
		wd.find_element_by_name("notes").send_keys(info_contact.notes)
		# input foto
		wd.find_element_by_name("photo").send_keys(info_contact.photo)
	
	def	destroy(self):
		self.wd.quit()

