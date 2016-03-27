#!/usr/bin/env python3
# -*-coding:utf-8-*-


class Equality(object):

    def __eq__(self, other):
        a = isinstance(other, self.__class__)
        b = self.__dict__ == other.__dict__ if a else False
        return (a and b)

    def __ne__(self, other):
        return not self.__eq__(other)
