#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...for the logging.
import logging as lg

#...for the time (being).
import time

## The GridPP talk categories.
TALK_CATEGORIES = {
    1:"Official",
    2:"Overviews",
    3:"Data Storage Management",
    4:"Configuration Management",
    5:"Workload Management",
    6:"Information & Monitoring",
    7:"Security",
    8:"Applications",
    9:"Networking",
    10:"Grid Infrastructure",
    11:"Particle Physics",
    12:"Other"
    }

class Talk:
    """ Wrapper class for GridPP talks. """

    def __init__(self, l):
        """
        Constructor.

        @param [in] l Comma Separated Value line containing the talk information.
        """

        ## The values.
        vs = l.split("\t")

        ## The talk date string.
        self.__date_str = vs[7]

        ## The talk date.
        self.__time = time.strptime(self.__date_str, "%d/%m/%Y")

        ## The talk date in seconds [s].
        self.__time_sec = time.mktime(self.__time)

        ## The talk title.
        self.__title = vs[5]

        ## The talk URL.
        self.__talk_url = vs[8]

        ## The authors.
        self.__authors = vs[4]

        ## The event title.
        self.__event_title = vs [6]

        ## The event URL.
        self.__event_url = vs[10]

        ## The talk category.
        self.__category = vs[12].strip()

    def __lt__(self, other):
        if self.__time_sec == other.__time_sec:
            return self.__title < self.__title
        else:
            return self.__time_sec < other.__time_sec

    def getTalkTitle(self):
        return self.__title

    def getTalkUrl(self):
        return self.__talk_url

    def getAuthors(self):
        return self.__authors

    def getTalkDateString(self):
        return time.strftime("%d %b %Y", self.__time)

    def getEventTitle(self):
        return self.__event_title

    def getEventUrl(self):
        return self.__event_url

    def getCategory(self):
        return self.__category

    def getWebEntry(self):
        """
        Get a web entry formattted for the GridPP website.

        * See http://www.gridpp.ac.uk/talks
        """

        ## The HTML string to return.
        s = """<li>
<a href="TALK_URL" target="_blank">TALK_TITLE</a> <br />
AUTHORS, <a href="EVENT_URL" target="_blank">EVENT_TITLE</a>, DATE_STRING.
</li>"""

        s = s.replace("TALK_URL",    self.getTalkUrl())
        s = s.replace("TALK_TITLE",  self.getTalkTitle())
        s = s.replace("AUTHORS",     self.getAuthors())
        s = s.replace("EVENT_URL",   self.getEventUrl())
        s = s.replace("EVENT_TITLE", self.getEventTitle())
        s = s.replace("DATE_STRING", self.getTalkDateString())

        return s
