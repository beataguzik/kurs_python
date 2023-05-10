skopiowac
def show_month(name, days):
    print(name)
    print()

    for day in days:
        if day < 10:
            day = f'0{day}'




show_month('january', range(31))

data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]

#1
january = range(1,31)
for i in january:
       print("january", i)
