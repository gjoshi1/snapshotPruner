import unittest
from datetime import datetime
import app

class TestSnapshotPrune(unittest.TestCase):

    def setUp(self):
        #test date to check results as the results vary per date
        #the below results have been obtained for a fixed test date.
        self.testDate = datetime.strptime('11042018', "%d%m%Y")
        self.snapshotidsphase1 = ['beta-1', 'beta-2', 'beta-1-final']
        self.snapshotidsphase2 = ['beta-1', 'beta-2', 'beta-1-final', 'live-1-final', 'live-2-final']
        self.snapshotidsphase3 = ['beta-1', 'beta-2', 'beta-1-final', 'live-1-final', 'live-2-final', 'live-seed-1', 'live-seed-3']
        self.snapshots = [
            ('beta-1', datetime(2017, 10, 1, 14, 10, 30), 'available'),
            ('beta-2', datetime(2018, 1, 20, 18, 1, 34), 'available'),
            ('beta-3', datetime(2018, 1, 22, 8, 45, 22), 'pending'),
            ('beta-1-final', datetime(2018, 1, 18, 12, 42, 37), 'available'),
            ('live-1-final', datetime(2017, 10, 16, 3, 56, 32), 'available'),
            ('live-2-final', datetime(2017, 12, 12, 10, 23, 34), 'available'),
            ('live-seed-1', datetime(2017, 10, 18, 11, 9, 29), 'available'),
            ('live-seed-2', datetime(2017, 10, 17, 11, 10, 25), 'available'),
            ('live-seed-3', datetime(2017, 11, 18, 11, 8, 44), 'available'),
            ('live-seed-4', datetime(2017, 11, 17, 11, 11, 47), 'available'),]



    def test_phase1(self):

        print "TEST PHASE 1"

        phase1 = app.getSnapshotsP1(self.snapshots)
        #correct result
        self.assertEqual(phase1, self.snapshotidsphase1)


    def test_phase2(self):

        print "TEST PHASE 2"
        phase2 = app.getSnapshotsP2(self.snapshots,self.snapshotidsphase1,self.testDate)
        self.assertEqual(phase2, self.snapshotidsphase2)


    def test_phase3(self):

        print "TEST PHASE 3"
        phase3 = app.getSnapshotsP3(self.snapshots,self.snapshotidsphase2,self.testDate)
        self.assertEqual(phase3, self.snapshotidsphase3)




if __name__ == '__main__':
    unittest.main()
