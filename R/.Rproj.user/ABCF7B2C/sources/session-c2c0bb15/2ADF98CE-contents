data <- read.csv('../output.csv')

library(ggplot2)
library(dplyr)


s <-
data |> 
  filter(grepl('CLAUCIO', X0))

all_ranges <-
data |> 
  mutate(X4 = as.numeric(X4)) |> 
  filter(X4 > 0)


get_ecdf <- function(x) {
  y <-
    all_ranges |> 
    filter(X6 == s$X6[x]) |> 
    pull(X4)
  
  ecdf(y)(s$X4[x])
}

s$indice <- sapply(1:4, get_ecdf)

to_ind <- 
  s |> 
  mutate(X6 = case_when(
    grepl('100 METROS LIV', X6) ~ '100M Free',
    grepl('100 METROS COS', X6) ~ '100M Backstroke',
    grepl('200 METROS', X6) ~ '200M Medley',
    grepl('400 METROS', X6) ~ '400M Free',
  )) |> 
  filter(X6 != '100M Free')

all_ranges |> 
  filter(X6 %in% s$X6) |> 
  mutate(X6 = case_when(
    grepl('100 METROS LIV', X6) ~ '100M Free',
    grepl('100 METROS COS', X6) ~ '100M Backstroke',
    grepl('200 METROS', X6) ~ '200M Medley',
    grepl('400 METROS', X6) ~ '400M Free',
  )) |> 
  filter(X6 != '100M Free') |> 
  ggplot(aes(x = X4)) +
  geom_histogram(bins = 13, color='white') +
  geom_text(data = to_ind, aes(x = 600, y = Inf, label = round(indice, 2)), vjust = 2) +
  geom_vline(data = to_ind, aes(xintercept = X4), color = 'red') +
  labs(x = 'FINA Points', y = 'Count') +
  theme_linedraw()+
  facet_wrap(~X6, scales = 'free', ncol = 2)
