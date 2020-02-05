import glob
import sys
import subprocess
#import pathlib

# get MP4 file list in the designated directory
# this script needs argument for directory which contains MP4 file

# Constants
# AccGPS = 1000 # no need, as acccuracy does not matter to gpmd2csv
# FixFPS = 3    # no need, as accuracy does not matter to gpmd2csv

print(sys.argv[1])
#p_temp = pathlib.Path(sys.argv[1])

fileList = []
for p in glob.glob(sys.argv[1] + "/*.MP4"):
    print(p)
    fileList.append(p)

# convert mp4 to bin (recursive)
binList = []
for f in fileList:
    binName = str(f) + ".bin"
    try:
        # ffmpeg
        cmd = "ffmpeg -y -i " + f + " -codec copy -map 0:3 -f rawvideo " + binName
        subprocess.check_call(cmd.split())  # bad to have constants 0:3
    except:
        print("subprocess.check_call() in bin convert failed")

    binList.append(binName)


binList =[]
for p in glob.glob(sys.argv[1] + "/*.bin"):
    print(p)
    binList.append(p)

# convert bin to csv (recursive)
for b in binList:
    csv = b + ".csv"
    print(csv)
    try:
        cmd = "/home/motsuka/go/bin/gpmd2csv -i " + b + " -o " + csv
        print(cmd)
        subprocess.check_call(cmd.split())
    except:
        print("subprocess.check_call() in csv convert failed")
#'''