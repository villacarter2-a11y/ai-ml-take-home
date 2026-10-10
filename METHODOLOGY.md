# Methodology

## 1. How to run it

### Enviroments Used:
Python Version: 3.12
Tested OS: Windows 11

```bash
# clone the repository and install dependencies
git clone https://github.com/villacarter2-a1ly/ai-ml-take-home.git
cd ai-ml-take-home
pip install -r requirements.txt

```
# Training and Creating Your Own Model:
This is for those who want to create their own model instead of using the model already created, tested, and evaluated.
 Note that in database.ipynb the model is already downloaded using an API key in a variable. A user can get their own key by going to the model data website at Roboflow: https://universe.roboflow.com/malletbottle2/sampled-yd-object-detection

Go to train.py and edit the model settings you wish to change

# Using an already complete and optimized model:

.In train.py you can run the code and view the output of model performance on the validation set downloaded
```bash
python train.py
```

.In inference.py you can run the code and view the output of model metrics for specific images by running
``` bash
python inference.py Sampled-YD-Object-Detection-2/valid/images output_txts
```

Where inference.py is the name of the python program, Sampled-YD-Object-Detection-2/valid/images is the path to the set of images with objects to be detected, and output_txts is a folder containing the text files containing object class, box boundaries, and classification confidence








## 2. Thought process

*Initial model performance with baseline settings of epoch = 40, imgsz = 640 performed extremely well (mAP50: .939), however performance for the bottle classification and detection was noticeably worse than the mallet (when comparing mAP50 mallet: .983 vs bottle: .895). Model split

*This is likely due to the mallet's unique shape and high contrast compared to the background whereas bottles have a more common shape and are more see through ultimately making it harder for the model to recognize the bottles

*Taking into consideration possible unclear environments such as deserts, bad angles, and poorly positioned bottles/mallets I decided to test data augmentation for specific hyperparameters that would likely help create a model recognize the objects despite poor enviroments. Ex: erasing, hsv_h, hsv_v, hsv_s, and mosaic which all would be useful in helping identify partially covered, blended in or even small objects.

*My first iteration was testing the saturation and hue of the images to create a model that  Keeping the baseline epoch of 40 and imgsze of 640 I tested different values for hsv_h and hsv_s first.

*Different values for the hyperparameters hsv_h and hsv_s alter image hue and saturation respectively. By altering image and brightness the model would be able to ignore repeatable characteristics like specific color of training data and focus more on the physical chararcteristics and measurements of an object that would be more transferable to identifying the objects in different environments.

*After testing both the upper and lower bounds of hsv_s where the default was .7, I tested values of .3, .5 which ultimately reduced mAP50 scores from the baseline .939 to .928 and .93 respectively (without resulting in any considerable benefit in another evaluation metric).

*After testing a lower bound value of hsv_h at .010 the model performed at an mAP50 of .935. Although, worse than the peak baseline model, the model showed better performance in mAP50-95 and Box(P) by a considerable amount (.625 vs .613 and .954 vs .931 respectively). Not only this, it's performance across each object in these specific areas was higher than its baseline counterpart. Meaning it was not just purely improving one objects scores like the mallet over the bottle.

*Throughout the process of building and evaluating models, I realized that even after testing multiple combinations of many different hyperparameters such as mosaic, hsv_v, hsv_s, erasing, and imgsz the baseline model retained the highest overall mAP50 score. This is likely due to the dataset already implementing similar features in a balanced variety of different angles, rotations, and clutteredness.




*To conclude, the model chosen features the hyperparameters epoch = 40, imgsz = 640, hsv_h = .010



## 3. Known limitations

*Important note: Since at the beginning the models choose randomized weights, the baseline model I refer to was the one that recorded the best overall mAP50 scores (alongside all other metrics as well). The same goes for the model chosen for my end to end machine learning pipeline. It is important to note that other variations of the models outperformed each other and may possess averages that do not reflect the outcome shown.

*While the model chosen over the baseline has higher scores in mAP50-95 signifying the model having higher overall confidence in the IoU (overlap of possible boxes) and in Box(P, the model performed worse by an overall .043 in the r score.

*Given that recall is very important in assuring that the rover does not skip over any objects, a very compelling argument can be made that having a higher recall ability is more important than the overall accuracy in creating boxes for objects.

* It is also to be noted that both the baseline and the updated model both underperform when it comes to detecting and classifying bottle objects compared to mallets.

Finally, if I were to make any adjustments to the model, I would spend more time working on preprocessing the data into more standardized and groupable properties ensuring that each characteristic and geometric property is trained and tested on. I would also spend time analyzing specific test cases for the bottles in order to hopefully find a pattern or underlying property that makes the model underperform and then tweak my model or data to help combat this.

### Model's Mistakes (false postives/negatives)
* Key errors observed when looking at my model's mistakes include the model detecting two objects either mallet and/or bottle on zoomedin phtos where a mallet covers most of the screen at an akward rotated angle/blur. The model likely struggles with unclear/rotated bigger images because it can be easier for the shape of the object to be unclear. Additionally, some false positives include deetcting unpresent mallets in cluttered areas like sandpits. This is likely due to darker spots in sand and cluttered photos appearing to share some similar features like shape/color to bottles at similar distances.

* Ideas to mitigate problems in the future: since the model seems to do well with medium to small-medium sizes but struggles with larger/stock images at rotated angles/blurs, it may be useful to scale down the photos to allow the shape to be better understood/learned.