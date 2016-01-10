import re
from random import randrange



def test_email_on_hp(app):
    # define number all contact
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))

    info_from_hp         = app.contact.get_contact_list()[index]
    email_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert info_from_hp.all_email_on_hp   ==  merge_like_email_on_hp(email_from_edit_page)

def test_phones_on_hp(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))

    contact_from_hp        = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_hp.all_phones_on_hp   ==  merge_like_phones_on_hp(contact_from_edit_page)


def test_info_contact_on_hp(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))

    contact_from_hp =  app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_hp.lastname == contact_from_edit_page.lastname
    assert contact_from_hp.firstname == contact_from_edit_page.firstname
    assert contact_from_hp.address == contact_from_edit_page.address






def clear(s):
    return re.sub('[() -]','',s)

def merge_like_phones_on_hp(contact):
    return '\n'.join(filter(lambda x: x!= "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home,contact.mobile,contact.work,contact.phone2]))))

def merge_like_email_on_hp(contact):
    return '\n'.join(filter(lambda x: x!= "",
                                filter(lambda x: x is not None,
                                       [contact.email,contact.email2,contact.email3])))