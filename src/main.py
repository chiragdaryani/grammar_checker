import os
import re
import csv
import argparse

import nltk
import pandas as pd

# Initialize the argument parser
parser = argparse.ArgumentParser()

# Add the parameters we will pass from cli
parser.add_argument('input_data_path',help='path to the input data file')
parser.add_argument('input_grammar_path',help='path to the input grammar file')
parser.add_argument('output_tsv_path',help='path to the output tsv file')

# Parse the arguments
args = parser.parse_args() 
#print(args)

# Path to input data file
input_data_path= args.input_data_path
# Path to input grammar file
input_grammar_path= args.input_grammar_path
# Path to output tsv file
output_tsv_path= args.output_tsv_path











''' 

Function to calculate precision and recall from the output file we created for our predictions

'''

def performance_metrics(output_tsv_path):
    output_tsv = pd.read_csv(output_tsv_path, delimiter="\t")
    
    TP= output_tsv[(output_tsv['ground_truth']==1) & (output_tsv['prediction']==1)].shape[0]
    FN= output_tsv[(output_tsv['ground_truth']==1) & (output_tsv['prediction']==0)].shape[0]
    FP= output_tsv[(output_tsv['ground_truth']==0) & (output_tsv['prediction']==1)].shape[0]
    TN= output_tsv[(output_tsv['ground_truth']==0) & (output_tsv['prediction']==0)].shape[0]


    print("===================")

    print('True positive = ', TP)
    print('False positive = ', FP)
    print('False negative = ', FN)
    print('True negative = ', TN)

    print("===================")

    Precision = TP / (TP + FP)
    print('Precision = ', Precision)

    Recall = TP / (TP + FN)
    print('Recall = ', Recall)

    print("===================")






















'''

Function to read all files, construct grammar object, parse all sentences and create final prediction results into output file

'''


def main():

    
    try: 


        # Read the grammar defined in toy.cfg file

        #grammar = nltk.CFG.fromstring()
        cfg_grammar = nltk.data.load(input_grammar_path)
        #print(cfg_grammar)
        
        # Create the parser from the loaded grammar
        parser= nltk.ChartParser(cfg_grammar)






        # Open the output file in which we will write final predictions

        with open(output_tsv_path, 'wt') as out_file:
            tsv_writer = csv.writer(out_file, delimiter='\t')
            # create headers for output file
            tsv_writer.writerow(['id', 'ground_truth','prediction'])
                            

            


            # Read input from "train.tsv" data file
            with open(input_data_path, 'r') as input_tsv_file:
                input_data_file = csv.reader(input_tsv_file, delimiter='\t')
                # skip the first line i.e headers (column names)
                next(input_data_file)
                


                # Go through each sentence one by one
                for row in input_data_file:


                            # Get the id of each sentence from 1st column
                            id = row[0]
                            #print(id)

                            # Get the true label of each sentence from 2nd column
                            truth_label = row[1]
                            #print(truth_label)




                            # the sentences we have to parse are stored in the 3rd column ( index no.2 ) of each row
                            sentence = row[2]
                            #print(sentence)

                            # Get the tokens from each sentence
                            #tokenized_sentence=sentence.split()
                            #print(tokenized_sentence)




                            # the POS tags are stored in the 4th column ( index no.3 ) of each row
                            sentence_pos_tags = row[3]

                            # Get the POS tag of each word in the sentence
                            tokenized_pos_tags=sentence_pos_tags.split()
                            #print(tokenized_pos_tags)



                            try:

                                # Parsing the POS Tag sequences with our grammar
                                trees= parser.parse_all(tokenized_pos_tags)
                                #print(trees)

                                #for tree in trees:
                                    #print(tree)
                                    #print("The sentence that was parsed successfully is:\n",sentence)

                                                            
                                # Atleast parse tree was returned, i.e. sentence was gramatically correct. Hence, give it a prediction of 0
                                if(len(trees)!=0):
                                    prediction = 0
                                    
                                # No parse tree retured, i.e. sentence was not gramatically correct. Hence, give it a predictiona of 1
                                if(len(trees)==0): 
                                    prediction = 1
                                



                            # will handle exceptions that came up while parsing the sentence
                            except Exception as e: 
                                print(e)
                                print("Something went wrong when parsing the sentence:\n",sentence,"\nWe are moving to the next file!")
                                print("=======================================================================")
                                
                                # since there was an exception while parsing, we will declare the string as not belonging to grammar (1)
                                prediction=1 
                                
                                # move to next row
                                continue



                            # will execute no matter exception occurred or not.
                            finally:
                                # Writing the id, truth, prediction to the output file!
                                tsv_writer.writerow([id, truth_label, prediction])




        # We have parsed all strings, predicted all labels and stored the values in the output tsv file. 
        # Now let's calculate precision and recall values using the below funtion.
        performance_metrics(output_tsv_path)
    
    except Exception as e:
        print("Something went wrong!\n The exception message is: ",e)




    
if __name__ == "__main__":
    main()