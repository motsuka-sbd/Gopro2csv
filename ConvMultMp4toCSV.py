import glob
import sys
import subprocess

# get MP4 file list in the designated directory
# this script needs argument for directory which contains MP4 file

# Constants
# AccGPS = 1000 # no need, as acccuracy does not matter to gpmd2csv
# FixFPS = 3    # no need, as accuracy does not matter to gpmd2csv

#fileList = glob.glob(sys.argv + "/*.MP4")
print(glob.glob(sys.argv + "/*.MP4"))
fileList = glob.glob(sys.argv + "/*.MP4")

# convert mp4 to bin (recursive)
binList = []
for f in fileList:
    print(f)
    binName = str(f) + ".bin"
    print(binName)
    try:
        # ffmpeg
        subprocess.check_call("ffmpeg -y -i " + f + "-codec copy -map 0:3 -f rawvideo " + binName)  # bad to have constants 0:3
    except:
        print("subprocess.check_call() in bin convert failed")

    binList.append(binName)

# convert bin to csv (recursive)
for b in binList:
    csv = b + ".csv"
    try:
        subprocess.check_call("gpmd2csv -i " + b + " -o " + csv)
    except:
        print("subprocess.check_call() in csv convert failed")
