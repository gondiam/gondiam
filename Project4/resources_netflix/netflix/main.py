import numpy as np
import kmeans
import common
import naive_em
import em



#2.K-means
# =============================================================================
# X = np.loadtxt("toy_data.txt")
# 
# K = [1,2,3,4]
# seeds = [0, 1, 2, 3, 4]
# for k in K:    
#     for seed in seeds:
#         mix, postt = common.init(X,k,seed)
#         common.plot(X, mix, postt,"hola")
#         mix,postt,costM = kmeans.run(X, mix, postt)
#         print("K = {}, seed = {},costM = {}".format(k, seed,costM))
# 
# 
# #4.Comparing K-means and EM
# X = np.loadtxt("toy_data.txt")
# 
# K = [1,2,3,4]
# seeds = [0, 1, 2, 3, 4]
# print ("K-means")
# for k in K:    
#     for seed in seeds:
#         mix, postt = common.init(X,k,seed)
#         common.plot(X, mix, postt,"hola")
#         mix,postt,costM = kmeans.run(X, mix, postt)
#         print("K = {}, seed = {},costM = {}".format(k, seed,costM))
#         
# print ("EM")
# for k in K:    
#     for seed in seeds:
#         mix, postt = common.init(X,k,seed)
#         common.plot(X, mix, postt,"hola")
#         mix,postt,costM = kmeans.run(X, mix, postt)
#         print("K = {}, seed = {},costM = {}".format(k, seed,costM))
# =============================================================================
# TODO: Your code here

# =============================================================================
# #4. Comparing K-means and EM
# X = np.loadtxt("toy_data.txt")
# Ks = [1, 2, 3, 4]
# seeds = [0, 1, 2, 3, 4]
# BICs = np.empty(len(Ks))
# 
# for i, K in enumerate(Ks):
#     k_best_mix, k_best_post, k_best_cost = None, None, np.inf
#     em_best_mix, em_best_post, em_best_ll = None, None, -np.inf
#     for seed in seeds:
#         init_mix, init_post = common.init(X, K, seed)
#         k_mix, k_post, k_cost= kmeans.run(X, init_mix, init_post)
#         em_mix, em_post, em_ll= naive_em.run(X, init_mix, init_post)
#         print("K = {}, seed = {},K_cost = {}".format(K, seed,k_cost))
#         print("K = {}, seed = {},EM_cost = {}".format(K, seed,em_ll))
#         if k_cost < k_best_cost:
#             k_best_mix, k_best_post, k_best_cost = k_mix, k_post, k_cost
#         if em_ll > em_best_ll:
#             em_best_mix, em_best_post, em_best_ll = em_mix, em_post, em_ll
#     BICs[i] = common.bic(X, em_best_mix, em_best_ll)
#     common.plot(X, k_best_mix, k_best_post, "K-means K={}".format(K))
#     common.plot(X, em_best_mix, em_best_post, "EM K={}".format(K))
# 
# print("BICs: ", BICs)
# print("Best BIC: ", np.max(BICs))
# print("Best K: ", Ks[np.argmax(BICs)])
# #raise NotImplementedError
# 
# 
# #5. Comparing K-means and EM
# X = np.loadtxt("toy_data.txt")
# Ks = [1, 2, 3, 4]
# seeds = [0, 1, 2, 3, 4]
# BICs = np.empty(len(Ks))
# 
# for i, K in enumerate(Ks):
#     k_best_mix, k_best_post, k_best_cost = None, None, np.inf
#     em_best_mix, em_best_post, em_best_ll = None, None, -np.inf
#     for seed in seeds:
#         init_mix, init_post = common.init(X, K, seed)
#         k_mix, k_post, k_cost= kmeans.run(X, init_mix, init_post)
#         em_mix, em_post, em_ll= naive_em.run(X, init_mix, init_post)
#         print("K = {}, seed = {},K_cost = {}".format(K, seed,k_cost))
#         print("K = {}, seed = {},EM_cost = {}".format(K, seed,em_ll))
#         if k_cost < k_best_cost:
#             k_best_mix, k_best_post, k_best_cost = k_mix, k_post, k_cost
#         if em_ll > em_best_ll:
#             em_best_mix, em_best_post, em_best_ll = em_mix, em_post, em_ll
#     BICs[i] = common.bic(X, em_best_mix, em_best_ll)
#     common.plot(X, k_best_mix, k_best_post, "K-means K={}".format(K))
#     common.plot(X, em_best_mix, em_best_post, "EM K={}".format(K))
# print("BICs: ", BICs)
# print("Best BIC: ", np.max(BICs))
# print("Best K: ", Ks[np.argmax(BICs)])
# 
# 
# =============================================================================

X = np.loadtxt("netflix_incomplete.txt")

K = 12
seeds = [0, 1, 2, 3, 4]

em_best_mix, em_best_post, em_best_ll = None, None, -np.inf
for seed in seeds:
    init_mix, init_post = common.init(X, K, seed)
    em_mix, em_post, em_ll= em.run(X, init_mix, init_post)
    if em_ll > em_best_ll:
        em_best_mix, em_best_post, em_best_ll = em_mix, em_post, em_ll
print("K = {}, LL = {}".format(K, em_best_ll))

X_fill_pred = em.fill_matrix(X, em_best_mix)
X_fill = np.loadtxt("netflix_complete.txt")

print("X_filled Error:", common.rmse(X_fill_pred, X_fill))
