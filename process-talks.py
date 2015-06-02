#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

 GridPP - Processing Talks

 See the README.md file and the GitHub wiki for more information.

 http://www.gridpp.ac.uk/talks

"""

# Import the code needed to manage files.
import os, glob

#...for parsing the arguments.
import argparse

#...for the logging.
import logging as lg

#...for the Talk wrapper class.
from records.talks import Talk, TALK_CATEGORIES

if __name__ == "__main__":

    print("*")
    print("*========================*")
    print("* GridPP - Process Talks *")
    print("*========================*")

    # Get the datafile path from the command line.
    parser = argparse.ArgumentParser()
    parser.add_argument("inputPath",       help="Path to the input dataset.")
    parser.add_argument("outputPath",      help="The path for the output files.")
    parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
    args = parser.parse_args()

    ## The path to the data file.
    datapath = args.inputPath

    ## The output path.
    outputpath = args.outputPath

    # Set the logging level.
    if args.verbose:
        level=lg.DEBUG
    else:
        level=lg.INFO

    # Configure the logging.
    lg.basicConfig(filename=os.path.join(outputpath, 'log_process-talks.log'), filemode='w', level=level)

    print("*")
    print("* Input path          : '%s'" % (datapath))
    print("* Output path         : '%s'" % (outputpath))
    print("*")


    # Get the TSV file.
    tf =  open(datapath, "r")
    lines = tf.readlines()
    tf.close()

    ## Dictionary of talks.
    talks = {}
    #
    for i in range(1,len(lines)):

        ## The current talk.
        talk = Talk(lines[i])

        # Populate the dictionary.
        talks[talk] = talk.getCategory()

    ## The HTML string of talks.
    hs = ""

    # Loop over the categories.
    for i, category in TALK_CATEGORIES.iteritems():
        hs += "\n\n\n%s\n\n\n" % (category)

        ## List for the talks sorted by category.
        sortedtalks = []
        #
        # Populate the list.
        for talk, cat in talks.iteritems():
            if cat == category:
                sortedtalks.append(talk)

        # Sort by date.
        sortedtalks = sorted(sortedtalks, reverse=True)
        #
        for talk in sortedtalks:
            hs += talk.getWebEntry()
            hs += "\n"

    # Write the HTML file.
    with open(os.path.join(outputpath, "talks.html"), "w") as hf:
        hf.write(hs)
