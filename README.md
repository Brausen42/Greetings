# Greetings
Project for generating a customized message based on a template message and inputs to that message.

## Instructions to run
run './main.py' or 'python3 main.py' from your terminal of choice that supports python3

## Overview of Design
I chose to design this project with the idea of 'Tokenizable' objects as a generic way to template out an object into something that could be plugged into a specially formatted message. These tokens can be made from any object, and at their simplest convert a value to a string, but can be powerful enough to have layers of logic built in.

These layers of logic are possible because the MessageTemplate continues to 'open up' each token which may contain even more tokens (or more logic!) until no tokens are left. I thought this would allow for lots of freedom and creativity in the future for creating unique messages.

The reason for splitting the Classes the way I did, was to group the data into independent pieces. For example, the reason a Reservation is pulled out of a Guest into its own Class is because the same Reservation could be a part of the list of active reservations a company currently has. Thus, the same id would map these Reservations together.

## Language
I picked Python as the language to use since it's one that I have a lot of experience with. However, it was a tough choice between Python and Typescript as I've been using Typescript more often in recent times. Both languages offer Object Oriented Programming concepts along with some fun and useful functional programming utility that I enjoy (notably function closures). Both are also quick and easy to write, with Typescript having the advantage of Type safety upon transpiling.

## Verifying correctness
My process for verifying correctness was two part. First, was thinking through the logic I was using and double checking that there weren't any holes in the logic which focused on the use cases of the project and ensuring that it was possible to do everything that might be useful. Second, was actually testing the project with real values. This meant normal values, and weird edge cases such as missing values, '$' characters, or almost tokens e.g. "{ALMOST}". Even more rigorous testing could be done with full coverage unit testing given more time.

## Things I would add with more time
* A slightly more detailed README
* A more user-friendly main program to use with the project
* More pre-built MessageTemplates
* Better error and edge-case checking
  * Notably, elegantly handle the potential for an infinite loop when two tokens 'open up' to reveal one another
* ID uniqueness enforcement
* Useful derived tokens for different 'Tokenizable' objects
  * e.g. GUEST.FULLNAME from GUEST.FIRSTNAME and GUEST.LASTNAME
* Unit tests to ensure code reliability
* RESTful web services that expose the project's functionality in a language agnostic way
* A web-based front end to make interacting with the data more enjoyable
* The ability to save back custom MessageTemplates to the 'database'
* A 'setup.py' to better track the package