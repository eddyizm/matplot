from matplotlib import pyplot as plt

word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]
plt.close('all')
plt.figure()
plt.plot( years, word_length)
plt.savefig('Lesson_3/images/winning_word_lengths.png')
plt.figure(figsize=(7,3))
plt.plot(years, power_generated)
plt.savefig('Lesson_3/images/power_generated.png')
plt.show()