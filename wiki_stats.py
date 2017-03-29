#!/usr/bin/python3

import os
import sys
import math

import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            s = f.read().split()
            (n, _nlinks) = [int(x) for x in (s[0], s[1])]
            self._n = n

            # links - это edges
            self._titles = []   #
            self._sizes = array.array('L', [0]*n)       #
            self._links = array.array('L', [0]*_nlinks) #
            self._redirect = array.array('B', [0]*n)    #
            self._offset = array.array('L', [0]*(n+1))  #

            i = 2

            i = 5
            j = 0
            while i < len(s):
                k = i+int(s[i])
                tmp = [int(x) for x in s[i+1:k+1]]
                for lk in tmp:
                    self._links[j] = lk
                    j += 1
                i = k + 4

            j = 1
            i = 3
            kk = 0
            self._offset[0] = 0
            while j <= n:
                self._offset[j] = int(s[i+2]) + self._offset[j-1]
                self._titles.append(s[i-1])
                self._redirect[kk] = int(s[i+1])
                self._sizes[kk] = int(s[i])
                kk += 1
                i += int(s[i+2]) + 4
                j += 1
        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return len(self.get_links_from(_id))

    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id+1]]

    def get_id(self, title):
        for i in range(len(self._titles)):
            if title == self._titles[i]:
                return i

    def get_number_of_pages(self):
        return self._n

    def is_redirect(self, _id):
        if self._redirect[_id]:
            return True
        return False

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
        wg.is_redirect(4)
        print()
    else:
        print('Файл с графом не найден')
        sys.exit(-1)

    # TODO: статистика и гистограммы