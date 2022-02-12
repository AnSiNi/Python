{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "eeb9d342",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None 0\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "prev_str = None\n",
    "str_cnt = 0\n",
    "#with open('C://Users//Работяга//Обучение//MapReduce//keywords_split.csv','r',encoding='utf-8') as kws:\n",
    "for i,line in sys.stdin:\n",
    "    word,nm = line.strip().split(',')\n",
    "    if prev_str:\n",
    "        if prev_str == word:\n",
    "            str_cnt  +=1\n",
    "        else:\n",
    "            print(prev_str,str_cnt)\n",
    "            str_cnt=1\n",
    "            prev_str = word\n",
    "    else:\n",
    "        str_cnt=1\n",
    "    prev_str = word \n",
    "print(prev_str,str_cnt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "88cde474",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
