使用opencv中的haar+adaboost进行物体检测,文件目录如下,目录介绍：　　
.
├── config  
│   ├── config.py  
│   ├── config.pyc  
│   ├── __init__.py  
│   └── __init__.pyc  
├── data  
│   ├── image   
│   │   ├── neg-->负样本   
│   │   │   ├── neg_1.jpg   
│   │   │   ├── neg_2.jpg   
│   │   │   ├── neg_3.jpg  
│   │   │   ├── neg_4.jpg   
│   │   │   └── neg_5.jpg  
│   │   ├── neg.txt-->负样本文件目录   
│   │   ├── pos-->正样本   
│   │   │   ├── pos_1.jpg   
│   │   │   ├── pos_2.jpg   
│   │   │   ├── pos_3.jpg   
│   │   │   ├── pos_4.jpg   
│   │   │   └── pos_5.jpg   
│   │   └── pos.txt-->正样本文件目录   
│   └── model   
│       ├── cascade.xml   
│       ├── params.xml   
│       ├── stage0.xml   
│       ├── stage10.xml   
│       ├── stage11.xml   
│       ├── stage12.xml   
│       ├── stage13.xml   
│       ├── stage14.xml   
│       ├── stage15.xml   
│       ├── stage1.xml   
│       ├── stage2.xml   
│       ├── stage3.xml   
│       ├── stage4.xml   
│       ├── stage5.xml   
│       ├── stage6.xml   
│       ├── stage7.xml   
│       ├── stage8.xml   
│       └── stage9.xml    
├── detection   
│   ├── calc_regionratio.py   
│   ├── create_annotation.py    
│   ├── demo  
│   │   ├── detect_01300000115459120894838850378.jpg   
│   │   ├── detect_01300000180919124256698376723.jpg   
│   │   ├── detect_01300000314631128246170511243.jpg   
│   │   ├── detect_131.jpg   
│   │   ├── detect_19300001287046131622747012866.jpg   
│   │   ├── detect_20071014171857166_2.jpg   
│   │   ├── detect_20081016103122407_2.jpg    
│   │   ├── detect_2889686_134437546000_2.jpg   
│   │   ├── detect_5451374_173506368112_2.jpg   
│   │   ├── detect_5736135_094819032909_2.jpg   
│   │   ├── detect_7953837_193544583114_2.jpg    
│   │   └── detect_th.jpg   
│   ├── demoy.py   
│   ├── demoy.pyc   
│   ├── __init__.py  
│   ├── __init__.pyc   
│   ├── make_annotations.py   
│   ├── nms.py   
│   ├── nms.pyc   
│   ├── objdetect.py   
│   ├── producePostxt.py  　-->产生样本文件.  
│   ├── train_cascade.py  　-->训练  
│   └── vec   
│       └── pos.txt.vec   
└── ReadMe.md  

效果图：  
