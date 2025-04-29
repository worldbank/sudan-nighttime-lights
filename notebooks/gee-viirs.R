#### MAIN PARAMS
proj_dir     <- "~/Dropbox/World Bank/Side Work/Sudan Economic Monitor"
iso3_code    <- c("SDN")
iso2_code    <- c("SD")
pc_base_year <- 2019

#### Packages
library(tidyverse)
library(sf)
library(leaflet)
library(leaflet.providers)
library(ggpubr)
library(terra)
library(tidyterra)
library(gtools)
library(readxl)
library(janitor)
library(geodata)
library(exactextractr)
library(haven)
library(blackmarbler)
library(dplyr)
library(readxl)
library(janitor)
library(ggpubr)
library(WDI)
library(kableExtra)
library(terra)
library(DT)

#### Paths

## Define
data_dir       <- file.path(proj_dir, "data")
ntl_bm_dir     <- file.path(data_dir, "Nighttime Lights BlackMarble")
gadm_dir       <- file.path(data_dir, "GADM")
gas_flare_dir  <- file.path(data_dir, "gas-flaring")

r2 <- rast(file.path(data_dir, "viirs-gee", "rawdata", "sd_viirs_corrected_monthly_start_202001_avg_rad.tif"))

adm_sf <- readRDS(file.path(data_dir, "hdx-boundaries", "adm2_hdx.Rds"))
adm_sf$uid <- 1:nrow(adm_sf)

# 1/ ---------------------------------------------------------------------------
r <- rast(file.path(data_dir, "viirs-gee", "rawdata", "sd_viirs_corrected_monthly_start_201401_201912_avg_rad.tif"))
r[r < 0] <- 0

## Sum
ntl_sum_df <- exact_extract(r, adm_sf, "sum")
ntl_sum_df$uid <- adm_sf$uid

ntl_sum_df <- ntl_sum_df %>%
  pivot_longer(cols = -uid) %>%
  dplyr::mutate(name = name %>%
                  str_replace_all("[:alpha:]|[:punct:]", "") %>%
                  as.numeric() %>%
                  replace_na(0))
ntl_sum_df$date <- ymd("2014-01-01") + months(ntl_sum_df$name)

ntl_sum_df <- ntl_sum_df %>%
  dplyr::select(uid, value, date) %>%
  dplyr::rename(ntl_sum = value)

## Mean
ntl_mean_df <- exact_extract(r, adm_sf, "mean")
ntl_mean_df$uid <- adm_sf$uid

ntl_mean_df <- ntl_mean_df %>%
  pivot_longer(cols = -uid) %>%
  dplyr::mutate(name = name %>%
                  str_replace_all("[:alpha:]|[:punct:]", "") %>%
                  as.numeric() %>%
                  replace_na(0))
ntl_mean_df$date <- ymd("2014-01-01") + months(ntl_mean_df$name)

ntl_mean_df <- ntl_mean_df %>%
  dplyr::select(uid, value, date) %>%
  dplyr::rename(ntl_mean = value)

## Merge/Clean
ntl_df <- ntl_sum_df %>%
  left_join(ntl_mean_df, by = c("uid", "date"))

adm_df <- adm_sf %>%
  st_drop_geometry() %>%
  dplyr::select(-date)

ntl_1_df <- ntl_df %>%
  left_join(adm_df, by = "uid")

# 2/ ---------------------------------------------------------------------------
r <- rast(file.path(data_dir, "viirs-gee", "rawdata", "sd_viirs_corrected_monthly_start_202001_avg_rad.tif"))
r[r < 0] <- 0

## Sum
ntl_sum_df <- exact_extract(r, adm_sf, "sum")
ntl_sum_df$uid <- adm_sf$uid

ntl_sum_df <- ntl_sum_df %>%
  pivot_longer(cols = -uid) %>%
  dplyr::mutate(name = name %>%
                  str_replace_all("[:alpha:]|[:punct:]", "") %>%
                  as.numeric() %>%
                  replace_na(0))
ntl_sum_df$date <- ymd("2020-01-01") + months(ntl_sum_df$name)

ntl_sum_df <- ntl_sum_df %>%
  dplyr::select(uid, value, date) %>%
  dplyr::rename(ntl_sum = value)

## Mean
ntl_mean_df <- exact_extract(r, adm_sf, "mean")
ntl_mean_df$uid <- adm_sf$uid

ntl_mean_df <- ntl_mean_df %>%
  pivot_longer(cols = -uid) %>%
  dplyr::mutate(name = name %>%
                  str_replace_all("[:alpha:]|[:punct:]", "") %>%
                  as.numeric() %>%
                  replace_na(0))
ntl_mean_df$date <- ymd("2020-01-01") + months(ntl_mean_df$name)

ntl_mean_df <- ntl_mean_df %>%
  dplyr::select(uid, value, date) %>%
  dplyr::rename(ntl_mean = value)

## Merge/Clean
ntl_df <- ntl_sum_df %>%
  left_join(ntl_mean_df, by = c("uid", "date"))

adm_df <- adm_sf %>%
  st_drop_geometry() %>%
  dplyr::select(-date)

ntl_2_df <- ntl_df %>%
  left_join(adm_df, by = "uid")

# Append -----------------------------------------------------------------------
ntl_all_df <- bind_rows(ntl_1_df,
                        ntl_2_df)

write_dta(ntl_all_df, file.path(data_dir, "viirs-gee", "finaldata", "sudan_ntl_monthly.dta"))
saveRDS(ntl_all_df, file.path(data_dir, "viirs-gee", "finaldata", "sudan_ntl_monthly.Rds"))
