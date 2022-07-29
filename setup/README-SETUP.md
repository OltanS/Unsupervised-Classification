STEPS:

1. Download anaconda
2. open anaconda prompt
3. cd to the setup folder (i.e. the folder this readme is in)
4. run the create-env.cmd (just type its name in and press enter)
5. run setup-env.cmd
   If this doesn't work, it means your cuda version is (probably) too low. run nvidia-smi on your command prompt, check your cuda version and set an appropriate cuda version. Look [here](https://pytorch.org/get-started/locally/) for which version to use
6. run set-gpu.py, it will instruct you on how to proceed
7. Setup is now done. Refer to HOW-TO-USE.md for further instructions.
