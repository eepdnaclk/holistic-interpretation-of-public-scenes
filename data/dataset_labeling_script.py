import subprocess
import argparse
from glob import glob

parser = argparse.ArgumentParser()

parser.add_argument("--input", "-i", type=str, dest="input", description="Input folder")
parser.add_argument("--output", "-o", type=str, dest="output", description="Output folder")
parser.add_argument("--suffix", "-s", type=str, dest="suffix", description="Suffix added to json as : vidName_suffix.json")
parser.add_argument("--file", "-f", type=str, dest="file", description="Python file to be run")
parser.add_argument("--ftype", "-f", type=str, dest="ftype", default="mp4", description="Extension of video file")

args = parser.parse_args()

src = args.input
dest = args.output
suffix = args.suffix
py_file = args.file

src_files = list(map(lambda x:x.replace("\\", "/"), glob(src + "/*.%s"%args.ftype)))

for file in src_files:
    file_name = file.split("/")[-1].rstrip(".%s"%args.ftype)
    out_name = dest.rstrip('/') + "/%s-%s.json"%(file_name, suffix)

    cmd = "python %s -v %s -y %s"%(py_file, file, out_name)
    print(cmd)

    subprocess.call(["python", py_file, "-v", file, "-y", out_name])



    # subprocess.call("test1.py", shell=True)