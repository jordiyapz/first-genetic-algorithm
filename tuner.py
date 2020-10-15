# %% import
from matplotlib import pyplot as plt
import gea
import math as m
from main import fungsiFitness, stopping_crit

# %% hipothesis dan fitness
def tuner_h(fenotip):
  num_run = 3

  uk_pop, res, p_mut, x_rate = fenotip

  gen = gea.Gea(fungsi_fitness=fungsiFitness,
                ranges=((-1, 2), (-1, 1)),
                resolusi=round(res),
                ukuran_populasi=round(uk_pop))

  maks_generasi = int((10000 - uk_pop * (1 - x_rate)) \
                   / (uk_pop * x_rate))

  sum_fit = 0
  sum_it = 0


  for i in range(num_run):
    gen.reset()
    fen, it, _ = gen.fit(stopping_crit=stopping_crit,
                          maks_generasi=maks_generasi,
                          crossover_rate=x_rate,
                          peluang_mutasi=p_mut,
                          rekam_history=False)
    sum_fit += fungsiFitness(fen)
    sum_it += it

  mean_fit = sum_fit/num_run
  mean_it = sum_it/num_run

  return (mean_fit, mean_it)

def tuner_fit_func(fenotip):
  mean_fit, mean_it = tuner_h(fenotip)
  return mean_fit/17 * 1/mean_it

# %%
ranges = (
  (50, 800),  # ukuran populasi
  (4, 10),    # resolusi
  (.01, .2),  # peluang_mutasi
  (.1, 1)     # crossover rate
)

# %% main
tuner = gea.Gea(fungsi_fitness=tuner_fit_func,
              ranges=ranges,
              resolusi=8,
              ukuran_populasi=16)

fen, _, rekaman = tuner.fit(maks_generasi=20,
                            peluang_mutasi=.06,
                            rekam_history=True,
                            verbose=1)

print(fen)
print(tuner_h(fen))

plt.plot(rekaman)
# %%
