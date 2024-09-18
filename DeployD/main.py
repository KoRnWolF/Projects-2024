import wmi

target_sys = wmi.WMI("192.168.10.191")
for disk in target_sys.Win32_LogicalDisk():
    drive_letter = disk.Caption
    #local disk test - Local Fixed Disk
    #Mapped disk test - Network Connection
    if disk.Description == "Network Connection":
        drive_detected = disk.Caption
        vol_name = disk.VolumeName
        print(f"{drive_detected} is a Mapped drive")
        print(f"Volume name :{vol_name}")
    # else:
    #     drive_detected = disk.Caption
    #     print(f"{drive_detected}is not Mapped drive")



#write code to check Windows version
#write code to copy files(Based on Windows version) and execute if found = 1


