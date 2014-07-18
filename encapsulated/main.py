import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #HTML for header
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Calculator!</title>
        <link rel="stylesheet" type="text/css" href="css/main.css" />
        <link href='http://fonts.googleapis.com/css?family=Josefin+Sans' rel='stylesheet' type='text/css' />
    </head>
    <body>'''
        #HTML for form inputs
        page_body = '''
            <div class='area'>
            <h1>Employee Earnings</h1>
            <button id="bobbut">Bob Jones</button>
            <button>Tom Frank</button>
            <button>James Fail</button>
            <button>Sarah Lewis</button>
            <button>Jake Wilders</button>
            </div>
            '''
        #HTML for closing tags
        page_close = '''
        </form>
    </body>
</html>'''
        self.response.write(page_head + page_body + page_close) #printing information

        #Bob's Earnings
        bob = Earnings()
        bob.hourly = 10.50
        bob.monthly = 1600
        bob.anual= 19200
        bob.time = 2 #time in years
        bob.calc_total()
        #self.response.write(str(bob.total_earnings))
        
        #Tom's Earnings
        tom = Earnings()
        tom.hourly = 50.50
        tom.monthly = 8000
        tom.anual= 96000
        tom.time = 10 #time in years
        tom.calc_total()
        #self.response.write(str(tom.total_earnings))
        
        #Jame's Earnings
        james = Earnings()
        james.hourly = 50.50
        james.monthly = 8000
        james.anual= 96000
        james.time = 10 #time in years
        james.calc_total()
        #self.response.write(str(james.total_earnings))
        
        #Sarah's Earnings
        sarah = Earnings()
        sarah.hourly = 50.50
        sarah.monthly = 8000
        sarah.anual= 96000
        sarah.time = 10 #time in years
        sarah.calc_total()
        #self.response.write(str(sarah.total_earnings))
        
        #Jake's Earnings
        jake = Earnings()
        jake.hourly = 50.50
        jake.monthly = 8000
        jake.anual= 96000
        jake.time = 10 #time in years
        jake.calc_total()
        #self.response.write(str(jake.total_earnings))

class Earnings(object):
    def __init__(self):
        self.__hourly = 0
        self.monthly = 0
        self.anual= 0
        self.time = 0
        self.__total_earnings = 0
        
    @property
    def total_earnings(self):
        #calculate total earnings
        return self.__total_earnings
    
    @total_earnings.setter
    def total_earnings(self, new_total_earnings):
        self.__total_earnings = new_total_earnings
    
    @property
    def hourly(self):
        #calculate total earnings
        return self.__hourly
    
    @hourly.setter
    def hourly(self, new_hourly):
        self.__hourly = new_hourly
            
    def calc_total(self):
      self.__total_earnings = self.anual * self.time
      
    





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
