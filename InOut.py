'''
Created on 20/10/2017

@author: bgw
'''

from datetime import datetime, timedelta
import sys
import getopt
import pycurl


USERNAME = "USERNAME"
PASSWORD = "PASSWORD"

ADDTIMEOPTIONS = ('Qtr', 'mQtr', 'Half', 'Hour', 'Day')
try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode


def setin():
    ''' Sets IN/OUT status to IN '''
    now = datetime.now()

    nexthour = (now + timedelta(hours=1)).strftime("%H:%M+%a+%d+%b")
    nextday = '08:30+{}'.format((now + timedelta(days=1)).strftime("%a+%d+%b"))
    setstatus(nexthour, nextday)

    print "Set status to IN"

def setfinishedforday():
    ''' Sets IN/OUT status to Finished for the Day '''
    now = datetime.now()

    nexthour = (now + timedelta(hours=1)).strftime("%H:%M+%a+%d+%b")
    nextday = '08:30+{}'.format((now + timedelta(days=1)).strftime("%a+%d+%b"))

    setstatus(nexthour, nextday, staddtime='Day', stwhere='Finished+for+the+day')

    print "Set status to Finished for day"

def setout(location, changestr='Qtr'):
    ''' Sets IN/OUT status to provided location for provided time '''


    if changestr not in ADDTIMEOPTIONS:
        helpme()

    location = location.replace(" ", "+")

    now = datetime.now()

    nexthour = (now + timedelta(hours=1)).strftime("%H:%M+%a+%d+%b")
    nextday = '08:30+{}'.format((now + timedelta(days=1)).strftime("%a+%d+%b"))


    setstatus(nexthour, nextday, staddtime=changestr, stwhere=location)

    print "Put you at %s for %s" % (location, changestr)


def setstatus(nxhour, nxday, sttype='', staddtime='Auto', stwhere='In', stback=''):
    '''Creates the data string and performs the pycurl request'''

    data = "NextHour={}&NextDay={}&Type={}&AddTime={}&Where={}&BackAt={}".format(nxhour, nxday,
                                                                                 sttype, staddtime,
                                                                                 stwhere, stback)
    url_dir = "http://intranet.powernet.inet/Staff/MyInOut.asp"
    conn = pycurl.Curl()
    conn.setopt(pycurl.URL, url_dir)
    conn.setopt(pycurl.POSTFIELDS, data)
    conn.setopt(pycurl.USERPWD, "{}:{}".format(USERNAME, PASSWORD))
    conn.setopt(pycurl.VERBOSE, 0)

    conn.perform()
    conn.close()

def helpme():
    ''' Prints out how to use this program '''
    print "InOut.py"
    print "\n\nCommands: \n"
    print "-h: Brings up help (This), or"
    print "-i: Set to in, or"
    print "-f: Finished for the day, or"
    print "-o 'LOCATION','TIME TO ADD': Puts status to 'LOCATION' and adds specified 'TIME'."
    print "If -o is called must provide 'LOCATION' and 'TIME TO ADD'"
    print "TIME must be in the following list:"
    print "'Qtr' - 15 mins\n'mQtr' - negative 15 mins"
    print "'Half' - 30 mins\n'Hour' - an hour\n'Day' - a day"
    exit(1)




def main(argv):
    ''' Performs the required function call depending on the input arguments '''


    try:
        opts, args = getopt.getopt(argv, "hifo:")
    except getopt.GetoptError:
        helpme()
    for opt, arg in opts:

        if opt == '-h':
            helpme()
        if opt == "-i":
            setin()
        elif opt == "-o":
            arguments = arg.split(",")
            if len(arguments) != 2:
                helpme()
            setout(arguments[0], arguments[1])
        elif opt == "-f":
            setfinishedforday()


if __name__ == '__main__':
    main(sys.argv[1:])
