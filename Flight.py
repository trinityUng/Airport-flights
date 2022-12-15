#imports information from Airport
from Airport import *

#Flight class created
class Flight:

    #constructor for the flight class
    def __init__(self,flightNo,origin,destination):
        #if statement created to check that origin and destination are airport objects
        if (isinstance(origin, Airport) or isinstance(destination, Airport)) == False:
            #if origin and destination is not an airport object a TypeError is raised
            raise TypeError("The origin and destination must be Airport objects")
        #if origin and destination are airport objects they will be initialize
        elif (isinstance(origin, Airport) or isinstance(destination, Airport)) == True:
            self._flightNo = flightNo
            self._origin = origin
            self._destination = destination

    #returns the object into a string format
    def __repr__(self):
        #if statement created to check if the flight is domestic or not by calling the other function in the class called isDomesticFlight()
        #if it's true it will return the flight number, origin city, destination city and domestic
        if self.isDomesticFlight() == True:
            return "Flight: " + self._flightNo + " from " + self._origin.getCity() + " to " + self._destination.getCity() + " {domestic}"
        #if it's false it will return the flight number, origin city, destination city and international
        elif self.isDomesticFlight() == False:
            return "Flight: " + self._flightNo + " from " + self._origin.getCity() + " to " + self._destination.getCity() + " {international}"

    #checks to see if self and other are the same and if not returns false
    def __eq__(self,other):
        #if statement created to check if other is a instance of the specified class type
        #if false it will return false
        if isinstance(other, Flight) == False:
                return False
        #if true it will check if self and other are the same and if not it will return false
        elif isinstance(other, Flight) == True:
            if (self._origin and self._destination) == (other.getOrigin() and other.getDestination()):
                return True
            else:
                return False

    #getter for flight number of the flight
    def getFlightNumber(self):
        return self._flightNo

    #getter for origin of the flight
    def getOrigin(self):
        return self._origin

    #getter for destination of the flight
    def getDestination(self):
        return self._destination

    #checks if the flight is domestic of not
    def isDomesticFlight(self):
        #if statement calls the getter of airport class to check if the origin and destination have the same country and if so returns true and else returns false, which is used in __repr__
        if self._origin.getCountry() == self._destination.getCountry():
            return True
        else:
            return False

    #setter for origin
    def setOrigin(self,origin):
        self._origin = origin

    #setter for destination
    def setDestination(self,destination):
        self._destination = destination
