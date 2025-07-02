from calendlink import CalendLink
from Parser import Parser
def main():
    inp = "get rid of my Meeting with team at 3 PM on Friday, location: Zoom, description: Discuss project updates."
    test = Parser(inp)
    parsed_event = test.parse()
    print("Parsed Event:", parsed_event)
    

if __name__ == "__main__":
    main()