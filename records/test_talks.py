#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...the usual suspects.
import os, inspect

#...for the unit testing.
import unittest

#...for the logging.
import logging as lg

#...for the Pixelman dataset wrapper.
from talks import Talk

class TalkTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_talk(self):

        tf = open("testdata/testtalk.tsv", "r")
        lines = tf.readlines()
        tf.close()

        ## The test talk.
        talk = Talk(lines[1])

        # The talk title.
        self.assertEqual(talk.getTalkTitle(), "A recent view of OSSEC and Elasticsearch at Scotgrid Glasgow")

        # The talk date string.
        self.assertEqual(talk.getTalkDateString(), "24 Mar 2015")

        # The talk URL.
        self.assertEqual(talk.getTalkUrl(), "https://indico.cern.ch/event/346931/session/3/contribution/39")

        # The authors.
        self.assertEqual(talk.getAuthors(), "G. Roy, S. Skipsey, G. Qin, G. Stewart, D. Britton")

        # The event URL.
        self.assertEqual(talk.getEventUrl(), "https://indico.cern.ch/event/346931/")

        # The web entry.
        self.assertEqual(talk.getWebEntry(), """<li>
<a href="https://indico.cern.ch/event/346931/session/3/contribution/39" target="_blank">A recent view of OSSEC and Elasticsearch at Scotgrid Glasgow</a> <br />
G. Roy, S. Skipsey, G. Qin, G. Stewart, D. Britton, <a href="https://indico.cern.ch/event/346931/" target="_blank">HEPiX Spring 2015 Workshop</a>, 24 Mar 2015.
</li>""")

        # The category.
        self.assertEqual(talk.getCategory(), "Data Storage Management")


if __name__ == "__main__":

    lg.basicConfig(filename='log_test_talks.log', filemode='w', level=lg.DEBUG)

    lg.info("")
    lg.info("==========================================")
    lg.info(" Logger output from records/test_talks.py ")
    lg.info("==========================================")
    lg.info("")

    unittest.main()
