from obspy.core import UTCDateTime

years = range(2011, 2061)
for year in years:
    t_bd = UTCDateTime(year, 7, 9)
    party = t_bd + (24 * 60 * 60)
    while party.isoweekday() != 5:
        party += 24 * 60 * 60
    print year, "the party is on", party.date
    
t = UTCDateTime()
count = 0
while t.year < 2013:
    t += 24 * 60 * 60
    if t.weekday() == 4 and t.day == 13:
        count += 1
        print t.date, "is a friday 13th"
print count, "days to take off"
