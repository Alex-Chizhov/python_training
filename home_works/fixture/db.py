import mysql.connector
from model.group import Group
from model.info_contact import Infos


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True  # Turn off cashing db

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self, clean=False):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname "
                           "from addressbook "
                           "where deprecated= '0000-00-00 00'")
            for row in cursor:
                (id, firstname, lastname) = row
                if clean :
                    list.append(Infos(id=str(id), firstname=firstname.strip(), lastname=lastname.strip()))
                else:
                    list.append(Infos(id=str(id), firstname=firstname, lastname=lastname))

        finally:
            cursor.close()
        return list



    def get_contact_list_from_home_page(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                contact_list.append(Infos(id=str(id), firstname=firstname.strip(), lastname=lastname.strip(), address=address.strip(),
                                            all_phones_on_hp="%s\n%s\n%s\n%s" % (home.strip(), mobile.strip(), work.strip(), phone2.strip()),
                                            all_email_on_hp="%s\n%s\n%s" % (email.strip(), email2.strip(), email3.strip())))
        finally:
            cursor.close()
        return contact_list

    def get_group_ids_of_contact(self, Contact):
        group_id_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, group_id) = row
                if Contact.id == str(id):
                    group_id_list.append(str(group_id))
        finally:
            cursor.close()
        return group_id_list

    def get_not_empty_groups_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (group_id) = row
                group_list.append(str(group_id))
        finally:
            cursor.close()
        return list(set(group_list))









    def destroy(self):
        self.connection.close()