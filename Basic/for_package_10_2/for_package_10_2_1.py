class ThailandPackage:
    def detail(self):
        print("[Thailand 5 days package] blah blah ")

if __name__ == "__main__":
    print("Thailand module directly executed")
    print("this message appeared only when module is directly executed ")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand module non-directly executed")