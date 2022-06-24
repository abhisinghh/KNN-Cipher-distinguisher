# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:21:57 2022

@author: hp
"""

import os
import time
import random
import string
import natsort
from binascii import hexlify as hexa, unhexlify as unhexa
import pandas as pd

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed

import multiprocessing
import threading


bin_numbers = ['00000000']
def generatePrintBinary(n):
 
    # Create an empty queue
    from queue import Queue
    q = Queue()
 
    # Enqueue the first binary number
    q.put("1")
    
 
    # This loop is like BFS of a tree with 1 as root
    # 0 as left child and 1 as right child and so on
    while(n > 0):
        n -= 1
        # Print the front of queue
        s1 = q.get()
        bin_numbers.append(s1.zfill(8))
 
        s2 = s1  # Store s1 before changing it
 
        # Append "0" to s1 and enqueue it
        q.put(s1+"0")
 
        # Append "1" to s2 and enqueue it. Note that s2
        # contains the previous front
        q.put(s2+"1")
 
n=255
generatePrintBinary(n)
#print(bin_numbers)

#function to split the stream of characters into given word length size here word_length =  1 byte = 8
word_length = 8

def split_to_byte(data) :
    split = [data[i:i+word_length] for i in range(0, len(data), word_length)]
    #print(len(split), split)
    return split


ecb_dir = "D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\\ecb\\"
folder_list = []
for folder in os.listdir(ecb_dir) :
    folder_list.append(ecb_dir +folder + '\\')
folder_list = natsort.natsorted(folder_list,reverse=False)
#print(folder_list)
#file_name = dir + "plain_text_file" + "1.txt" #str(counter)"" + ".txt"
#with open(file_name, encoding='ANSI') as fp:
#    file_data = fp.read()
#    data += file_data

#print(len(ecb_file_names_list))
ecb_file_names_list = []

for i in range(8) :
    file_names_list = []
    #test_counter = 0
    for file in os.listdir(folder_list[i]) :
        file_addr = folder_list[i] + file
        file_names_list.append(file_addr)
        #test_counter += 1
        #if test_counter == 8 :
        #   break
    file_names_list = natsort.natsorted(file_names_list,reverse=False)
    ecb_file_names_list.append(file_names_list)
ecb_file_names_list = natsort.natsorted(ecb_file_names_list,reverse=False)
#print((ecb_file_names_list[7][:8]))

#ecb_file_names_list = ecb_file_names_list[:10]

file_counter = 0
def generate_feature_vector(file): 
    
    global file_counter
    file_counter += 1
    global bin_numbers
    print('file {}, {}'.format(file_counter, file))
    
    data = ''
    with open(file) as fp:
        file_data = fp.read()
        data += file_data
    #print('length of characters in file  = {}'.format(len(data)))
    #print('data = {}'.format(data[:2]))
    data = unhexa(data)
    BLOCKLEN = 524288
    data = data[:BLOCKLEN]   
    binary_data_stream = ''
    
    char_pos = 0
    for i in data :
        bin_char = '{:08b}'.format((i))
        #if len(bin_char) > 8 :
            #print(char_pos)
            #print(bin_char)
        binary_data_stream += bin_char
        char_pos += 1
    print('binary data length = {}, data = {}'.format(len(binary_data_stream), binary_data_stream[:16]))
    
    #splited bytes stores all the splited chunks of the stream
    splited_bytes = split_to_byte(binary_data_stream)
    print('no of bytes in data {}'.format(len(splited_bytes)))
    
    #store the values in the extractions like first bit of each byte will go inside extraction_0 and so on till extraction_7
    #extracts stores the all the extractions in 8 lists
    
    extraction_1 = ''
    extraction_2 = ''
    extraction_3 = ''
    extraction_4 = ''
    extraction_5 = ''
    extraction_6 = ''
    extraction_7 = ''
    extraction_8 = ''

    for byte in splited_bytes :
        extraction_1 = extraction_1 + byte[0]
        extraction_2 = extraction_2 + byte[1]
        extraction_3 = extraction_3 + byte[2]
        extraction_4 = extraction_4 + byte[3]
        extraction_5 = extraction_5 + byte[4]
        extraction_6 = extraction_6 + byte[5]
        extraction_7 = extraction_7 + byte[6]
        extraction_8 = extraction_8 + byte[7]
    print(len(extraction_1), extraction_1[:16])
    
    
    dictionary_for_extraction_1 = {}
    dictionary_for_extraction_2 = {}
    dictionary_for_extraction_3 = {}
    dictionary_for_extraction_4 = {}
    dictionary_for_extraction_5 = {}
    dictionary_for_extraction_6 = {}
    dictionary_for_extraction_7 = {}
    dictionary_for_extraction_8 = {}
    
    for i in bin_numbers :
        if i not in dictionary_for_extraction_1.keys():
            dictionary_for_extraction_1[i] = 0
        if i not in dictionary_for_extraction_2.keys():
            dictionary_for_extraction_2[i] = 0
        if i not in dictionary_for_extraction_3.keys():
            dictionary_for_extraction_3[i] = 0
        if i not in dictionary_for_extraction_4.keys():
            dictionary_for_extraction_4[i] = 0
        if i not in dictionary_for_extraction_5.keys():
            dictionary_for_extraction_5[i] = 0  
        if i not in dictionary_for_extraction_6.keys():
            dictionary_for_extraction_6[i] = 0       
        if i not in dictionary_for_extraction_7.keys():
            dictionary_for_extraction_7[i] = 0         
        if i not in dictionary_for_extraction_8.keys():
            dictionary_for_extraction_8[i] = 0
            
    
    #print(len(list_of_dictionary_of_extracts))
    #adding frequency in the dictionary for each extract
    splited_extraction_1 = split_to_byte(extraction_1)
    splited_extraction_2 = split_to_byte(extraction_2)
    splited_extraction_3 = split_to_byte(extraction_3)
    splited_extraction_4 = split_to_byte(extraction_4)
    splited_extraction_5 = split_to_byte(extraction_5)
    splited_extraction_6 = split_to_byte(extraction_6)
    splited_extraction_7 = split_to_byte(extraction_7)
    splited_extraction_8 = split_to_byte(extraction_8)
    
    for byte in splited_extraction_1 :
        if byte in dictionary_for_extraction_1.keys() :
                dictionary_for_extraction_1[byte] += 1
       
    for byte in splited_extraction_2 :
        if byte in dictionary_for_extraction_2.keys() :
                dictionary_for_extraction_2[byte] += 1
     
    for byte in splited_extraction_3 :
        if byte in dictionary_for_extraction_3.keys() :
                dictionary_for_extraction_3[byte] += 1
     
    for byte in splited_extraction_4 :
        if byte in dictionary_for_extraction_4.keys() :
                dictionary_for_extraction_4[byte] += 1
     
    for byte in splited_extraction_5 :
        if byte in dictionary_for_extraction_5.keys() :
                dictionary_for_extraction_5[byte] += 1
     
    for byte in splited_extraction_6 :
        if byte in dictionary_for_extraction_6.keys() :
                dictionary_for_extraction_6[byte] += 1
     
    for byte in splited_extraction_7 :
        if byte in dictionary_for_extraction_7.keys() :
                dictionary_for_extraction_7[byte] += 1
     
    for byte in splited_extraction_8 :
        if byte in dictionary_for_extraction_8.keys() :
                dictionary_for_extraction_8[byte] += 1
 
    #for i in range(8) :
        #print("printing dictionary values for extraction {}".format(i))
        #print(list_of_dictionary_of_extracts[i])
        #print(sum(list_of_dictionary_of_extracts[i].values()))
    
    list_of_dict_values_of_all_extracts = []
    
    dict_value_1 = dictionary_for_extraction_1.values()
    for value in dict_value_1 :
        list_of_dict_values_of_all_extracts.append(value)
                
    dict_value_2 = dictionary_for_extraction_2.values()
    for value in dict_value_2 :
        list_of_dict_values_of_all_extracts.append(value)
    
    dict_value_3 = dictionary_for_extraction_3.values()
    for value in dict_value_3 :
        list_of_dict_values_of_all_extracts.append(value)
    
    dict_value_4 = dictionary_for_extraction_4.values()
    for value in dict_value_4 :
        list_of_dict_values_of_all_extracts.append(value)
    
    dict_value_5 = dictionary_for_extraction_5.values()
    for value in dict_value_5 :
        list_of_dict_values_of_all_extracts.append(value)
    
    dict_value_6 = dictionary_for_extraction_6.values()
    for value in dict_value_6 :
        list_of_dict_values_of_all_extracts.append(value)
    
    dict_value_7 = dictionary_for_extraction_7.values()
    for value in dict_value_7 :
        list_of_dict_values_of_all_extracts.append(value)
    
    dict_value_8 = dictionary_for_extraction_8.values()
    for value in dict_value_8 :
        list_of_dict_values_of_all_extracts.append(value)
    


    return list_of_dict_values_of_all_extracts


entire_ecb_feature_vector = []

def start_feature_generation(ecb_file_names_list) :
    global algo_counter 
    algo_counter += 1
    ecb_feature_vector = []
    
    #with ThreadPoolExecutor(max_workers=16) as exe:
        #print('inside thread')
        #feature_vector = exe.map(generate_feature_vector,ecb_file_names_list)
        #ecb_feature_vector.append(feature_vector)
    with ProcessPoolExecutor(max_workers=8) as exe:
       feature_vector = exe.map(generate_feature_vector,ecb_file_names_list)
    #for file in ecb_file_names_list :
        #feature_vector = generate_feature_vector(file)
        #print(len(feature_vector))
        #ecb_feature_vector.append(feature_vector) 
    df = pd.DataFrame(feature_vector)
    print(df.shape)
    #out_dir = ''
    df.to_csv('feature_vector_algo_' + str(algo_counter) + '.csv')    


entire_ecb_feature_vector = []

if __name__ == '__main__':
    
    st = time.time()
    algo_counter = 0
    processes = []
    #with ProcessPoolExecutor(max_workers=8) as exe:
       #exe.map(start_feature_generation,ecb_file_names_list)
        
    for i in range(8) :
        start_feature_generation(ecb_file_names_list[i])
        #p = multiprocessing.Process(target = start_feature_generation, args=(ecb_file_names_list[i],))
        #p.start()
        #processes.append(p)
    #for p in processes :
        #p.join()
        #entire_ecb_feature_vector.append(result)
    et = time.time()
    print('Execution time: ', (et - st), ' seconds') 
    
    new_ecb_file_names_list = []
    for list in ecb_file_names_list :
      new_file_list = [x.replace('D:\\Abhimanyu Singh\\2 knn experiement\\ciphertext_data\\ecb\\', '').replace('.txt', '') for x in list]
      new_ecb_file_names_list.append(new_file_list)

    #print(len(new_ecb_file_names_list))
    
    
    #threads = []
    #for i in range(8) :
    #    file_names_list = ecb_file_names_list[i]
    #    t = threading.Thread(target = start_feature_generation, args = (file_names_list,))
    #    t.start()
    #    threads.append(t)
    #
    #entire_ecb_feature_vector = [t.join() for t in threads]threads = []
