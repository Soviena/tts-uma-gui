# Uma Musume TTS Gen - GUI
A Gui frontend from project [](https://github.com/ReturnToFirst/uma-tts-vits)

1. Prepare the folder
```
git clone https://github.com/jaywalnut310/vits
cd vits/monotonic_align && python setup.py build_ext --inplace
pip install Cython librosa matplotlib numpy scipy Unidecode pyopenjtalk jaconv
wget https://github.com/ReturnToFirst/uma-tts-vits/releases/download/v1.0.0/G_790000.pth
mv G_790000.pth vits/
```

2. Install requirement
```
pip install -r requirements.txt
```

3. Run replace_cleaner.py
```
python replace_cleaner.py
```

4. Copy front.py, frontend.py, out.py to vits
```
cp front.py vits/
cp frontend.py vits/
cp out.py/
```

5. Run frontend.py to open the program
```
python frontend.py
```