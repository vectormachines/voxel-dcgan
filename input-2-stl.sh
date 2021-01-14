cd "/content/voxel-dcgan/binvox2mesh"
for f in /content/drive/MyDrive/v2/ubuntu-gtx1080/stars156-binvox/*.binvox
do
	python binvox2mesh.py "$f"
done