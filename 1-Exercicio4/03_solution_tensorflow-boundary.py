# Solução
# 3. Traçar o limite de decisão para este perceptron TensorFlow. Por que você acha que a implementação do TensorFlow é melhor do que a implementação do NumPy no conjunto de testes?

x_min = -2
y_min = (-(modelparams['weights'][0] * x_min) / modelparams['weights'][1] -
         (modelparams['bias'][0] / model_params['weights'][1]))

x_max = 2
y_max = (-(modelparams['weights'][0] * x_max) / modelparams['weights'][1] -
         (modelparams['bias'][0] / modelparams['weights'][1]))


fig, ax = plt.subplots(1, 2, sharex=True, figsize=(7, 3))

ax[0].plot([x_min, x_max], [y_min, y_max])
ax[1].plot([x_min, x_max], [y_min, y_max])

ax[0].scatter(X_train[y_train == 0, 0], X_train[y_train == 0, 1], label='class 0', marker='o')
ax[0].scatter(X_train[y_train == 1, 0], X_train[y_train == 1, 1], label='class 1', marker='s')

ax[1].scatter(X_test[y_test == 0, 0], X_test[y_test == 0, 1], label='class 0', marker='o')
ax[1].scatter(X_test[y_test == 1, 0], X_test[y_test == 1, 1], label='class 1', marker='s')

ax[1].legend(loc='upper left')
plt.show()


# O modelo TensorFlow funciona melhor no conjunto de testes apenas por chance aleatória.
# Lembre-se, o algoritmo perceptron deixa de aprender assim que classifica
# o conjunto de treinamento perfeitamente.
# Possíveis explicações por que há uma diferença entre o NumPy e
# os resultados TensorFlow poderiam ser, portanto, a precisão numérica, ou pequenas diferenças
# na nossa implementação.
