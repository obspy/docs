from obspy.core import UTCDateTime

t_now = UTCDateTime()
t_bd = UTCDateTime(2011, 7, 9)
days = t_bd.julday - t_now.julday
print days, "days to my birthday"

bday = t_bd.isoweekday()
print "my birthday is day of week no.", bday
# we could also map this to a string representation using a dictionary
weekdays = {1: "monday", 2: "tuesday", 3: "wednesday", 4: "thursday",
            5: "friday", 6: "saturday", 7: "sunday"}
bday = weekdays[bday]
print "my birthday is a", bday

party = t_bd + (24 * 60 * 60)
while party.isoweekday() != 6:
    party += (24 * 60 * 60)
print "the party is going to be on", party.date
