#Airport class created
class Airport:

    #constructor created for airport class
    def __init__(self,code,city,country):
        self._code = code
        self._city = city
        self._country = country

    #returns the object in a string format
    def __repr__(self):
        return self._code + " (" + self._city + ", " + self._country + ")"

    #getter for the code of the airport
    def getCode(self):
        return self._code

    #getter for the city of the airport
    def getCity(self):
        return self._city

    #getter for the country of the airport
    def getCountry(self):
        return self._country

    #setter for the cityt
    def setCity(self,city):
        self._city = city

    #setter for the country
    def setCountry(self,country):
        self._country = country
