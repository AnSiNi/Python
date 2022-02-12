{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a5558056",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "#with open('C://Users//Работяга//Обучение//MapReduce//keywords_split.csv','w',encoding='utf-8') as kws:\n",
    "#    with open('C://Users//Работяга//Обучение//MapReduce//keywords.csv','r',encoding='utf-8') as kw:\n",
    "for i,line in sys.stdin:\n",
    "     str_l,shw=line.strip().split(',')\n",
    "     str_spl=str_l.strip().split(' ')\n",
    "     for num in range(len(str_spl)):\n",
    "         print('{},1\\n'.format(str_spl[num]))"
   ]
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
