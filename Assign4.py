##
#author: Trinity Ung
#date: December 1st, 2022
#This program gathers information from two files, which will then use functions to complete tasks, objects, classes, dictionaries and sets

#imports information from Flight and Airport
from Flight import *
from Airport import *

allAirports = {}
allFlights = {}

#function loads data from the text files
def loadData(airportFile, flightFile):
    #try-except created to handle any exception that might occur will opening and reading the files
    try:
        loadFlightFile = flightFile
        loadAirportFile = airportFile
        #opens the files and reads the information
        openFlightFile = open(loadFlightFile, "r")
        openAirportFile = open(loadAirportFile, "r")

        #reads the lines in airport file
        for line in openAirportFile:
            #removes any spaces and splits where a comma occurs
            lineFixAirport = line.strip().split(",")
            code = lineFixAirport[0].strip()
            city = lineFixAirport[2].strip()
            country = lineFixAirport[1].strip()
            #once spaces are removed they are passed to the airport class
            airportObj = Airport(code,city,country)
            #oject is added to the dictionary
            allAirports[code] = airportObj

        #reads the line in flight file
        for line in openFlightFile:
            #removes any spaces and splits were a comma ocurrs
            lineFixFlight = line.strip().split(",")
            flightNumber = lineFixFlight[0].strip()
            origin = lineFixFlight[1].strip()
            destintation = lineFixFlight[2].strip()
            #goes through the allAirports dictionary
            for airport in allAirports:
                airport = allAirports[airport]
                #if statement checks if the airport object is the same as the origin or destination of the flights
                if airport.getCode() == origin:
                    originObj = airport
                if airport.getCode() == destintation:
                    destintationObj = airport

            #passed to the flight class
            flightObj = Flight(flightNumber,originObj,destintationObj)
            #if created to make sure duplicates are not added
            if originObj.getCode() not in allFlights:
                allFlights[originObj.getCode()] = [flightObj]
            else:
                allFlights[originObj.getCode()].append(flightObj)
        return True
    #if an exception ocurred false will be returned
    except:
        return False

#function created to find the airport by the airport code
def getAirportByCode(code):
    airportCode = code
    #if the code is in allAirports it will return the object airport of that flight code
    if airportCode in allAirports:
        return allAirports.get(airportCode)
    #if the code is not in allAirports it will return false
    else:
        return -1

#function returns a list with all Flight objects that have the chosen city as the origin or destination
def findAllCityFlights(city):
    flightCity = city
    cityList = []
    #nested for loops go through allFlights objects
    for i in range(len(allFlights)):
        for j in allFlights.values():
            for x in j:
                #if the city is in the object it will add it to the list
                if flightCity in str(x):
                    #if statement makes sure that there are no duplicates
                    if str(x.getFlightNumber()) not in str(cityList):
                        cityList.append(x)
    #returns the list of all the objects that are the origin or destination of the choosen city
    return cityList

#function returns a list with all Flight objects that have the chosen country as the origin or destination
def findAllCountryFlights(country):
    flightCountry = country
    countryList = []
    cityListInTheCountry = []
    #nested for loops go through allAirports
    for a in range(len(allAirports)):
        for b in allAirports.values():
            #checks to see if the country is the same as the chosen country and if the same the city will be added to a list
            if b.getCountry() == flightCountry:
                #if statement makes sure there are no duplicates
                if str(b.getCity()) not in str(cityListInTheCountry):
                    cityListInTheCountry.append(b.getCity())

    #nested for loops go through the allFlights
    for i in range(len(allFlights)):
        for j in allFlights.values():
            #for loop goes through the list with all the cities of the chosen country that was created above
            for word in cityListInTheCountry:
                for x in j:
                    #if the word in the city list i in the object then it will be added to the final list that contains the flight objects
                    if word in str(x):
                        if str(x.getFlightNumber()) not in str(countryList):
                            countryList.append(x)
    #returns a list with all the objects of the country as the origin or destination
    return countryList

#function finds if there is a direct flight and if not the program finds the connecting flight
def findFlightBetween(origAirport,destAirport):
    startAirport = origAirport
    endAirport = destAirport
    connectionFlights = set()
    empty = True
    finalAns = ""

    #checks to make sure that the airport code exist
    if startAirport.getCode() in allFlights.keys():
        #the nested for loop created to go through allFlights and get the objects
        for i in range(len(allFlights)):
            for j in allFlights.values():
                for x in j:
                    #if statement checks to see if there is a direct flight by checking if the origin and destination are the same
                    if (str(startAirport) == str(x.getOrigin())) and (str(x.getDestination()) == str(endAirport)):
                        #if the if statement is true the program will return the string of the airport codes
                        return "Direct Flight: " + startAirport.getCode() + " to " + endAirport.getCode()
                    #if statement checsk if there is no direct flight
                    elif(str(startAirport) != str(x.getOrigin())) and (str(x.getDestination()) != str(endAirport)):
                        #checks to see if the object destination code is in allFlights
                        if x.getDestination().getCode() in allFlights.keys():
                            #if statement checks if the endAirport city is in x destination and if x destination city is in the objects of startAirport
                            if (str(endAirport.getCity()) in str(allFlights.get(x.getDestination().getCode()))) and (str(x.getDestination().getCity()) in str(allFlights.get(startAirport.getCode()))):
                                #if the statement is true it will add it to the set, don't need another if statement for duplicates as sets don't apply duplicates
                                connectionFlights.add(x.getDestination().getCode())
                                #sets th final answer to the set so that it can be returned later
                                finalAns = connectionFlights
                                #empty varibale created to prevent -1 being returned
                                empty = False
                            #if there is no connecting flights then the program will return -1
                            if empty == True:
                                #if the endAirport city is not in x destination and if x destination city is not in the objects of startAirport it will set finalAns to -1
                                if (str(endAirport.getCity()) not in str(allFlights.get(x.getDestination().getCode()))) and (str(x.getDestination().getCity()) not in str(allFlights.get(startAirport.getCode()))):
                                    finalAns = -1
    #if there is no direct flight the program will either reuturn the set of connecting flights or -1 if there are no connecting flights
    return finalAns

#function returns the return flight
def findReturnFlight(firstFlight):
    deptFlight = firstFlight
    originAirport = deptFlight.getOrigin()
    arrivalAirport = deptFlight.getDestination()
    none = ""

    #nested for loop go throughs allFlights object
    for i in range(len(allFlights)):
        for j in allFlights.values():
            for x in j:
                #finds the return flight by checking if the object destination is the same as the originAirport and checks if the object origin is the same as the arrivalAirport
                if (str(x.getDestination()) == str(originAirport)) and (str(x.getOrigin()) == str(arrivalAirport)):
                    #if true it will return the object
                    return x
                #if not it will set the variable none to -1, as if the program returned -1 right away it wouldn't fully go through all of allFlights
                else:
                     none = -1
    #if there is no return flight it will return -1
    return none
