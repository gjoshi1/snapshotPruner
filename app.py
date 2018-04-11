from datetime import datetime,time, tzinfo, timedelta,date
from operator import itemgetter
import calendar


#The Problem
#Every night, an automated process captures a snapshot of a database and uploads that snapshot to a persistent data store. These snapshots are very large and to reduce our storage costs we want to prune some of them.

#Objective
#Implement a function that will be used to determine which snapshots can be pruned. The function will receive a single parameter that is a list of snapshots, and is expected to return a list of snapshot IDs that can be pruned.

#Phase 1
#Return all snapshot IDs for only the snapshots that have a status of "available" and the ID starts with "beta" or "test" regardless of when the snapshot was created.
def getSnapshotsP1(snapshots):
    snapshotIds = []

    for snapshot in snapshots:
        if(snapshot[2] == 'available'):
            if(snapshot[0].startswith('beta') or snapshot[0].startswith('test')):
                snapshotIds.append(snapshot[0])

    print "PHASE 1 : "+ str(snapshotIds)
    return snapshotIds


#Phase 2
#Return all snapshot IDs for only the snapshots that have a status of "available" and:

#Match any snapshots detected from Phase 1,
#ID starts with "live" and ends with "final" and was not created during the current month, the previous month, or the month before. If the current month is January, you only want to return snapshots created before November.
def getSnapshotsP2(snapshots,snapshotIds,currentDate=datetime.today()):

    prevDate = next_month(currentDate, -3)

    for snapshot in snapshots:
        if(snapshot[2] == 'available'):
            if(snapshot[0].startswith('live') and snapshot[0].endswith('final')):
                if(snapshot[1] < prevDate):
                    snapshotIds.append(snapshot[0])

    print "PHASE 2 : "+str(snapshotIds)
    return snapshotIds

#Phase 3
#Return all snapshot IDs for only the snapshots that have a status of "available" and:

#Match any snapshots detected from Phase 2,
#ID starts with "live-seed", was not created during the current month, the previous month, or the month before, and is not the first snapshot of the month. If the current month is January, you only want to return snapshots created before November if they are not the first snapshot of the month.
def getSnapshotsP3(snapshots,snapshotIds,currentDate=datetime.today()):

    prevDate = next_month(currentDate, -3)
    monthsnapshots = {}
    monthKeys={}
    for snapshot in snapshots:
        if(snapshot[2] == 'available' and snapshot[0].startswith('live-seed') ):
            #if(snapshot[1] < prevDate):
                #create tuple of month and snapshot so we can later
                #separate the lists as per month and pick the roght snapshot
                monthsnapshots.update({snapshot[1]:snapshot})

                #get all months
                monthKeys.update({snapshot[1].month:snapshot[1].month})


    for m in monthKeys.keys() :
        snapshotIds += (getMonthSnapshotsExcludingFirst(monthsnapshots.values(),m))

    print "PHASE 3 : "+ str(snapshotIds)
    return snapshotIds

def getMonthSnapshotsExcludingFirst(snapshots,month):

    monthSnapshotIds = []
    for snapshot in snapshots:
        if (snapshot[1].month == month):
            monthSnapshotIds.append(snapshot[0])

    monthSnapshotIds.sort()

    #remove the first snapshot of the month
    monthSnapshotIds.pop()

    return monthSnapshotIds

#https://stackoverflow.com/questions/3424899/whats-the-simplest-way-to-subtract-a-month-from-a-date-in-python
#get date before/after X month.
def next_month(given_date, month):
    yyyy = int(((given_date.year * 12 + given_date.month) + month)/12)
    mm = int(((given_date.year * 12 + given_date.month) + month)%12)

    if mm == 0:
        yyyy -= 1
        mm = 12

    return given_date.replace(year=yyyy, month=mm)
