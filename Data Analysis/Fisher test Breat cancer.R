#Fisher test
TeaTasting<-matrix(c(39, 30961, 63, 30937),
       nrow = 2,
       dimnames = list(Guess = c("Death", "Survive"),
                       Group = c("Treatment", "Control")));TeaTasting
fisher.test(TeaTasting, alternative = "less")
