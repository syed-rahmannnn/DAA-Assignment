vowel(a). vowel(e). vowel(i). vowel(o). vowel(u).

count_vowels([], 0).
count_vowels([H|T], N) :- vowel(H), count_vowels(T, N1), N is N1 + 1.
count_vowels([_|T], N) :- count_vowels(T, N).