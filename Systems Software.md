# Systems Software

## OCR – Optical Character Recognition
- OCR converts images of text into editable text with separate characters.
- OMR (Optical Mark Recognition) reads multi-choice answer papers and is able to recognise, based off which box is ticked, whether the candidate is right or wrong.
- Barcodes are a sequence of black and white lines, which are used to store a unique key for that product.
- The barcode allows devices reading the barcode to look up data about the product on a database.
- Different values are represented by different thicknesses of lines.
- At the start and end of the barcode there are terminators that allow the reader to know when the barcode begins and ends.
<br>

## The Four Types of Software
![image](https://user-images.githubusercontent.com/90699946/137457279-a02a7cd8-5e94-4b93-9686-2bd238842bd1.png)
<br>
<br>

## Sensors and Actuators
An actuator is able to create something or make something happen. It is an output device which can cause physical movement.
Examples include motors, and automatic doors. Sensors and actuators form what is known as a feedback loop.

When a sensor detects a change, it tells the actuator to make a physical change to the system. This could, in turn, cause a change in what the sensors are detecting, which in turn can cause further activation of the actuator.

![image](https://user-images.githubusercontent.com/90699946/137457675-b9f01edd-7212-4d8a-9fe3-aab571d78085.png)

<br>

## Operating Systems
Systems software allows control over the hardware and software of the computer. An operating system can have:
- Processor Management
- Memory Management
- Peripheral Management
- Utility Software
- Networking
- Security
- User Interface

### Processor Management
Processor management means the operating system will divide the processor up into sections, each assigned to carry out seperate tasks.

### Memory Management
Memory management means controlling and coordinating memory, assigning portions called "blocks" to various running programs to optimise overall system performance.

### Peripheral Management
Peripheral devices, such as speakers or keyboards, are hardware devices that are connected to the computer and can communicate with it. They are able to do this because of the OS, which controls the connection between all hardware, software and peripheral devices in a computer system.

### Utility Software
Utility software is designed to maintain a computer system and optimise it's functions. These are several examples of utility software:
- Data compression
- Defragmentation
- Backups
- Encryption

### Networking
Processor management means the operating system will divide the processor up into sections, each assigned to carry out seperate tasks.


### Types of Software
![image](https://user-images.githubusercontent.com/90699946/143052421-9b2d983d-6fcc-4583-9ecf-6d3355828a12.png)


## Memory Management

The memory manager must split RAM into workable chunks of storage and allocate those chunks to processes in a fair manner. As processes start and stop at different times and have different memory demands, keeping track of what memory is free becomes a challenge. Allocation of RAM can be done through two managing techniques that will be explored in this chapter, both employing a table to monitor which process has been allocated which chunk of memory. 
This allows RAM to be shared without worrying about any processes accidentally overwriting each other or gaining unauthorised access, as their access will be strictly monitored by the OS.
Security is a core concern for memory management. If processes could inspect or change each other’s memory, this could bypass many security protocols put in place to protect user data. For example, if a process could inspect the data from your web browser, it could very easily manipulate what you see on screen.
Finally, the last consideration is the use of virtual memory to extend memory beyond what is physically available.
It is key to remember at this stage that RAM will hold:
- the OS
- currently running programs
- current files and data you are working on







