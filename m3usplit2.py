########################################################################################################################
#   m3usplit2 - script to split biiig m3u playlists for viewer comfort 
#   Splits file into multiple group files                                                                              #
#   Radio Erewan | radek@3210.pl                                                                                       #
#   Version 1.0 | 2021-03-30                                                                                           #
########################################################################################################################

import re
import sys, getopt

#   Function to iterate through file and collect all group names
def fillChannelList(lista, file):
    for index, line in enumerate(file):
        match = re.search(r'(group-title\=)(\")(.*)(\")', line)
        if match:
            if match.group(3) not in lista:
                lista.append(match.group(3))

#   Function to count all items asigned to a channel
def countChannel(channelName, file):
    marker = 0
    count = 0
    index = 0
    file.seek(0)
    for index, line in enumerate(file):
        match = re.search(r'(group-title\=)(\")(.*)(\")', line)
        if match:
            if match.group(3) == channelName:
                count += 1
    return count

#   Function to Append to outfile all items with specific channelName
def appendChannels(channelName, infile, outfile):
    marker = 0
    index = 0
    infile.seek(0)
    for index, line in enumerate(infile):
        match = re.search(r'(group-title\=)(\")(.*)(\")', line)
        if match:
            if match.group(3) == channelName:
                outfile.write(line)
 #  Set marker to 1 to write corresponding stream patch (next line)
                marker = 1
 #  We need to append also corresponding stream path
        elif marker == 1:
            outfile.write(line)
            marker = 0

#   Function to append to outfile all items with specific channelName additionaly splitting them alphabetically
def splitChannels(channelName, infile, outfile):
    marker = 0
    index = 0
    infile.seek(0)
    for index, line in enumerate(infile):
#   Searching for group
        match = re.search(r'(group-title\=)(\")(.*)(\")', line)
#   Searching for programName
        match2 = re.search(r'(tvg-name\=)(\")(.*)(\")', line)
        if match:
            if match.group(3) == channelName:
                if match2:
#   Replacing groupName tag with additional alphabet character
                    line = re.sub(r'(group-title\=)(\")(.*)(\")',
                                   'group-title=\"' + channelName + " " + match2.group(3)[0] + "\" ", line)
                outfile.write(line)
#  Set marker to 1 to write corresponding stream patch (next line)
                marker = 1
#  We need to append also corresponding stream path
        elif marker == 1:
            outfile.write(line)
            marker = 0

def main(argv):
    inputfile = 'infile.m3u'
    outputfile = 'outfile'
    append = False
    numbertosplit = 3000
    try:
        opts, args = getopt.getopt(argv,"has:i:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('m3usplit.py [-a] [-s xxxx] -i <inputfile> -o <outputfile>\n-a - appends to output\n-s number of items in group to alphabetical split (defaults to 3000)')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('m3usplit.py [-a] [-s xxxx] -i <inputfile> -o <outputfile>\n-a - appends to output\n-s number of items in group to alphabetical split (defaults to 3000)')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-a"):
            append = True
        elif opt in ("-s"):
            numbertosplit = int(arg)
    print ('Input file is "', inputfile)
    print ('Output file starts with "', outputfile)

#   Open input file for reading
    infile = open(inputfile, "r")
#   If not appending, we are cleaning contents of output file

#   Open output file for appending
#   Write first line of m3u

#   List of avaliable channels
    lista = list()
    fillChannelList(lista, infile)
    lista.sort ()
#   Iterating through channels to fill output
    for query in lista:
        if  query:
            
            fail = re.sub(r'[\\/*?:"<>|]',"",outputfile+"_"+query+'.m3u')
            outfile = open (fail, "w")
            outfile.write("#EXTM3U\n")
            size = countChannel(query, infile)
            splitChannels(query, infile, outfile)
            print ('Output file is: ', fail)

            outfile.close()


    infile.close()

    print ("We are done!")

if __name__ == "__main__":
   main(sys.argv[1:])

