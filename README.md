# LVM_Task
In this code we have covered some basic topics of Python Unit Test Framework, such as - Assertion, Fixtures, Testloader, Test Suite, Skip Test, etc.

With the help of this code we are able to create/remove PV, LV, VG.


The commands used for the same are as follows -

Creating PV - sudo python3 cli.py --disk pvcreate /dev/sdb1

Creating PV - sudo python3 cli.py --test vgcreate /dev/sdb1 --vgname vg1

Creating PV - sudo python3 cli.py --test lvcreate /dev/sdb1 --vgname vg1 --lvname lv1 --size 2000M


If you have any doubts, you can refer the PNG file, which shows you the output in shell.
