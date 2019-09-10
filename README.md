# Generate Text Summmary
### How to run the project

- Install the required packages using the command ```$ pip install -r requirements.txt ```.
- Run ```$ python3 main.py```
###Rationale behind my approach
TTo keep it simple, I have used an unsupervised learning approach to find the sentences similarity and rank them. One benefit of this will be, we don’t need to train and build a model prior start using it for your project.
Since we will be representing our sentences as the bunch of vectors, we can use it to find the similarity among sentences. It measures cosine of the angle between vectors. Angle will be 0 if sentences are similar.
Next, Below is our code flow to generate summarize text:-
Input article → split into sentences → remove stop words → build a similarity matrix → generate rank based on matrix → pick top N sentences for summary.
