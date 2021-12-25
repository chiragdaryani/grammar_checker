# Intro to NLP - Assignment 2

In this assignment, our aim is using Context-Free Grammars (CFG) and constituency parsing to build a grammar checker for the English Language. We then evaluate the performance of our grammar checker on the dataset of sentences written by English learners with grammatical mistakes. We analyze the errors made by the grammar checker and report our findings.


## Team
|Student name| CCID |
|------------|------|
|Chirag Daryani   |  cdaryani    |
|Varshini Prakash   |  vprakash    |

## How to Execute?

To run this project,

1. Download the repository as a zip file.
2. Extract the zip to get the project folder.
3. Open Terminal in the directory you extracted the project folder to. 
4. Change directory to the project folder using:

    `cd f2021-asn2-chiragdaryani-main`
5. Install the required libraries, **NLTK** and **Pandas** using the following commands:

    `pip3 install nltk`

    `pip3 install pandas`
 
6. Now to execute the code, use the following command (in the current directory):

    `python3 src/main.py data/train.tsv grammars/toy.cfg output/train.tsv`
    
## Description of the execution command

Our program **src/main.py** that takes three positional command-line arguments in this order: the first is a path to the input data file, the second is a path to the grammar file, and the third is a path to the output TSV file.

For our assignment, the input dataset **train.tsv** which is a collection of english sentences is stored in the directory [data/train.tsv](data/train.tsv).
The grammar file **toy.cfg** we have created is stored in the grammars folder [grammars/toy.cfg](grammars/toy.cfg)
The final output is written in a file **train.tsv** inside the output folder [output/train.tsv](output/train.tsv)

So we'll specify these three paths and our final execution command becomes:

**python3 src/main.py data/train.tsv grammars/toy.cfg output/train.tsv**


## References


https://www.nltk.org/book/ch08.html

https://docs.huihoo.com/nltk/0.9.5/en/ch07.html

http://aritter.github.io/courses/5525_slides/cfg.pdf

https://newbedev.com/combining-a-tokenizer-into-a-grammar-and-parser-with-nltk

https://stackoverflow.com/questions/18984722/how-to-parse-the-special-character-in-context-free-grammar
