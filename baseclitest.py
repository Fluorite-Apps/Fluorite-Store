import subprocess

#subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo test', shell=True)

POWERSHELL_PATH = "C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"
#command = "irm get.scoop.sh | iex"

@staticmethod
def run_ftp_upload_powershell_script(command):
    commandline_options = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', command]
    process_result = subprocess.run(commandline_options, stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
    # print(process_result.returncode)
    print(process_result.stdout)
    # print(process_result.stderr)

#run_ftp_upload_powershell_script(command)



while True:
    print("Welcome to Scoop GUI CLI base program")
    cmd = input(">> ")
    # cmd = (str("scoop ") + str(cmd))
    cmd = str(cmd)
    run_ftp_upload_powershell_script(cmd)


