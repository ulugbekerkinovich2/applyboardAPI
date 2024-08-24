import requests
import icecream as ic
import time

def list_universities(request):
    url = "https://www.applyboard.com/quick_search.json?countries%5B%5D=USA&countries%5B%5D=Canada&countries%5B%5D=United+Kingdom&countries%5B%5D=Australia&countries%5B%5D=Ireland&group_by_school=true&only_direct=false&sort_by=school_rank&v=2"
    response = requests.get(url)
    data = response.json()
    
    universities = []
    for school in data["schools"]['schoolHashMap']:
        ic(school)
        