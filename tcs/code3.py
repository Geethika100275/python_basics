# The Cruise Ship: A ship has people entering and exiting every hour for T hours. Given two arrays E[] (entry) and L[] (leaving), find the maximum number of guests on the ship at any given instance.
def ship(E,L,k):
    
    current=0
    max_people=0
    for i in range(k):
        
        current = current+E[i]-L[i]
        if current > max_people:
            max_people=current
    return max_people
E = [1,4,6,4,2,0]
L = [0,2,4,1,0,3]
k=int(input("Enter the particular hour"))
print(ship(E,L,k))
