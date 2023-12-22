SVCS, nicknamed "Dracula's Castle", is the name given to any platform that I use for virtualization.

## Current
In early May 2023, I was given an HP BladeSystem C3000 chassis with three HP ProLiant BL460c G8 systems installed along with many other computer parts.

### SVCS1
SVCS1 uses the platform designated "Methamphetamine". The system is currently used for general purpose virtualization.

Specifications:

- System: HP ProLiant BL460c G8
- CPUs: 2x Intel Xeon E5-2697 v2
- Memory: 8x16GB (128GB) Micron Technology PC3-12800R 2Rx4 Registered ECC
- Storage: 1x HGST 600GB 10000RPM 6Gb/s SAS

### SVCS2
SVCS2 uses the hardware platform "Dextroamphetamine". I could not actually get the system to boot from the hard drive. Since SVCS1 "Methamphetamine" and SVCS3 "Lisdexamfetamine" are more than enough for my current needs, I have not put this system in production yet.

Specifications:

- System: HP ProLiant BL460c G8
- CPUs: 2x Intel Xeon E5-2643 v2
- Memory: 64GB (8x8GB) Nanya Technology PC3-12800R 1Rx4 Registered ECC
- Storage: 1x HGST 600GB 10000RPM 6Gb/s SAS

### SVCS3
SVCS3 uses the hardware platform "Lisdexamfetamine". This is the oldest BL460c G8 in use. From June 8, 2023 to October 9, 2023, the system reported a motherboard error that was later discovered to just be the BIOS version not supporting the Intel Xeon Ivy Bridge CPUs that I attempted to install on June 8. After the original E5-2650 Sandy Bridge CPUs were installed, the system operated as normal.

Specifications:

- System: HP ProLiant BL460c G8
- CPUs: 2x Intel Xeon E5-2650
- Memory: 128GB (8x16GB) SK hynix PC3-12800R 2Rx4 Registered ECC
- Storage: 1x HGST 600GB 10000RPM 6Gb/s SAS

## Former
From February 2023 to the introduction of the systems above, the motherboard ["Polyethylene"](../pc_pe/) was used.