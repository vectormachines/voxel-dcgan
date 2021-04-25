cd "/content/voxel-dcgan/binvox2mesh"
for f in /content/drive/MyDrive/colab/train-out/*.binvox
do
	python binvox2mesh.py "$f"
done