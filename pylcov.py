import os
import subprocess
import sys


def main(params):
    gcov_input_dir=params[1]
    gcov_tool_exe=params[2]
    gcov_fct_report=params[3]
    gcov_params="{0} -i --function-summaries {1}/{2}"

    for file in os.listdir(gcov_input_dir):
        if file.endswith(".o"):
            #we have a c file
            c_file=file.replace(".o",".c")
            cmd=gcov_params.format(gcov_tool_exe,gcov_input_dir,c_file)

            result = subprocess.run(cmd, capture_output=True, text=True)

            print(result.stdout)

    pass

#param 1 - directory with gcov data
#param 2 - gcov tool location
#param 3 - html report

if __name__=="__main__":
    if len(sys.argv) != 4:
        print("something went wrong")
    else:
        main(sys.argv)