#!/usr/bin/env python
import subprocess
import os
import sys
import signal
from io import StringIO
import readline

def parseCmd(cmd):
    '''Parses the input command into its composite components. 
    If there exists a sequence of commands, we first separate those 
    commands into separate lists within a larger 2D list. In either case,
    the 2D list consisting of those commands requested is returned.'''
   
    seq = False
    if ';' in cmd: # we have at least 2 commands (i.e. a command sequence)
        components = cmd.split(';')
        seq = True
    else:
        components = cmd.split()


    # Regardless of the number of commands specified,
    # we capture each as a list within a larger
    # list, to make calling them later easier.

    if seq:
        for ind in range(len(components)):
            components[ind] = components[ind].split()
    else:
        components = [components]
   

    return components

def sigint_handler(signal, frame):
    sys.exit(0)

def count_controls(cmd):
    
    chars = ['>', '<', '1>', '2>', ]
    
    count = 0
    for i in cmd:
        if i in chars:
            count += 1

    return count

def run_pipes(cmd):
    '''Takes in a list of a commands split by thier composite
    pipes, and runs that command, piping output as necessary.'''

    num_commands = len(cmd)
    for i in range(num_commands - 1):
        first = cmd[i]
        second = cmd[i + 1]

def runCmd(cmd):
    '''Given a cmd specified as a reference to a list containing
    a command and its composite arguments, Runs the given command. 
    Redirects standard in/output as necessary.'''
    
    # Split on pipe characters
    # cmd = cmd.split('|')

    # Add support for compound commands:
    # ['cat', '>', 'out.txt', '<', 'test.txt'] 

    # Add support for piped commands:
    # ['ls', '|', 'echo']

    # Add support for changing directories
    
    # Remove user error by accounting for trailing spaces
    for i in range(len(cmd)):
        cmd[i] = cmd[i].strip() # rid ourselves of any trailing spaces


    if('|' in cmd):
        # Recombine our command, so that we can properly split it on any 
        # pipes that may exist. If there are pipes, we call a 
        # separate function to handle them.
        
        cmd = ' '.join(cmd).split('|')
        print(cmd)
        sys.exit(0)
        run_pipes(cmd)
        return
    
    control_chars = []
    for ind in range(len(cmd)):
        # Handle len(1) command characters
        if len(cmd[ind]) == 1:
            if cmd[ind] == '>':
                control_chars.append(('>', ind))
                continue
            if cmd[ind] == '<':
                control_chars.append(('<', ind))
                continue
        elif len(cmd[ind]) == 2:
            if cmd[ind] == '2>':
                control_chars.append(('2', ind))
                continue
            if cmd[ind] == '1>':
                control_chars.append(('1', ind))
                continue


    # Use the information gathered through last 
    # iteration through the command to redirect
    # in/output as necessary.
    for char, position in control_chars:
        first_args = cmd[:position] 
        after_arg = cmd[position + 1]

        if(char == '>' or char == '1'): 
            outfile = open(after_arg, 'w')
            process = subprocess.run(first_args, stdout=outfile)
            outfile.close()
            return
        elif(char == '<'):
            infile = open(after_arg)
            process = subprocess.run(first_args, stdin=infile)
            infile.close()
            return
        elif(char == '2'):
            outfile = open(after_arg, 'w')
            process = subprocess.run(first_args, stdout=outfile, stderr=outfile)
            outfile.close()
            return
    
    

    process = subprocess.run(cmd, check=True)

def main():
    '''The meat of our Shell. Where user input will be received and parsed.'''
    # Let tab be used to autocomplete filenames 
    readline.parse_and_bind("tab: complete")
    
    while(True):
        # Read in and parse user's cmd
        cmd = input('>>> ')
        if cmd == '':
            sys.exit(0)
        else:
            cmdList = parseCmd(cmd)
        
            # Run the command and capture return signal
            for cmd in range(len(cmdList)):
                try:
                    runCmd(cmdList[cmd])
                except Exception as x:
                    print('\'' + str(cmdList[cmd]) + '\'', 'returned exception:', x)



if __name__ == '__main__':
    main()
