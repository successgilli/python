from matplotlib import pyplot as plt

movies = ['merlin', 'hulk', 'chandelier', 'opponent', 'inception']
num_oscars = [5, 11,3,8,10]

plt.bar(movies, num_oscars)
plt.ylabel('# of academy awards')
plt.title('My Favourite Movies')
plt.show()
