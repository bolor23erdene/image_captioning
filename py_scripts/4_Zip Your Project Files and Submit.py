#!/usr/bin/env python
# coding: utf-8

# ## Project Submission
# 
# When you are ready to submit your project, meaning you have checked the [rubric](https://review.udacity.com/#!/rubrics/1427/view) and made sure that you have completed all tasks and answered all questions. Then you are ready to compress your files and submit your solution!
# 
# The following steps assume:
# 1. All cells have been *run* in Notebooks 2 and 3 (and that progress has been saved).
# 2. All questions in those notebooks have been answered.
# 3. Your architecture in `model.py` is your best tested architecture.
# 
# Please make sure all your work is saved before moving on. You do not need to change any code in these cells; this code is to help you submit your project, only.
# 
# ---
# 
# The first thing we'll do, is convert your notebooks into `.html` files; these files will save the output of each cell and any code/text that you have modified and saved in those notebooks. Note that the first notebooks are not included because their contents will not affect your project review.

# In[ ]:


get_ipython().system('jupyter nbconvert "2_Training.ipynb"')
get_ipython().system('jupyter nbconvert "3_Inference.ipynb"')


# ### Zip the project files
# 
# Next, we'll zip all these notebook files and your `model.py` file into one compressed archive named `project2.zip`.
# 
# After completing this step you should see this zip file appear in your home directory, where you can download it as seen in the image below, by selecting it from the list and clicking **Download**. This step may take a minute or two to complete.
# 
# <img src='images/download_ex.png' width=50% height=50%/>
# 

# In[ ]:


get_ipython().getoutput('apt-get -y update && apt-get install -y zip')
get_ipython().system('zip project2.zip -r . -i@filelist.txt')


# ### Submit Your Project
# 
# After creating and downloading your zip file, click on the `Submit` button and follow the instructions for submitting your `project2.zip` file. Congratulations on completing this project and I hope you enjoyed it!

# In[ ]:




