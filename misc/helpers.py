# -*- coding: utf-8 -*-
import re
import cPickle
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

# 1) Whitelist of keywords for navigation, and function for keeping priority queue.
#
# Scores a page's outgoing links based on learned set of keywords associated with directories. 
# The function accepts a list of (URL, [keywords]), where keywords are the text within and 
# surrounding a hyperlink.
directory_keywords = ['professor', 'faculty', 'tenure', 'people', 'full-time', 'directory', 'personnel', 'professeur', 'professeure', 'staff']

def evaluate_links(keyword_dict):
    # Whitelist of keywords for navigating to faculty directories.
    default_score = 100

    # Create a new dictionary to hold URL scores
    evaluated_links = [] 
    for pair in keyword_dict:
        key, phrases = pair[0], pair[1]
        score = default_score

        for phrase in phrases:
            # Add points for positive keywords. Searches the text 
            # around and within the link
            for positive_keyword in directory_keywords:
                score += phrase.count(positive_keyword)

        for positive_keyword in directory_keywords:
            score += key.count(positive_keyword)

        # Add the URL with its score
        evaluated_links.append((key, phrases, score))

    # Sort queue by the URL's score. Returns a list with most
    # revelant URLS towards the end.
    x = sorted(evaluated_links, key=lambda triple: triple[2])
    return [triple[0] for triple in x]

print("\nDirectory keywords: {0}\n".format(directory_keywords))

# 2) Complete set of features of our random forest classifier for classifying pages as 
# directories.
#
features = pd.read_pickle('features.p')
print("Length of total feature set: {0}".format(len(features)))
clf = cPickle.load(open('classifier.p', 'rb'))
important = sorted(range(len(clf.feature_importances_)), key=lambda i:clf.feature_importances_[i])
print("Important features: {0}\n".format(features[important[len(important)-10:]]))


# 3) Whitelist of first and last names
#
# See `name_set.p` for list of first and last names randomized. To load:
# 
x = cPickle.load(open('name_set.p', 'rb'))
print("Total number of names: {0}\n".format(len(x))) # 7058


# 4) Whitelist of keywords in TT and non-TT titles. 
#
title_keywords = ['professor', 'faculty', 'tenure', 'people', 'full-time', 'assistant', 'associate ', 'director', 'chair', 'president', 'asst.', 'prof.', 'assoc.', 'personnel', 'professeure', 'professeur', 'research', 'visiting', 'practice', 'adjunct', 'secretary', 'admin', 'lecturer', 'emerit', 'affiliat', 'industry', 'part-time', 'instructor', 'specialist', 'advisor', 'manager', 'retire', 'courtesy', 'technical', 'post-doc', 'postdoc', 'staff', 'guest', 'collab', 'coordinat', 'develop', 'support', 'chancellor', 'scholar', 'engineer', 'joint', 'in residence', 'dir.', 'dean', 'programmer', 'analyst', 'technician', 'designer', 'co-chair', 'secondary appointment', 'teaching', 'provost', 'head', 'scientist', 'lead', 'directeur', 'phd student', 'graduate', 'fellow']
print("Total number of title keywords: {0}\n".format(len(title_keywords)))


# 5) Blacklist of keywords which cannot be contained in TT titles
# 
non_TT_titles = ['adjoint', 'techincal', 'business advisor', 'academic advisor', 'tutoring', 'manager', 'admin', 'specialist', 'support', 'staff', 'programmer', 'guest', 'developer', 'finan','scientist', 'researcher', 'intern ', 'lecturer', 'analyst', 'instruct', 'post', 'technici', 'technical', 'part-time', 'part time', ' of practice', ' of the practice', 'research professor', 'office assistant', 'research associate', 'marketing', 'research assistant', 'teaching', 'affiliate', 'acting faculty', 'specilaist', 'outreach', 'clinical', 'partnerships', 'recruitment', 'communications', 'media relations', 'collaborator', 'visiting', 'practice', 'adj ', 'senior fellow', 'research fellow', 'avionics', 'commercialization', 'comm ', 'project director', 'adjt', 'research engineer', 'it director', 'lab director', 'managing director', 'student success', 'status-only', 'librarian', 'visitng', 'secondary faculty', 'lecturer', 'emeritus', 'hourly', 'assistant to the ', 'adjunct faculty', 'pullman bremerton everett adjunct', 'adjunct and courtesy', 'joint / courtesy faculty', 'courtesy appointment', 'secondary appointment', 'assistant adjunct professor', 'secretary', 'retired', 'emerita', 'in residence', 'program assistant', 'industry', 'emeriti', 'doctoral fellow']
print("Total number of non-TT title keywords: {0}\n".format(len(non_TT_titles)))
