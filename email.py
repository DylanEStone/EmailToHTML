# Important
import os
import re
from datetime import date

class Link:
    link = ""
    paragraph = 0
    def __init__(self, link, paragraph):
        self.link = link
        self.paragraph = paragraph

class Email:
    title = ""
    links = []
    bodies = []
    def __init__(self, links, bodies):
        self.links = links
        self.bodies=bodies
    def set_title(self, title):
        self.title=title
    def set_link(self, link):
        self.link=link
    def set_bodies(self, bodies):
        self.bodies = bodies

# Cuts out metadata
def parse_emails():
    filename = ("/home/stone/.thunderbird/wd5ca36k.default/Mail/Local Folders/Stallman")
    text = open(filename,'r')
    document = text.readlines()
    flag=0
    count=0
    emails = []
    for line in document:
        if re.match("From -", line):
            flag = 0
        if flag == 1:
            emails.append(line.strip())
        if re.match("X-VR-SPAMCAUSE", line):
            flag = 1
        count+=1
    return emails


# Removes some unwanted spacing, and prints contents
def print_contents(emails):
    for line in emails:
        if re.match("http", line):
            print("<a href=\"", line.strip())
        elif (line != ""):
            print(line.strip())
        else :
            print()

## Less Spaghetti O's
def group_emails(emails):
    new_str = ""
    group_emails = []
    links = []
    bodies = []
    link_index = 0
    kount = 0
    for line in emails:
        #print("line: ", line)
        if line != "":
            if new_str != "":
                new_str += " "
            new_str += line
        elif line == "":
            kount += 1
            if kount == 3:
                kount = 0
                continue
            if new_str == "":
                group_emails.append(Email(links, bodies))
                grp_str = []
                links = []
                bodies = []
                continue
            if is_link(new_str):
                links.append(Link(new_str, link_index-1))
            else:
                bodies.append(new_str)
                link_index += 1
            new_str = ""
    return group_emails

def is_link(string):
    if re.match("http", string):
        return True
    else:
        return False


# links link
def print_email(index, emails):
    print("\n")
    print("title: ", emails[index].title)
#    print("links: ", emails[index].links[0].link)
#    print("links index: ", emails[index].links[0].paragraph)
    print("body: ", emails[index].bodies)

def main():
    email_list = []
    email_list = parse_emails()
    email_list = group_emails(email_list)
    for x in range(len(email_list)):
        print_email(x, email_list)


if __name__ == '__main__':
    main()
