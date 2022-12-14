#!/usr/bin/env python3



Credit_bookshelf = [("Chase", "112322", "793", "VantageScore3.0", "850"),
                    ("WellsFargo", "112722", "799", "FICO9 -Experian", "850"),
                    ("Bank of America", "112122", "798", "FICO -Transunion", "850"),
                    ("Discover", "111922", "798", "FICO -Transunion", "850"),
                    ("Citi", "112222", "798", "FICO8 -Equifax", "900")]


class Score:
    def __init__(self, name, date, score, issuer, maximum):
        self.name = name
        self.date = date
        self.score = score
        self.issuer = issuer
        self.maximum = maximum

    """use below to output what you want, default is the memory location only"""
    def __repr__(self):
        return str(self.name) + " @" + str(self.score) + " || last_monthly_update: " + str(self.date) + "\n" " >> type: " \
               + str(self.issuer) + " >> Max_score is: " + str(self.maximum)


bookshelf = []
for (name, date, score, issuer, maximum) in Credit_bookshelf:
    cred = Score(name, date, score, issuer, maximum)
    bookshelf.append(cred)

for x in bookshelf:
    print(x)
    print("\n")


