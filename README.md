# decaptcha-classification

This repository is part of a submission for an assignment, which was part of the course Introduction to Machine Learning (CS771A), Fall Semester, 2022, IIT Kanpur. 

## Problem Statment
Each CAPTCHA image in this assignment will be 500 × 150 pixels in size. Each image will contain a code composed of **3 upper case Greek characters** (i.e. no numerals, punctuation
marks or lowercase characters). The font of all these characters would be the same, as would be the font size. However, each character may be rotated (degree of rotation will always
be either 0◦,±10◦,±20◦,±30◦ and each character may be rendered with a different color. The background color of each image can also change. However, all background colors are light in
shade. Each image also has some stray lines in the background which are of varying thickness, varying color and of a shade darker than that of the background. These stray lines are intended to make the CAPTCHAs more “interesting” and realistic.

We have been provided with 2000 training images (see the subdirectory train) in the assignment package. The true codes present in each image are collected in the file labels.txt. In
addition to this we have also been given reference images (see the subdirectory reference in the assignment archive) for all 24 characters in a standardized form with a white background. This is to simply give a handy reference on what unrotated images of characters look like if all color information is removed.

Our task is to design an algorithm that can take a set of such 500 × 150 images and return the code present in that image.

## Approach

The approach has been detailed in the report present in the repository.
