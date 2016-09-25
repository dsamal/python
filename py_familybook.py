__author__ = 'DEBASISH'

import ConfigParser

def fb_Menu():
    x = raw_input("===== Hi Welcome to your Family Book =====\n" \
        "So How can I help you ? Below are the options for you to choose from\n\nSelect\n" \
        "1 : To Add a Family Member to the Book\n" \
        "2 : To Look for a Family Member Details in the Book\n" \
        "3 : To Correct any Family Member Name in the Book\n" \
        "4 : To Remove any Member from the Family Book\n" \
        "5 : To Exit\n")

    if x.isdigit():
        i = int(x)
        if 0 < i and i < 6:
            return i
        else:
            print "I wish i could understand your choice\n" \
              "At present I only understands the options from the menu which I show you\n" \
              "Please select an option from there...let me show you again!\n"
            return -1
    else:
        print "I wish i could understand your choice\n" \
              "At present I only understands the options from the menu which I show you\n" \
              "Please select an option from there...let me show you again!\n"
        return -1


def fb_AskMemberDetails():
    name = raw_input("What is the member's name ?")
    gender = raw_input("What's the gender of this member ?")
    father = raw_input("Who is the father of this new member ?")
    mother = raw_input("Who is the mother of this new member ?")
    spouse = raw_input("Who is the spouse of this new member ? if not married please enter 0")

    file_name = name+".dat"
    f1 = open(file_name, "ab+")
    str = "Father = " + father
    f1.write(str)
    f1.close()
    print "Thanks for sharing the information. The new member has been added to your Family Book"


def fb_AddMember():
    print "===== Well let's add the new member to you Family Book =====\n" \
          "I will ask few details of this new member, just share the same and I will quickly add him/her\n"
    fb_AskMemberDetails()
    return 0


def fb_SearchMember():
    name1 = raw_input("Enter whom you are looking for in your family book")
    #name2 = raw_input("Enter the 2nd person's name")
    config = ConfigParser.ConfigParser()
    config.read("family_book.ini")
    fb_section = config.sections()
    if name1 in fb_section:
        print "Following are the Relations found for", name1
        for i in config.items(name1):
            print i[1], '-', i[0]
        return 0
    else:
        print "Sorry", name1, "is not a member in your family book."
        return -1
def fb_EditMember():
    return 0


def fb_RemoveMember():
    return 0


def fb_Exit():
    return


def fb_CheckOption(i):
    """

    :rtype : int
    """
    if 1 == i:
        fb_AddMember()
    elif 2 == i:
        fb_SearchMember()
    elif 3 == i:
        fb_EditMember()
    elif 4 == i:
        fb_RemoveMember()
    elif 5 == i:
        fb_Exit()
    else:
        return -1

ip = -1
while -1 == ip:
    ip = fb_Menu()

fb_CheckOption(ip)


























