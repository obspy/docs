from obspy.xseed import Parser
sp = Parser("dataless.seed")
sp.writeXSEED("dataless.seed")
