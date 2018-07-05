# -*- coding: utf-8 -*-
import re

def skip_faculty(title):
    title = title.lower()
    cannot_contain = ["adjoint", "techincal", "business advisor", "academic advisor", "tutoring", "manager", "admin", "specialist", "support", "staff", "programmer", "guest", "developer", "finan","scientist", "researcher", "intern ", "lecturer", "analyst", "instruct", "post", "technici", "technical", "part-time", "part time", " of practice", " of the practice", "research professor", "office assistant", "research associate", "marketing", "research assistant", "teaching", "affiliate", "acting faculty", "specilaist", "outreach", "clinical", "partnerships", "recruitment", "communications", "media relations", "collaborator", "visiting", "practice", "adj ", "senior fellow", "research fellow", "avionics", "commercialization", "comm ", "project director", "adjt", "research engineer", "it director", "lab director", "managing director", "student success", "status-only", "librarian", "visitng", "secondary faculty", "lecturer", "emeritus", "hourly", "assistant to the ", "cross-appointed", "joint appointment", "adjunct faculty", "pullman bremerton everett adjunct", "adjunct and courtesy", "joint / courtesy faculty", "courtesy appointment", "cross appointed", "secondary appointment", "assistant adjunct professor", "secretary", "retired", "emerita", "in residence", "program assistant", "industry", "emeriti", "doctoral fellow"]
    wrong_department = False
    if title.count("professor") > 0 and (title.count(" of ") > 0 or title.count(" for ") > 0 or title.count(" in ") > 0):
        if title.count("comput") > 0 or title.count("electric") > 0 or title.count("embedded") > 0 or title.count("engineer") > 0:
            wrong_department = True
    elif title.count("chair") > 0 and (title.count(" of ") > 0 or title.count(" for ") > 0 or title.count(" in ") > 0):
        if title.count("computer") > 0 or title.count("electric") > 0 or title.count("engineering") > 0:
            wrong_department = True
    elif title.count("director") > 0 and (title.count(" of ") > 0 or title.count(" for ") > 0 or title.count(" in ") > 0):
        if title.count("professor") > 0 and title.count("computer") > 0 or title.count("electric") > 0 or title.count("embedded") > 0 or title.count("engineer") > 0:
            wrong_department = True
    else:
        wrong_department = True

    if title.count("coordinator") > 0 and title.count("professor") == 0:
        return False
    if (not title.startswith("adjunct ")) and not title.startswith("research") and (not title.endswith("courtesy")) and (not title.endswith(" designer")) and (not title.startswith("engineer ")) and (not title.endswith("asst")) and (not title.startswith("visiting ")) and (not title.startswith("joint ")) and (not title.startswith("exec")) and (not title.startswith("adjunct")) and (not title.startswith("courtesy ")) and (not title.endswith("engineer")) and (not title.endswith("tech")) and all([title.count(word) == 0 for word in cannot_contain]) and not title.endswith("assistant") and not title == "project collaborator" and not title == "advisor" and not title == "research facilitator" and not title == "graduate advisor" and not title == "undergraduate advisor" and not title == "deputy director" and not title.endswith("affiliate") and not title.endswith(" secretary") and not title == ("secretary") and not title.endswith(" student") and not title.endswith(" intern") and not (title.count("scholar") > 0 and not title.count("professor") > 0):
        if wrong_department:
            return True

    return False
