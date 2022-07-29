echo y|conda create -n "testing" python=3.7.7 ipython
conda activate testing
echo y|conda install pytorch torchvision cudatoolkit=11.3 -c pytorch
echo y|conda install faiss-gpu -c pytorch
echo y|conda install matplotlib scipy scikit-learn
echo y|conda install pyyaml easydict
echo y|conda install termcolor