# Solução 
# 1. Treine um perceptron de peso zero com diferentes taxas de aprendizagem e compare os parâmetros do modelo e os limites de decisão uns com os outros. O que você observa?

small_lr_params = perceptron_train(X_train, y_train, learning_rate=0.01, mparams=None, zero_weights=True)

for _ in range(2):
    _ = perceptron_train(X_train, y_train, mparams=small_lr_params)

x_min_small = -2
y_min_small = (-(small_lr_params['weights'][0] * x_min) /
               small_lr_params['weights'][1] -
               (small_lr_params['bias'] / small_lr_params['weights'][1]))

x_max_small = 2
y_max_small = (-(small_lr_params['weights'][0] * x_max) /
               small_lr_params['weights'][1] -
               (small_lr_params['bias'] / small_lr_params['weights'][1]))


fig, ax = plt.subplots(1, 2, sharex=True, figsize=(7, 3))

ax[0].plot([x_min, x_max], [y_min, y_max])
ax[1].plot([x_min_small, x_max_small], [y_min_small, y_max_small])

ax[0].scatter(X_train[y_train == 0, 0], X_train[y_train == 0, 1], label='classe 0', marker='o')
ax[0].scatter(X_train[y_trai == 1, 0], X_train[y_train == 1, 1], label='classe 1', marker='s')

ax[1].scatter(X_train[y_train == 0, 0], X_train[y_train == 0, 1], label='classe 0', marker='o')
ax[1].scatter(X_train[y_train == 1, 0], X_train[y_train == 1, 1], label='classe 1', marker='s')

ax[1].legend(loc='lower right')

plt.ylim([-3, 3])
plt.xlim([-3, 3])
plt.show()


print('Learning=1. rate params:', model_params)
print('Learning=0.01 rate params:', small_lr_params)

# Como podemos ver, diminuir a taxa de aprendizado altera os parâmetros do modelo.
# Mas se olharmos de perto, podemos ver que no caso do perceptron
# a taxa de aprendizagem é apenas um fator de escala do vetor de peso e bias
# se inicializarmos os pesos para zero. Portanto, a região de decisão
# é exatamente o mesmo para diferentes taxas de aprendizado.
