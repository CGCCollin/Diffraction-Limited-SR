# Super-Resolution-Diffraction-Limited-Images
ESRGAN inspired super-resolution model for reconstruction of diffraction limited images.
<a href="https://figshare.com/articles/dataset/DL-SMLM_a_biological_imaging_dataset_containing_paired_widefield_and_SMLM_super-resolution_images/26879218/1">Dataset</a>
To use:</br>
Use python atleast 3.12</br>
Run python -m venv ./venv</br>
./venv/activate.ps1 ./venv/activate.bash</br>
run python -m pip install requirements.txt</br>
run python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126</br>
</br>
Ensure you have a copy of the extracted dataset.</br>
Extract each inteneral folder, and place it into ./dset</br>
Run code as desired (running data-prep first.)</br>
Enjoy!</br>
Note you need to run data_prep first, (adjusting paths as needed)</br>
then run the model script.</br>