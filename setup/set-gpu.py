import os
import sys

if len(sys.argv) != 2:
    print("go to your task manager -> performance and look at the index next to your dedicated gpu\n" +
    "assuming you have a shitty intel gpu too bc you're using a laptop\n" +
    "for me dedicated gpu was indexed 1")

    print("then run the program like: python set-gpu.py 1")
    quit(1)

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
print("Set CUDA_DEVICE_ORDER to PCI_BUS_ID")
os.environ["CUDA_VISIBLE_DEVICES"] = str(sys.argv[1]) #set number here to your dedicated GPU
print(f"Set CUDA_VISIBLE_DEVICES to {str(sys.argv[1])}")
quit()