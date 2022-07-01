# Structure and function of the processor

## Memory and the CPU
![image](https://user-images.githubusercontent.com/90699946/136962173-be2c26ac-d544-499b-8f97-9dd1243aa251.png)

### CPU
The Central Processing Unit (CPU), is made up of several components which enable it to execute instructions. These include:
- Control Unit
- Buses
- Arithmetic Logic Unit (ALU)
- Registers

<br>

### The Control Unit (CU)
- Used for the co-ordination of the CPU activities.
- It sends electrical impulses to the other CPU components to control the flow of data around the system.
- The Control Unit takes in the next instruction, decodes it into several steps, manages its execution and stores the result back in memory or registers.

<br>

### Buses

A **bus** is a set of parallel wires connecting two or more components of a computer. The CPU is connected to main memory by three seperate buses:
- When the CPU wishes to access a particular memory location, it sends the address to memory on the **address bus**.
- The data in that location is then returned to the CPU on the **data bus**.
- Control signals are sent along the **control bus**.

Data and control signals travel in both directions between the CPU, memory and peripheral controllers. Addresses travel in only one direction along the address bus, from the CPU to it's destination. The three buses are known collectively as the **system bus**.

#### Control Bus
- The purpose of the Control Bus is to carry electrical signals from the CPU to other components. These impulses can carry command, timing or status information.
- The control bus also carries the clock speed pulses, and transmits data in only one direction.

#### Data Bus
- The data bus provides a path for data and instructions to travel along between system components.

#### Address Bus
- Memory is divided up into unit called **words**. These words are used as operands in program insructions.
- A word is typically 16 or 32 bits, and each word in memory has a different address.
- The Address Bus carries these word addresses between components so that the data can be retrieved and sent back to the CPU.

<br>

### Arithmetic Logic Unit (ALU)

- Carries out arithmetic and logical operations within the CPU.
- The results are then stored in the Accumulator.
- Arithmetic operations performs instructions on fixed or floating point numbers.
- Logical operations carries out Boolean logic operations

<br>

### Registers

#### The Program Counter (PC)
- Holds the address of the next instruction to be executed.
- After every executed instruction the counter will increment so that it holds the address of the next instruction.
- The next insruction can simply be the next in sequence, or, if the current instruction is a branch or jump instruction, it can be copied from the Current Instruction Register.

#### Current Instruction Register (CIR)
- Holds the current instruction being executed.

#### Memory Address Register (MAR)
- Holds the address of the current instruction being executed.
- It locates the place in memory (copied from the program counter) where the instruction soon to be in use is.

#### Memory Data Register (MDR)
- Used to temporarily store the data read or written from memory.
- The data is copied from the memory value located by the MAR, then stored here until sent to the CIR.

#### Status Register (SR)
- Used in case of a data interruption or overflow.
- It is made up of several bits that are used to indicate whether there has been a failure of some sort within the CPU.

<br>

### Fetch-Decode-Execute Cycle

#### Fetch
- The address of the next instruction is copied from the Program Counter to the MAR.
- The instruction held at that address is copied to the MDR, and the content of the Program Counter is incremented.
- The contents of the MDR are copied to the CIR.

#### Decode
The instruction in the CIR is split up into **opcode** and **operand**. The opcode is used to determine the type of instruction and what hardware to use to execute it, and the operand holds either:
- The address of the data to be used with the operation, which is then copied to the MDR
- The actual data to be operated on, which will be copied to the MDR

#### Execute
The data to be operated on may be passed to the ALU depending on the instructions, and the instruction is carried out.

<br>

<br>

## Processor Performance

The main factors affecting CPU performance are:
- Clock speed
- Number of cores
- Cache

### Clock Speed
- The **system clock** generates signals called **clock pulses** that switch between 1 and 0 several million times per second. CPU operations can only start as the clock changes from 0 to 1, and this helps synchronise all the CPU components.
- These clock pulses are transmitted via the **control unit**.
- **Clock speed** is the number of pulses the system clock generates per second. One pulse is equal to one Hertz (Hz).
- Typical clock speeds for a PC are between 2 and 4 GHz.

### Number of Cores
- However many tasks a computer can carry out simultaneously depends on the **number of cores**. Each core can theoretically process an instruction at the same time as another, improving processor performance.
- However, this doesn't always improve performance if the software can't take advantage of all the processors.

### Cache
- **Cache** is a very small area of memory used to carry data within the CPU and prevent data bottlenecks.
- When an instruction is fetched from main memory, it is copied into the cache. This is because it might be needed later, and it's much quicker to fetch the instruction from cache than from main memory.
- As cache fills up, unused instructions or data still being held are replaced with more recent ones.
- This improves performance, as increasing cache size also increases the time instructions are held in cache.
- There are two types of cache:
  - **Level 1 Cache** is primary cache, which is faster but has less memory storage
  - **Level 2 Cache** is secondary cache, which is slower (still fairly fast) but has a larger memory storage

<br>

### Pipelining
- Without **pipelining**, the steps in the Fetch-Execute cycle take place in sequence. When the next instruction is being fetched, the execute part of the cycle is idle.
- With pipelining, the computer architecture allows the next instruction to be fetched whilst the previous one is being executed, and is then held in a buffer close to the processor until it can be executed.

<br>

## Words and word sizes

### Address bus
- Each **word** in memory has its own address. When the processor wants to read a word from memory, it puts the address of the word on the address bus.
- The width of the **address bus** determines the maximum number of bits that can pass along it. For example, an address bus consisting of 8 lines can only transmit a maximum address of 8 bits, making it an 8-bit address bus.

### Data bus
- The largest operand that can be held in a word relates to the size of the **data bus**.
- If the data bus is 8 bits wide, each word can only hold values up to 256, or 1 character. A wider data bus can transmit larger values or more characters at a time.




















