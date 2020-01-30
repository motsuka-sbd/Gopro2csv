import glob
import sys
import subprocess

# get MP4 file list in the designated directory
# this script needs argument for directory which contains MP4 file

fileList = glob.glob(sys.argv + "/*.MP4")

# convert mp4 to bin (recursive)
binList = []
for f in fileList:
    binName = str(f) + ".bin"
    try:
        subprocess.check_call("echo ffmpeg -y -i " + f + "-codec copy -map 0:3 -f rawvideo " + binName)
    except:
        print("subprocess.check_call() in bin convert failed")

    binList.append(binName)

# convert bin to csv (recursive)
for f in binList:
    csv = f + ".csv"
    try:
        subprocess.check_call("gpmd2csv -i " + f + " -o " + csv)
    except:
        print("subprocess.check_call() in csv convert failed")
