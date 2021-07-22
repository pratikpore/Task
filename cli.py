import argparse
import unittest
from unittest.suite import TestSuite
from runner import execute
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--test", help = "command to execute", choices=['pvcreate','vgcreate','lvcreate'])

parser.add_argument("--disk",nargs='+', help = "name of disk")
parser.add_argument('--lvname', help="logical volume name")
parser.add_argument('--size', help="determine size of the lv")
parser.add_argument('--vgname', help="volume group name for allocating lv")
args = parser.parse_args()

cmd = args.test
disk_name = args.disk
lvname = args.lvname
size = args.size
vgname = args.vgname



if __name__ == '__main__':
    import test
    suite = TestSuite()
    loader = unittest.TestLoader()
    if cmd == 'pvcreate':
        suite.addTests(loader.loadTestsFromName("test.Lvm.test_pvcreate"))
    if cmd == 'vgcreate':
        suite.addTests(loader.loadTestsFromName("test.Lvm.test_vgcreate"))
    if cmd == 'lvcreate':
        suite.addTests(loader.loadTestsFromName("test.Lvm.test_xlvcreate"))


    runner = unittest.TextTestRunner()
    runner.run(suite)


