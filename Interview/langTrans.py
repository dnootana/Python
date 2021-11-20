#!/usr/bin/env python3.8

table="".maketrans("0123456789","\N{Devanagari digit zero}\N{Devanagari digit one}"
"\N{Devanagari digit two}\N{Devanagari digit three}"
"\N{Devanagari digit four}\N{Devanagari digit five}"
"\N{Devanagari digit six}\N{Devanagari digit seven}"
"\N{Devanagari digit eight}\N{Devanagari digit nine}")
print("0123456789".translate(table))