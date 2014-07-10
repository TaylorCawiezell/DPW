'''
Taylor
07/10/14
simple-login
'''

import webapp2 #use webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self):
        about_button = Button()
        about_button.click()
        about_button.show_label()
        contact_button = Button()
        contact_button.label = 'Contact Us'
        contact_button.show_label()
class Button(object):
    def __init__(self):
        print "constructor method of button ran"
        self.label = "" #public attribute
        self.__size = 60 #private attribute - two underscores
        self._color = "#3abeef" #protected attribute -one underscore
        #self.click()
        #self.on_roll_over('Hello!!')
    
    def click(self):
        print "You've clicked me :("
        
    def on_roll_over(self, message):
        print "You've rolled over me ;D" + message
    
    def show_label(self):
        print "My Label is " + self.label

#no touchy
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
