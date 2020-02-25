# Pyshell

Eli Saracino
esaracin@bu.edu
5/23/2017


Pyshell:

Pyshell uses a series of helper functions and packages to simulate a Linux-based shell environment, wherein a user can enter commands
with specific control characters that redirect input/output as necessary. Generally, these commands take the form of
executable program files and are run through the pyshell process using Python's subprocess library, which handles much of the work
in forking and loading program images into the new memory space.

In an effort to implement a realistic shell, I utilize the readline library functions, namely the titular readline() method,
which allow for autocompletion that feels very accurate to any given shell experience.

The shell supports many of the control characters that a given supported Bash shell might, albeit with some limitations:

        ';':    The semi-colon used to separate a sequence of commands has been implemented, and Pyshell can accept an arbitrarily
		long sequence in this manner. Any other controls characters are entirely viable for use in conjuction
                with the semi-colon

        '>':    The greater-than sign can be used to redirect the stdout of a given command to a given file name that is entered
                following the '>' symbol and a space character (i.e. cmd > output.txt)

        '<':    The less-than sign can be used to redirect the stdin of a given command to read from a given file whose name is
                entered following the '<' symbol and a space character (i.e. cmd < input.txt)

        '1>':   A 1 followed by a greater-than sign redirects the stdout of a given command to a given file name that is entered
                following the sequence and a space character (i.e. cmd 1> output.txt)

        '2>':   A 2 followed by a greater-than sign redirects the standard error of a given command to a given file whose name is
                entered following the sequence and a space character (i.e. cmd 2> output.txt)

        *'&>':  A '&' sign followed by a greater-than sign redirects the both the standard output and the standard error of a cmd
                to the specified file whose name is entered following the sequence and a space character (i.e. cmd &> output.txt)

        '|':    The vertical bar indicates that a given command should pipe its output as input to the next command in a sequence.
                This MUST be follwoed by at least one other command (i.e. cmd1 | cmd2 | cmd3), and can handle an arbitrary number 
		of consecutive pipes.


	*: Denotes that the specified control character has yet to be fully implemented into the current version of Pyshell.

	** Changing directories through the use of the 'cd' command is, similarly, yet to be implemented.

Pyshell expects Python 3, and currently, for ease of testing and use, includes a shebang line pointing to a common installation 
of Python 3, so as to be runnable from the command line by simply prepending its name with the usual './'. 

Going forward, the following features need to be implemented in order to cover the basics of a true shell environment:

	Simultaneous input/output redirection (within a single command)
	Support for non-trvial pipe commands (i.e. flag uses such as 'ls -a | cat') as well as compound commands that include similar flags.
	Support for graceful exit with EOF
	Support for directory movement through cd
