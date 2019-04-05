#!/usr/bin/env python3

import json
from Guest import Guest
from Company import Company
from MessageTemplate import MessageTemplate

invalidIndexMsg = "Whoops, that doesn't seem to be an option. Try again!"
notAnIntegerMsg = "Please enter an integer ;)"

# load guests
guests = []
for guest in json.load(open("./resources/Guests.json")):
    guests.append(Guest(guest))

#load companies
companies = []
for company in json.load(open("./resources/Companies.json")):
    companies.append(Company(company))

#load templates
templates = []
for template in json.load(open("./resources/MessageTemplates.json")):
    templates.append(MessageTemplate(template))

def printGuests():
    print("\nGuests:")
    for guest in guests:
        print(str(guest.id) + ") " + guest.lastName + ", " + guest.firstName)

def printCompanies():
    print("\nCompanies:")
    for company in companies:
        print(str(company.id) + ") " + company.company + " - " + company.timezone)

def printTemplates():
    print("\nTemplates:")
    for template in templates:
        print(str(template.id) + ") " + template.message)

print("Welcome to the Message Templater!")
printTemplates()
pickedTemplate = input("\nEnter a number to use an existing template, or type a new template message yourself:\n")
try:
    num = int(pickedTemplate)
    for template in templates:
        if str(num) == template.id:
            active = template
    if active == None:
            print(invalidIndexMsg)
except:
    active = MessageTemplate({"message":pickedTemplate})

comp = None
while comp == None:
    printCompanies()
    companyId = input("Pick a company: ")
    try:
        num = int(companyId)
        for company in companies:
            if str(num) == company.id:
                comp = company
                continue
        if comp == None:
            print(invalidIndexMsg)
    except:
        print(notAnIntegerMsg)

person = None
while person == None:
    printGuests()
    personId = input("Pick a guest: ")
    try:
        num = int(personId)
        for guest in guests:
            if str(num) == guest.id:
                person = guest
                continue
        if person == None:
            print(invalidIndexMsg)
    except:
        print(notAnIntegerMsg)


active.loadValues(comp)
active.loadValues(person)

print("\nHere's your message :D\n")
print(active.createMessage())
