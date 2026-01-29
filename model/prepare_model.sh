git clone https://github.com/ultralytics/ultralytics.git
git checkout v8.3.224
patch ultralytics/ultralytics/utils/loss.py loss.py.patch
cp data.yaml ultralytics/
