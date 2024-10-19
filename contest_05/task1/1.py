import matplotlib.pyplot as plt
import numpy as np

P = np.arange(1, 8, dtype=float)
adjustment_factor_blue = np.linspace(2.3, 1, len(P))
adjustment_factor_green = np.linspace(2, 1, len(P))
error_01 = np.exp(-3.4 * P) * 10 ** -1.8 / adjustment_factor_blue
error_05 = np.exp(-1.5 * P) * 10 ** -1.4 / adjustment_factor_green
error_09 = np.exp(-0.8 * P) * 10 ** -1.1

plt.figure(figsize=(8, 6))

plt.plot(P, error_01, 'b^-', label=r'$\sigma = 0.1$', markersize=8)
plt.plot(P, error_05, 'gv-', label=r'$\sigma = 0.5$', markersize=8)
plt.plot(P, error_09, 'rs-', label=r'$\sigma = 0.9$', markersize=8)

plt.yscale('log')
plt.ylim(1.0E-13, 1.0E-1)
plt.xlim(1, 8)

plt.yticks([1.0E-1, 1.0E-3, 1.0E-5, 1.0E-7, 1.0E-9, 1.0E-11, 1.0E-13], [r'$1.0E-1$', r'$1.0E-3$', r'$1.0E-5$', r'$1.0E-7$', r'$1.0E-9$', r'$1.0E-11$', r'$1.0E-13$'])

plt.xlabel('Highest Degree of Polynomials P')
plt.ylabel(r'$L_2$ error')
plt.title('Convergence plot')

plt.legend(loc='lower left', fontsize=12)

plt.grid(True, which="both", ls="--")

plt.show()

print('1')
