import time
import random
import sys
from quicksort_last_pivot import quick_sort_by_count_last_pivot
from quicksort_median_of_three_pivot import qsort_by_count_mo3
from word_counter_binary_search import word_counter_bin
from unique_words_in_list import find_unique_words_in_list1

def load_file(file_name):
   f = open(file_name).read().split()
   return f

# Get the time units given by the perf_counter
# Note: time.clock has been deprecated in Python 3.3
# and replaced with the more precise perf_counter method

# define time.get_time to be the appropriate time counter
if sys.version_info < (3, 3):
   get_time = time.clock
   print("Using time.clock for timing - Python ver < 3.3")
else:
   get_time = time.perf_counter
   print("Using time.perf_counter for timing - Python ver >= 3.3")
   REZ = time.get_clock_info('perf_counter').resolution
   print('Smallest unit of time is ' + str(REZ) + ' seconds')


#list_of_sizes = list(range(40, 800, 40))
n_trials = 10
total_time = 0
#test_list = ['picture','yourself','in','a','boat','on','a','river','with','tangeringe','trees','and','marmalade','skies','somebody','calls','you','you','answer','quite','slowly','a','girl','with',
             #'kaleidoscope','eyes','cellophane','flowers','of','yellow','and','green','towering','over','your','head','look','for','the','girl','with','the','sun','in','her','eyes','and','shes','gone','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','ah','follow','her','down','to','a','bridge','by','a','fountain'
             #'where','rocking','horse','people','eat','marshmallow','pies','everyone','smiles','as','you','drift','pass','the','flowers','that','grow','so','incredibly','high','newspapwer','taxis','appear','on','the','shore','waiting','to','take','you','away','climb','in','the','back','with','your','head','in','the','clouds','and',"you're",'gone','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','ah','picture','yourself','on','a','train','in','a','station','with','plasticine','porters','with','looking','glass','ties','suddenly','someone','is','there','at','the','turnstile','the','girl','with','kaleidoscope','eyes','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','ah','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','ah','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds','lucy','in','the','sky','with','diamonds',]
for i in range(n_trials):
   #crash_test_dummy, comparisons = word_counter_bin(test_list)
   cactus , comparisons = word_counter_bin(load_file('war_and_peace.txt'))
   #doggie , comparisons = word_counter_bin(load_file('text_alice.txt'))
   start = get_time()
   quick_sort_by_count_last_pivot(cactus)
   #qsort_by_count_mo3(cactus)


   end = get_time()
   time_taken = end - start
   total_time += time_taken

#print(find_unique_words_in_list1(cactus, doggie))
#counter = 0
#while counter < len(find_unique_words_in_list1(cactus, doggie)):
   #counter+=1
#print(counter)
avg_time = total_time / n_trials
print('Avg time take = {}'.format(avg_time))

