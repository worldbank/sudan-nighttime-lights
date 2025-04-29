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

adm_sf <- readRDS(file.path(data_dir, "hdx-boundaries", "adm2_hdx.Rds"))
adm_sf$uid <- 1:nrow(adm_sf)

# 1/ ---------------------------------------------------------------------------
ntl_df <- map_df(2013:2024, function(year_i){
  print(year_i)
  r <- rast(file.path(data_dir, "viirs-gee", "rawdata", "annual", paste0("SDN_viirs_corrected_mean_",year_i,".tif")))
  r[r < 0] <- 0
  
  adm_sf$ntl_sum  <- exact_extract(r, adm_sf, "sum")
  adm_sf$ntl_mean <- exact_extract(r, adm_sf, "mean")
  adm_sf$year <- year_i
  
  adm_df <- adm_sf %>%
    st_drop_geometry()
  
  return(adm_df)
})

write_dta(ntl_df, file.path(data_dir, "viirs-gee", "finaldata", "sudan_ntl_annual.dta"))
saveRDS(ntl_df, file.path(data_dir, "viirs-gee", "finaldata", "sudan_ntl_annual.Rds"))

ntl_df %>%
  group_by(year) %>%
  dplyr::summarise(ntl_sum = sum(ntl_sum)) %>%
  ungroup() %>%
  
  ggplot() +
  geom_col(aes(x = year,
               y = ntl_sum))

