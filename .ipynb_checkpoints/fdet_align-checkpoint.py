{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "FileExistsError",
     "evalue": "[WinError 183] 既に存在するファイルを作成することはできません。: 'C:\\\\Users\\\\2020A00140\\\\AppData\\\\Roaming\\\\jupyter\\\\runtime\\\\kernel-656a0e9e-6a51-4ce7-ae95-1e0a784d3fb9.json'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileExistsError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-1635b799da91>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     13\u001b[0m \u001b[0moutdir\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mPath\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msys\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0margv\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     14\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 15\u001b[1;33m \u001b[0moutdir\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmkdir\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mparents\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexist_ok\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     16\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     17\u001b[0m \u001b[0mimages\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\pathlib.py\u001b[0m in \u001b[0;36mmkdir\u001b[1;34m(self, mode, parents, exist_ok)\u001b[0m\n\u001b[0;32m   1282\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_raise_closed\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1283\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1284\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_accessor\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmkdir\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmode\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1285\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mFileNotFoundError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1286\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mparents\u001b[0m \u001b[1;32mor\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mparent\u001b[0m \u001b[1;33m==\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mFileExistsError\u001b[0m: [WinError 183] 既に存在するファイルを作成することはできません。: 'C:\\\\Users\\\\2020A00140\\\\AppData\\\\Roaming\\\\jupyter\\\\runtime\\\\kernel-656a0e9e-6a51-4ce7-ae95-1e0a784d3fb9.json'"
     ]
    }
   ],
   "source": [
    "# sysはPythonのインタプリタや実行環境に関する情報を扱うためのライブラリです。\n",
    "# 使用しているプラットフォームを調べる時や、\n",
    "# スクリプトの起動パラメータを取得する場合などに利用します。\n",
    "import sys\n",
    "import cv2\n",
    "import dlib\n",
    "from pathlib import Path\n",
    "import imutils\n",
    "from imutils.face_utils import FaceAligner\n",
    "from imutils.face_utils import rect_to_bb\n",
    "\n",
    "indir = Path(sys.argv[1])\n",
    "outdir = Path(sys.argv[2])\n",
    "\n",
    "outdir.mkdir(parents=True, exist_ok=True)\n",
    "\n",
    "images = []\n",
    "for img_name in indir.glob(\"*\"):\n",
    "    if img_name.suffix not in [\".jpg\", \".png\", \".bmp\" ,\".jpeg\"]:\n",
    "        continue\n",
    "    images.append(img_name)\n",
    "\n",
    "face_predictor = \"shape_predictor_68_face_landmarks.dat\"\n",
    "\n",
    "detector = dlib.get_frontal_face_detector()\n",
    "predictor = dlib.shape_predictor(face_predictor)\n",
    "fa = FaceAligner(predictor, desiredFaceWidth=256)\n",
    "\n",
    "print(images)\n",
    "for img_name in images:\n",
    "    print(img_name)\n",
    "    outfile = outdir / (\"%s.jpg\" % img_name.stem)\n",
    "    img = cv2.imread(str(img_name))\n",
    "\n",
    "    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\n",
    "    faces = detector(img_gray, 2)\n",
    "\n",
    "    if len(faces)==0:\n",
    "        print(\"==0\",img_name)\n",
    "        continue\n",
    "    if len(faces)>1:\n",
    "        print(\">1\",img_name)\n",
    "        continue\n",
    "\n",
    "    (x, y, w, h) = rect_to_bb(faces[0])\n",
    "    if w == 0 or h == 0:\n",
    "        continue\n",
    "\n",
    "    x = max(0, x)\n",
    "    y = max(0, y)\n",
    "    w = min(img_gray.shape[1], x + w) - x\n",
    "    h = min(img_gray.shape[0], y + h) - y\n",
    "\n",
    "\n",
    "    faceOrig = imutils.resize(img[y:y+h, x:x+w], width=256)\n",
    "    faceAligned = fa.align(img, img_gray, faces[0])\n",
    "\n",
    "    cv2.imwrite(str(outfile), faceAligned)\n",
    "    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
