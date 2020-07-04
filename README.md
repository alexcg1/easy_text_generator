# Machine Learning for Mortals

![](./mortals.webm)

## What is it?

An app that runs in your web browser and uses a nice GUI interface to generate text from pre-trained machine learning models like GPT-2. It doesn't support training models at the moment.

## Can I See an Example?

### General text (GPT-2)

Starting text: `It is a truth universally acknowledged`

```
It is a truth universally acknowledged that any single person's life will change
when he or she becomes a parent, even if he or she becomes a parent on his or
her own. To put it bluntly, that person's life will change for the better if he
or she gets a baby and the child is adopted.  When I talk to children in
orphanages or on the streets that all I hear is talk of wanting to adopt and
growing up being a "good baby" or that children are not in trouble when they
don't get adopted because "the community would always give them a chance." I
don't want to hear that when they ask, "What did you know or don't know about
adoption?" 
```

### Star Trek scripts

Starting text: `One to beam up Mr Scott`

```
[Transporter room]

SCOTT: Mister Data. 
DATA: We are still at three million kilometres. 
SCOTT: Mister Data, you won't have much time. Beam away. 
DATA: We will be gone in two minutes. 
SCOTT: Mister Data, you just won't do it. You have to get back into
here, Mister Data. 
DATA: Sir, I wish to
```

## How Do I Use it?

### Precaution

Machine learning needs a LOT of RAM. I highly recommend 16gb or more, or enabling a swap partition if you're on Linux. Otherwise your machine may just lock up during install or running the program (it happened to me plenty).

### Install

```bash
git clone git@github.com:alexcg1/machine_learning_mortals.git
cd machine_learning_mortals
pip install -r requirements.txt
```

### Run

In the same directory as above

```bash
streamlit app.py
```

It opens a tab in your web browser where you can choose the model you want and generate text.

### Thanks to:

* [Script Buddy v2](https://github.com/cdpierse/script_buddy_v2) - code adapted from here
* [Huggingface](https://huggingface.co/models) - a huge list of models for working with text
