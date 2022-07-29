This assumes you finished README-SETUP.md and have the relevant environment active

**IMPORTANT**
To configure the hyperparameters, change the relevant yaml files in configs/pretext or configs/scan or configs/selflabel (respectively, for all three different phases of running this)

1. change the path at utils/mypath.py to your path for the datasets(not sure if you need the folders already so be safe probs there, defo don't need to have already installed the dataset it does it for you) e.g.
   > C:/Users/oltan/Documents/Projects/Unsupervised-Classification/datasets/cifar-10
2. set output directory at configs/env.yml in format shown above
3. cd to the root of the repository
4. Go to the relevant yaml file in the configs/pretext directory and either reduce the batch_size or the num_workers(not sure about this parameter but should work I think) parameters to a point where the following command does not give you a cuda out of memory error at one point.
5. Run the following command, except for the file in the end choose the relevant yaml for the dataset. (FOR PRETEXT)

   > python simclr.py --config_env configs/env.yml --config_exp configs/pretext/simclr_cifar10.yml

6. If you don't want to run pretext they already did it for a few datasets, I'll copy what they said about using what they did (I tested it, it works):  
   In order to save time, we provide pretrained models in the README.md for all the datasets discussed in the paper.
   First, download the pretrained model [here](https://drive.google.com/file/d/1261NDFfXuKR2Dh4RWHYYhcicdcPag9NZ/view?usp=sharing) and save it in your experiments directory. Then, move the downloaded model to the correct location (i.e. `repository_eccv/stl-10/pretext/`) and calculate the nearest neighbors. This can be achieved by running the following commands:

```bash
mv simclr_stl-10.pth.tar repository_eccv/stl-10/pretext/checkpoint.pth.tar  # Move model to correct location
python tutorial_nn.py --config_env configs/env.yml --config_exp configs/pretext/simclr_stl10.yml    # Compute neighbors
```

You should get the following results:

```
> Restart from checkpoint repository_eccv/stl-10/pretext/checkpoint.pth.tar
> Fill memory bank for mining the nearest neighbors (train) ...
> Fill Memory Bank [0/10]
> Mine the nearest neighbors (Top-20)
> Accuracy of top-20 nearest neighbors on train set is 72.81
> Fill memory bank for mining the nearest neighbors (val) ...
> Fill Memory Bank [0/16]
> Mine the nearest neighbors (Top-5)
> Accuracy of top-5 nearest neighbors on val set is 79.85
```

Now, the model has been correctly saved for the clustering step and the nearest neighbors were computed automatically.

7. Run semantic clustering like this: (except change the dataset name and config file ofc)
   > python scan.py --config_env configs/env.yml --config_exp configs/scan/scan_stl10.yml

You can see the relevant logs in the logs directory

8. Visualize the clustering with: (except change the dataset name and config file ofc)

   > python eval.py --config_exp configs/scan/scan_stl10.yml --model repository_eccv/stl-10/scan/model.pth.tar --visualize_prototypes

9. Good job, you used the model!
