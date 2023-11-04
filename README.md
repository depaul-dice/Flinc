# Prerequisites
* Python 3.x with headers and compiler
* pip >= 20.x
* glibc>=2.17

# Reproducible Notebook Containers using Application Virtualization

To install and use FLINC in your Jupyter environment, follow the steps 
below.

1. After extracting the flinc directory, `cd` into it.
2. Find the path of the kernel you wish to audit using this command:

   `jupyter kernelspec list`
   
3. Execute install.sh from the command line:
   
   `./install.sh <user kernel path>`
   
   `<user kernel path>` is the path of the kernel that will execute your notebook code.

4. The successful execution of the above script will result in the 
installation of sciunit, audit kernel, and repeat kernel.
   You may confirm the kernel installations by running:
   
   `jupyter kernelspec list`

   
6. Select the audit kernel from within the notebook and execute your notebook 
code. After execution completes, select 'No Kernel' from the list or shutdown the kernel and wait 30 
seconds to 1 minute to complete.
7. Repeat your notebook code on the same or different machine by selecting 
the repeat kernel.
8. After using the repeat kernel, select No Kernel again to finish.
9. Sciunit will store your notebook as an executable which you can 
view using:

   `sciunit list`

**NOTES**
1. The install.sh script must only be executed once.
   Once the audit and repeat kernels have been installed, the script 
should not be run again.
2. No existing file should be deleted or modified in the flinc directory.
3. After testing one notebook with the audit and repeat kernels successfully, 
   shut down the server and start it again before running another notebook with the audit kernel.
4. If you run your code using the audit kernel on machine #1, you can repeat it using the repeat kernel on machine #2. To do this, first execute your code using audit kernel, and then run 'sciunit copy' to obtain a unique code. Take that code and run `sciunit open <code>`. This transfers the contents of the notebook container to machine #2 from machine #1.
