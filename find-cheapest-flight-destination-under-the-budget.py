class Flight:
    def __init__(self, origin, destination, rent) -> None:
        self.origin = origin
        self.destination = destination
        self.rent = rent
    
flights = [Flight("EDI", "LHR", 140),
            Flight("EDI", "NYK", 420),
            Flight("EDI", "DEL", 480),
            Flight("EDI", "TKY", 330),
            Flight("EDI", "LHR", 98)]
        
def createItinerary(budget):
    unique_destination = []
    for flightObj in flights:
        if flightObj.rent <= budget:
            unique_destination.append(flightObj.destination)

    print("\n".join(map(str, set(unique_destination))))

createItinerary(int(input("Enter your budget: ")))
