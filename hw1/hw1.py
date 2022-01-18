import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def exercise_1():
	# a
	x = np.linspace(-3,3,100)
	mu=0
	sigma=1
	pdf_x = (1/np.sqrt(2*np.pi*(sigma**2)))*np.exp(-((x-mu)**2)/(2*(sigma**2)))
	fig1,ax1 = plt.subplots()
	ax1.set_xlabel('x')
	ax1.set_ylabel('p(x)')
	ax1.set_title('PDF')
	ax1.plot(x,pdf_x)
	plt.show()

	# b
	fig2,ax2 = plt.subplots(2,1)
	sample = np.random.normal(mu,sigma,1000)
	mu_1,sig_1 = norm.fit(sample)
	y_value = norm(mu_1, sig_1)
	x = np.linspace(min(sample),max(sample), 1000)
	ax2[0].hist(sample,4,density=True)
	ax2[0].plot(x,y_value.pdf(x),'r-', lw=2, label='norm pdf')
	ax2[1].hist(sample,1000,density=True)
	ax2[1].plot(x,y_value.pdf(x),'r-', lw=2, label='norm pdf')
	print(mu_1)
	print(sig_1)
	plt.show()



if __name__ =='__main__':
	exercise_1()
