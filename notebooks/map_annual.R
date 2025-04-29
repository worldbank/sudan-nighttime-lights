# Map of NTL Change

library(tidyverse)
library(sf)

proj_dir <- "~/Dropbox/World Bank/Side Work/Sudan Economic Monitor"

#ntl_df <- read_dta(file.path(proj_dir, "data", "Locality NTL.dta"))
ntl_df <- readRDS(file.path(proj_dir, "Data", "viirs-gee", "finaldata", "sudan_ntl_annual.Rds"))

ntl_wide_df <- ntl_df %>%
  dplyr::mutate(period = case_when(
    year == 2023 ~ "p1",
    year == 2024 ~ "p2"
  )) %>%
  filter(!is.na(period)) %>%
  dplyr::select(admin2Pcode, ntl_sum, period) %>%
  
  group_by(admin2Pcode, period) %>%
  dplyr::summarise(ntl_sum = mean(ntl_sum)) %>%
  ungroup() %>%
  
  pivot_wider(names_from = period,
              values_from = ntl_sum,
              id_cols = admin2Pcode) %>%
  
  dplyr::mutate(diff = p2 - p1,
                diff_log = log(p2) - log(p1),
                abs_diff = abs(p2 - p1),
                pc = (p2 - p1)/p1 * 100)


hdx2_sf <- readRDS(file.path(proj_dir, "data", "hdx-boundaries", "adm2_hdx.Rds"))

hdx2_sf <- hdx2_sf %>%
  left_join(ntl_wide_df, by = "admin2Pcode")

ggplot() +
  geom_sf(data = hdx2_sf,
          aes(fill = diff)) +
  theme_void() +
  scale_fill_viridis_c() +
  labs(fill = "Difference")
ggsave("~/Desktop/sudan_23_25_diff.png",
       height = 4, width = 4)

hdx2_sf$diff %>% summary()
ggplot() +
  geom_sf(data = hdx2_sf,
          aes(fill = diff)) +
  theme_void() +
  scale_fill_gradient2(
    low = "red",
    mid = "white",
    high = "blue",
    midpoint = 0,
    limits = c(-16300, 26151)
  ) +
  labs(fill = "Difference",
       title = "Comparing:\n(1) Dec 23, Jan-Feb 24 &\n(2) Dec 24, Jan-Feb 25")
ggsave("~/Desktop/sudan_diff.png",
       height = 4, width = 4)

hdx2_sf$diff_log %>% summary()
ggplot() +
  geom_sf(data = hdx2_sf,
          aes(fill = diff_log)) +
  theme_void() +
  scale_fill_gradient2(
    low = "red",
    mid = "white",
    high = "blue",
    midpoint = 0,
    limits = c(-2.23, 0.98)
  ) +
  labs(fill = "Absolute\nDifference")
ggsave("~/Desktop/sudan_23_25_abs_diff_log.png",
       height = 4, width = 4)

ntl_df %>%
  group_by(date) %>%
  dplyr::summarise(ntl_sum = sum(ntl_sum)) %>%
  ungroup() %>%
  dplyr::filter(date >= ymd("2020-01-01")) %>%
  
  ggplot() +
  geom_col(aes(x = date,
               y = ntl_sum))



